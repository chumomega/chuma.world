#!/usr/bin/env python3
"""Record a short looping clip of SneakySneaks for the services-page
case study. Uses Playwright's built-in WebM recording — no ffmpeg
pipeline, no Selenium grid. The output is converted to MP4 + GIF.

The walkthrough is intentionally simple (load page, slowly scroll
through the available content) because the live site is currently
barebones. Re-run after each feature ships to refresh the clip.

Run:
    ../tempo/.venv/bin/python tools/record_sneakysneaks.py
"""
from pathlib import Path
import subprocess
import shutil

from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "assets" / "demos"
SITE = "https://sneakysneaks-production.up.railway.app/"

# 1280x720 = 16:9 landscape, the conventional "desktop product" tile
# proportion. SneakySneaks is a web product so the desktop framing
# tells the right story.
WIDTH, HEIGHT = 1280, 720


def record() -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_video_dir = OUT_DIR / "_raw"
    raw_video_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": WIDTH, "height": HEIGHT},
            record_video_dir=str(raw_video_dir),
            record_video_size={"width": WIDTH, "height": HEIGHT},
        )
        page = context.new_page()
        page.goto(SITE, wait_until="networkidle", timeout=30_000)

        # Brief beat at the top of the page.
        page.wait_for_timeout(1500)

        # Slow scroll through whatever content the page has. Easing the
        # scroll keeps the recording feeling intentional rather than
        # robotic. ~6 seconds total.
        page.evaluate(
            """async () => {
                const total = document.body.scrollHeight;
                const steps = 30;
                for (let i = 1; i <= steps; i++) {
                    window.scrollTo({top: (total * i) / steps, behavior: 'auto'});
                    await new Promise(r => setTimeout(r, 200));
                }
            }"""
        )

        # Beat at the bottom before closing.
        page.wait_for_timeout(1200)
        context.close()
        browser.close()

    # Playwright writes a .webm into raw_video_dir. Move/rename it.
    webm = next(raw_video_dir.glob("*.webm"))
    final_webm = OUT_DIR / "sneakysneaks.webm"
    shutil.move(str(webm), final_webm)
    raw_video_dir.rmdir()
    print(f"wrote {final_webm.relative_to(REPO)}")
    return final_webm


def to_mp4(webm: Path) -> Path:
    """ffmpeg → MP4 (H.264) for cross-browser <video> tag support."""
    mp4 = webm.with_suffix(".mp4")
    if shutil.which("ffmpeg") is None:
        print("ffmpeg not installed — skipping MP4 conversion")
        return mp4
    subprocess.run([
        "ffmpeg", "-y", "-i", str(webm),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-an",                       # no audio
        str(mp4),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"wrote {mp4.relative_to(mp4.parent.parent.parent)}")
    return mp4


if __name__ == "__main__":
    webm = record()
    to_mp4(webm)
