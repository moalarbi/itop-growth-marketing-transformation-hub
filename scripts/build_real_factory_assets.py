from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "صور من المصنع"
OUT = ROOT / "assets" / "images"
SIZE = (1600, 900)


ASSETS = [
    {
        "out": "hero-itop-factory.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.36.jpeg",
        "mode": "cover",
        "center": (0.54, 0.56),
    },
    {
        "out": "01-executive-case.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.34 (1).jpeg",
        "mode": "cover",
        "center": (0.56, 0.55),
    },
    {
        "out": "02-dual-market.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.59.24.jpeg",
        "mode": "cover",
        "center": (0.55, 0.54),
    },
    {
        "out": "03-digital-infrastructure.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.34.jpeg",
        "mode": "contain",
    },
    {
        "out": "04-seo-growth.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.35 (3).jpeg",
        "mode": "contain",
    },
    {
        "out": "05-keyword-strategy.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.59.24 (3).jpeg",
        "mode": "contain",
    },
    {
        "out": "06-social-linkedin.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.53.13 (1).jpeg",
        "mode": "contain",
    },
    {
        "out": "07-paid-leads.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.58.55 (3).jpeg",
        "mode": "contain",
    },
    {
        "out": "08-brand-positioning.webp",
        "src": "WhatsApp Image 2026-06-04 at 15.07.13.jpeg",
        "mode": "contain",
    },
    {
        "out": "09-product-marketing.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.58.55 (2).jpeg",
        "mode": "contain",
    },
    {
        "out": "10-content-media.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.33 (1).jpeg",
        "mode": "contain",
    },
    {
        "out": "11-retail-distribution.webp",
        "src": "WhatsApp Image 2026-06-04 at 15.00.39 (1).jpeg",
        "mode": "cover",
        "center": (0.50, 0.50),
    },
    {
        "out": "12-projects-acquisition.webp",
        "src": "WhatsApp Image 2026-06-04 at 15.00.39 (3).jpeg",
        "mode": "contain",
    },
    {
        "out": "13-crm-kpi.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.34 (2).jpeg",
        "mode": "contain",
    },
    {
        "out": "14-department-roadmap.webp",
        "src": "WhatsApp Image 2026-06-04 at 14.51.35.jpeg",
        "mode": "cover",
        "center": (0.52, 0.55),
    },
    {
        "out": "15-executive-recommendation.webp",
        "src": "WhatsApp Image 2026-06-04 at 15.07.12.jpeg",
        "mode": "contain",
    },
]


def cover(img: Image.Image, center=(0.5, 0.5)) -> Image.Image:
    return ImageOps.fit(
        img,
        SIZE,
        method=Image.Resampling.LANCZOS,
        centering=center,
    )


def contain_with_real_photo_background(img: Image.Image) -> Image.Image:
    background = cover(img).filter(ImageFilter.GaussianBlur(radius=24))
    background = ImageEnhanceWrapper(background, brightness=0.72)
    foreground = ImageOps.contain(img, SIZE, method=Image.Resampling.LANCZOS)
    canvas = background.copy()
    x = (SIZE[0] - foreground.width) // 2
    y = (SIZE[1] - foreground.height) // 2
    canvas.paste(foreground, (x, y))
    return canvas


def ImageEnhanceWrapper(img: Image.Image, brightness: float) -> Image.Image:
    from PIL import ImageEnhance

    return ImageEnhance.Brightness(img).enhance(brightness)


def build_asset(item: dict[str, object]) -> Path:
    src = SRC / str(item["src"])
    img = Image.open(src)
    img = ImageOps.exif_transpose(img).convert("RGB")
    if item.get("mode") == "cover":
        result = cover(img, tuple(item.get("center", (0.5, 0.5))))
    else:
        result = contain_with_real_photo_background(img)
    out = OUT / str(item["out"])
    result.save(out, "WEBP", quality=88, method=6)
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for item in ASSETS:
        out = build_asset(item)
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
