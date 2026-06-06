from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


W, H = 1600, 900
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images"

IVORY = (246, 241, 232)
PAPER = (255, 250, 240)
GREEN = (18, 60, 53)
GREEN_2 = (29, 90, 77)
ORANGE = (200, 117, 62)
CHARCOAL = (28, 36, 33)
MUTED = (105, 115, 110)
LINE = (70, 84, 76)


ASSETS = [
    ("hero-itop-factory.webp", "hero"),
    ("01-executive-case.webp", "executive_case"),
    ("02-dual-market.webp", "dual_market"),
    ("03-digital-infrastructure.webp", "digital_infra"),
    ("04-seo-growth.webp", "search"),
    ("05-keyword-strategy.webp", "keywords"),
    ("06-social-linkedin.webp", "social"),
    ("07-paid-leads.webp", "paid"),
    ("08-brand-positioning.webp", "brand"),
    ("09-product-marketing.webp", "products"),
    ("10-content-media.webp", "content"),
    ("11-retail-distribution.webp", "distribution"),
    ("12-projects-acquisition.webp", "projects"),
    ("13-crm-kpi.webp", "crm"),
    ("14-department-roadmap.webp", "roadmap"),
    ("15-executive-recommendation.webp", "recommendation"),
]


def rgba(c, a=255):
    return (*c, a)


def make_canvas(seed: int):
    rng = random.Random(seed)
    img = Image.new("RGBA", (W, H), rgba(IVORY))
    px = img.load()
    for y in range(H):
        for x in range(W):
            n = rng.randint(-9, 8)
            r, g, b, a = px[x, y]
            px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)), a)
    d = ImageDraw.Draw(img, "RGBA")
    for _ in range(540):
        x = rng.randint(0, W)
        y = rng.randint(0, H)
        length = rng.randint(45, 260)
        d.line((x, y, x + length, y + rng.randint(-8, 8)), fill=rgba((160, 145, 120), rng.randint(9, 22)), width=1)
    for x in range(-80, W + 80, 78):
        d.line((x, 0, x + 520, H), fill=rgba(GREEN, 10), width=1)
    for y in range(80, H, 92):
        d.line((0, y, W, y), fill=rgba(GREEN, 9), width=1)
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette, "RGBA")
    for i in range(80):
        alpha = int(2.2 * i)
        vd.rectangle((i * 3, i * 2, W - i * 3, H - i * 2), outline=rgba(GREEN, max(0, 50 - alpha // 4)), width=2)
    img.alpha_composite(vignette)
    return img, ImageDraw.Draw(img, "RGBA"), rng


def rough_line(d, pts, color=GREEN, width=4, jitter=3, reps=2, rng=None, alpha=230):
    rng = rng or random
    for _ in range(reps):
        out = []
        for x, y in pts:
            out.append((x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter)))
        d.line(out, fill=rgba(color, alpha), width=width, joint="curve")


def rough_rect(d, box, outline=GREEN, width=4, fill=None, rng=None, reps=2):
    x1, y1, x2, y2 = box
    if fill:
        d.rectangle(box, fill=fill)
    pts = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1, y1)]
    rough_line(d, pts, outline, width=width, jitter=3, reps=reps, rng=rng)


def rough_poly(d, pts, outline=GREEN, width=4, fill=None, rng=None):
    if fill:
        d.polygon(pts, fill=fill)
    rough_line(d, pts + [pts[0]], outline, width=width, jitter=3, reps=2, rng=rng)


def rough_ellipse(d, box, outline=GREEN, width=4, fill=None, rng=None, reps=2):
    rng = rng or random
    if fill:
        d.ellipse(box, fill=fill)
    for _ in range(reps):
        off = [rng.uniform(-3, 3) for _ in range(4)]
        d.ellipse((box[0] + off[0], box[1] + off[1], box[2] + off[2], box[3] + off[3]), outline=rgba(outline, 225), width=width)


def hatch(d, box, color=GREEN, spacing=18, width=2, alpha=82, slope=1):
    x1, y1, x2, y2 = box
    for x in range(int(x1 - (y2 - y1)), int(x2 + (y2 - y1)), spacing):
        if slope > 0:
            d.line((x, y2, x + (y2 - y1), y1), fill=rgba(color, alpha), width=width)
        else:
            d.line((x, y1, x + (y2 - y1), y2), fill=rgba(color, alpha), width=width)


def frame(d, rng):
    rough_rect(d, (62, 54, W - 62, H - 54), outline=GREEN, width=3, rng=rng, reps=2)
    d.rectangle((78, 70, W - 78, H - 70), outline=rgba(ORANGE, 80), width=1)
    for x, y in [(98, 92), (W - 98, 92), (98, H - 92), (W - 98, H - 92)]:
        rough_ellipse(d, (x - 10, y - 10, x + 10, y + 10), outline=ORANGE, width=3, fill=rgba(ORANGE, 40), rng=rng)


def factory_background(d, rng, ybase=660):
    for x in range(90, W, 180):
        rough_line(d, [(x, 145), (x + rng.randint(-12, 12), ybase)], LINE, width=3, jitter=2, rng=rng, alpha=95)
    for y in range(170, 390, 58):
        rough_line(d, [(100, y), (W - 100, y - 34)], LINE, width=2, jitter=2, rng=rng, alpha=70)
    rough_line(d, [(120, ybase), (W - 120, ybase - 10)], GREEN, width=4, rng=rng, alpha=110)
    rough_line(d, [(140, ybase + 50), (W - 150, ybase + 28)], LINE, width=2, rng=rng, alpha=75)
    for x in range(250, 1300, 300):
        rough_rect(d, (x, 440, x + 190, 590), outline=GREEN, width=3, fill=rgba(PAPER, 54), rng=rng)
        hatch(d, (x + 10, 452, x + 180, 580), color=GREEN, spacing=18, alpha=34)
    rough_line(d, [(160, 610), (1450, 610)], GREEN, width=6, rng=rng, alpha=130)
    for x in range(200, 1350, 130):
        rough_line(d, [(x, 620), (x + 70, 548)], ORANGE, width=3, rng=rng, alpha=115)


def pipe_stack(d, rng, x, y, rows=4, cols=8, r=24, length=360, color=GREEN):
    for row in range(rows):
        for col in range(cols):
            ox = x + col * r * 1.65 + (row % 2) * r * .82
            oy = y + row * r * 1.22
            rough_ellipse(d, (ox, oy, ox + r * 1.75, oy + r * 1.15), outline=color, width=3, fill=rgba(PAPER, 85), rng=rng)
            d.ellipse((ox + 8, oy + 6, ox + r * 1.75 - 8, oy + r * 1.15 - 6), outline=rgba(color, 90), width=2)
            rough_line(d, [(ox + r * .9, oy), (ox + length, oy - 35)], color, width=3, rng=rng, alpha=120)
    hatch(d, (x, y, x + length + 30, y + rows * r * 1.3), color=GREEN, spacing=32, alpha=22)


def coil(d, rng, cx, cy, rx=170, ry=100, turns=7, color=CHARCOAL):
    for i in range(turns):
        t = i / max(1, turns - 1)
        box = (cx - rx + t * 16, cy - ry + t * 10, cx + rx - t * 16, cy + ry - t * 10)
        rough_ellipse(d, box, outline=color, width=5, rng=rng, reps=2)
    for a in range(0, 360, 45):
        rad = math.radians(a)
        rough_line(d, [(cx, cy), (cx + math.cos(rad) * rx * .88, cy + math.sin(rad) * ry * .88)], ORANGE, width=4, rng=rng, alpha=120)
    rough_ellipse(d, (cx - 28, cy - 18, cx + 28, cy + 18), outline=ORANGE, width=4, fill=rgba(ORANGE, 36), rng=rng)


def fittings(d, rng, x, y, scale=1.0, count=20):
    for i in range(count):
        px = x + rng.randint(0, int(360 * scale))
        py = y + rng.randint(0, int(120 * scale))
        s = rng.randint(int(18 * scale), int(35 * scale))
        if i % 3 == 0:
            rough_rect(d, (px, py, px + s * 1.6, py + s), outline=GREEN_2, width=3, fill=rgba(GREEN_2, 58), rng=rng)
            rough_ellipse(d, (px - s * .15, py, px + s * .55, py + s), outline=GREEN, width=3, rng=rng)
        elif i % 3 == 1:
            rough_ellipse(d, (px, py, px + s * 1.25, py + s * 1.25), outline=GREEN_2, width=3, fill=rgba(GREEN_2, 50), rng=rng)
            rough_ellipse(d, (px + s * .34, py + s * .34, px + s * .9, py + s * .9), outline=GREEN, width=2, rng=rng)
        else:
            rough_line(d, [(px, py + s), (px + s, py + s), (px + s, py)], GREEN_2, width=8, jitter=2, reps=2, rng=rng, alpha=200)
            rough_ellipse(d, (px - 5, py + s - 11, px + 18, py + s + 11), outline=GREEN, width=2, rng=rng)
            rough_ellipse(d, (px + s - 11, py - 5, px + s + 11, py + 18), outline=GREEN, width=2, rng=rng)


def board(d, rng, box, cards=6, strings=True):
    rough_rect(d, box, outline=GREEN, width=4, fill=rgba(PAPER, 120), rng=rng)
    x1, y1, x2, y2 = box
    points = []
    for i in range(cards):
        cw = rng.randint(95, 155)
        ch = rng.randint(62, 92)
        cx = rng.randint(int(x1 + 30), int(x2 - cw - 30))
        cy = rng.randint(int(y1 + 30), int(y2 - ch - 30))
        rough_rect(d, (cx, cy, cx + cw, cy + ch), outline=LINE, width=2, fill=rgba(IVORY, 180), rng=rng)
        for yy in range(cy + 18, cy + ch - 12, 18):
            rough_line(d, [(cx + 18, yy), (cx + cw - 18, yy)], LINE, width=1, jitter=1, rng=rng, alpha=90)
        points.append((cx + cw // 2, cy + ch // 2))
        rough_ellipse(d, (cx + 7, cy + 7, cx + 20, cy + 20), outline=ORANGE, width=2, fill=rgba(ORANGE, 80), rng=rng)
    if strings and len(points) > 1:
        for a, b in zip(points, points[1:]):
            rough_line(d, [a, b], ORANGE, width=3, jitter=1, reps=1, rng=rng, alpha=115)


def laptop(d, rng, x, y, w=360, h=210):
    rough_rect(d, (x, y, x + w, y + h), outline=GREEN, width=4, fill=rgba(PAPER, 160), rng=rng)
    for i in range(4):
        rough_rect(d, (x + 28 + i * 74, y + 34, x + 85 + i * 74, y + 72), outline=LINE, width=2, fill=rgba(GREEN_2, 28), rng=rng)
    for i in range(3):
        rough_line(d, [(x + 36, y + 105 + i * 32), (x + w - 42, y + 98 + i * 29)], LINE, width=2, rng=rng, alpha=95)
    rough_poly(d, [(x - 38, y + h + 8), (x + w + 38, y + h + 8), (x + w + 82, y + h + 64), (x - 82, y + h + 64)], outline=GREEN, fill=rgba(IVORY, 128), rng=rng)


def magnifier(d, rng, cx, cy, r=120):
    rough_ellipse(d, (cx - r, cy - r, cx + r, cy + r), outline=GREEN, width=8, fill=rgba(PAPER, 46), rng=rng)
    rough_line(d, [(cx + r * .62, cy + r * .62), (cx + r * 1.55, cy + r * 1.55)], GREEN, width=12, rng=rng)
    for i in range(6):
        rough_line(d, [(cx - r + 40, cy - 70 + i * 26), (cx + r - 50, cy - 80 + i * 31)], LINE, width=2, rng=rng, alpha=90)


def person(d, rng, x, y, scale=1.0, pose="stand"):
    rough_ellipse(d, (x - 18 * scale, y - 70 * scale, x + 18 * scale, y - 34 * scale), outline=CHARCOAL, width=max(2, int(3 * scale)), fill=rgba(PAPER, 70), rng=rng)
    rough_line(d, [(x - 30 * scale, y - 32 * scale), (x + 30 * scale, y - 32 * scale)], GREEN, width=max(2, int(5 * scale)), rng=rng)
    rough_line(d, [(x, y - 32 * scale), (x, y + 48 * scale)], GREEN, width=max(3, int(7 * scale)), rng=rng)
    rough_line(d, [(x, y + 48 * scale), (x - 35 * scale, y + 105 * scale)], GREEN, width=max(2, int(5 * scale)), rng=rng)
    rough_line(d, [(x, y + 48 * scale), (x + 35 * scale, y + 105 * scale)], GREEN, width=max(2, int(5 * scale)), rng=rng)
    if pose == "point":
        rough_line(d, [(x + 22 * scale, y - 22 * scale), (x + 85 * scale, y - 48 * scale)], ORANGE, width=max(2, int(5 * scale)), rng=rng)
    else:
        rough_line(d, [(x - 20 * scale, y - 18 * scale), (x - 55 * scale, y + 30 * scale)], GREEN, width=max(2, int(4 * scale)), rng=rng)
        rough_line(d, [(x + 20 * scale, y - 18 * scale), (x + 55 * scale, y + 30 * scale)], GREEN, width=max(2, int(4 * scale)), rng=rng)
    rough_line(d, [(x - 24 * scale, y - 64 * scale), (x + 24 * scale, y - 64 * scale)], ORANGE, width=max(2, int(5 * scale)), rng=rng)


def camera(d, rng, x, y, scale=1.0):
    rough_rect(d, (x, y, x + 170 * scale, y + 95 * scale), outline=GREEN, width=4, fill=rgba(PAPER, 120), rng=rng)
    rough_ellipse(d, (x + 58 * scale, y + 24 * scale, x + 116 * scale, y + 82 * scale), outline=GREEN, width=5, rng=rng)
    rough_line(d, [(x + 170 * scale, y + 46 * scale), (x + 255 * scale, y + 14 * scale), (x + 255 * scale, y + 80 * scale), (x + 170 * scale, y + 56 * scale)], ORANGE, width=4, rng=rng)
    rough_line(d, [(x + 78 * scale, y + 95 * scale), (x + 55 * scale, y + 180 * scale)], GREEN, width=4, rng=rng)
    rough_line(d, [(x + 92 * scale, y + 95 * scale), (x + 150 * scale, y + 182 * scale)], GREEN, width=4, rng=rng)


def scene_hero(d, rng):
    factory_background(d, rng, 650)
    coil(d, rng, 480, 470, 210, 130, 8)
    pipe_stack(d, rng, 1010, 500, rows=4, cols=7, r=28, length=300)
    rough_rect(d, (520, 610, 1070, 760), outline=GREEN, width=4, fill=rgba(PAPER, 130), rng=rng)
    fittings(d, rng, 560, 635, 1.25, 24)
    laptop(d, rng, 660, 260, 360, 210)
    rough_line(d, [(555, 280), (395, 360), (330, 450)], ORANGE, width=5, rng=rng, alpha=130)
    rough_line(d, [(1000, 280), (1190, 380), (1295, 505)], ORANGE, width=5, rng=rng, alpha=130)
    person(d, rng, 360, 610, 1.2)
    person(d, rng, 1225, 590, 1.0, "point")


def scene_executive_case(d, rng):
    factory_background(d, rng, 710)
    board(d, rng, (250, 150, 760, 520), cards=7)
    coil(d, rng, 1080, 470, 160, 100, 6)
    pipe_stack(d, rng, 950, 610, rows=3, cols=6, r=24, length=320)
    magnifier(d, rng, 580, 570, 110)
    rough_line(d, [(760, 360), (950, 455)], ORANGE, width=4, rng=rng, alpha=130)
    person(d, rng, 820, 685, 1.05, "point")


def scene_dual_market(d, rng):
    rough_line(d, [(800, 110), (800, 790)], GREEN, width=5, rng=rng, alpha=100)
    factory_background(d, rng, 710)
    pipe_stack(d, rng, 170, 520, rows=4, cols=6, r=26, length=300)
    rough_rect(d, (160, 260, 430, 455), outline=GREEN, width=4, fill=rgba(PAPER, 120), rng=rng)
    rough_rect(d, (190, 305, 265, 455), outline=LINE, width=3, fill=rgba(GREEN_2, 35), rng=rng)
    fittings(d, rng, 465, 520, .88, 13)
    board(d, rng, (905, 180, 1370, 500), cards=5)
    rough_rect(d, (950, 555, 1325, 720), outline=GREEN, width=4, fill=rgba(PAPER, 100), rng=rng)
    for i in range(5):
        rough_line(d, [(980, 590 + i * 26), (1290, 575 + i * 25)], LINE, width=2, rng=rng, alpha=90)
    person(d, rng, 910, 700, .95, "point")


def scene_digital_infra(d, rng):
    factory_background(d, rng, 700)
    laptop(d, rng, 420, 250, 560, 300)
    pipe_stack(d, rng, 1030, 545, rows=3, cols=5, r=24, length=260)
    fittings(d, rng, 360, 620, 1.1, 18)
    board(d, rng, (1070, 180, 1375, 440), cards=4, strings=False)
    rough_line(d, [(980, 375), (1070, 300)], ORANGE, width=4, rng=rng, alpha=120)


def scene_search(d, rng):
    factory_background(d, rng, 720)
    magnifier(d, rng, 760, 385, 180)
    for i, (x, y) in enumerate([(330, 260), (480, 560), (940, 220), (1125, 545), (1260, 340)]):
        rough_ellipse(d, (x - 36, y - 28, x + 36, y + 28), outline=GREEN, width=4, fill=rgba(PAPER, 125), rng=rng)
        rough_line(d, [(760, 385), (x, y)], ORANGE if i % 2 else GREEN_2, width=3, rng=rng, alpha=100)
    pipe_stack(d, rng, 980, 660, rows=2, cols=6, r=22, length=320)
    fittings(d, rng, 300, 640, .9, 12)


def scene_keywords(d, rng):
    rough_rect(d, (240, 220, 1320, 700), outline=GREEN, width=4, fill=rgba(PAPER, 90), rng=rng)
    for x in [330, 570, 810, 1050]:
        rough_rect(d, (x, 270, x + 150, 505), outline=LINE, width=3, fill=rgba(IVORY, 160), rng=rng)
        for y in range(320, 480, 42):
            rough_line(d, [(x + 25, y), (x + 125, y + rng.randint(-4, 4))], LINE, width=2, rng=rng, alpha=80)
    fittings(d, rng, 320, 555, .88, 14)
    pipe_stack(d, rng, 840, 575, rows=2, cols=5, r=24, length=290)
    coil(d, rng, 1120, 610, 105, 62, 5)
    magnifier(d, rng, 690, 490, 75)


def scene_social(d, rng):
    factory_background(d, rng, 720)
    laptop(d, rng, 250, 260, 430, 255)
    for x in [760, 925, 1090]:
        rough_rect(d, (x, 220, x + 130, 390), outline=GREEN, width=3, fill=rgba(PAPER, 135), rng=rng)
        rough_rect(d, (x + 18, 242, x + 112, 305), outline=LINE, width=2, fill=rgba(GREEN_2, 28), rng=rng)
        for y in [326, 350, 374]:
            rough_line(d, [(x + 20, y), (x + 110, y)], LINE, width=2, rng=rng, alpha=75)
    camera(d, rng, 1010, 520, .75)
    fittings(d, rng, 410, 650, .9, 14)
    rough_line(d, [(675, 365), (760, 290), (925, 310), (1090, 290)], ORANGE, width=4, rng=rng, alpha=120)


def scene_paid(d, rng):
    factory_background(d, rng, 720)
    board(d, rng, (260, 150, 890, 520), cards=5)
    for i in range(4):
        rough_rect(d, (980 + i * 70, 190 + i * 92, 1270 - i * 25, 250 + i * 92), outline=GREEN, width=3, fill=rgba(PAPER, 140), rng=rng)
    rough_line(d, [(590, 520), (980, 560), (1190, 615)], ORANGE, width=5, rng=rng, alpha=135)
    magnifier(d, rng, 405, 595, 70)
    fittings(d, rng, 970, 655, .78, 11)


def scene_brand(d, rng):
    factory_background(d, rng, 700)
    rough_poly(d, [(800, 170), (1090, 260), (1015, 535), (800, 660), (585, 535), (510, 260)], outline=GREEN, width=7, fill=rgba(PAPER, 80), rng=rng)
    rough_ellipse(d, (665, 280, 935, 550), outline=GREEN, width=7, fill=rgba(GREEN_2, 35), rng=rng)
    coil(d, rng, 400, 585, 120, 75, 5)
    pipe_stack(d, rng, 1010, 585, rows=3, cols=5, r=23, length=260)
    fittings(d, rng, 630, 610, 1.0, 16)
    for a in range(-70, 90, 35):
        rough_line(d, [(800, 415), (800 + math.cos(math.radians(a)) * 330, 415 + math.sin(math.radians(a)) * 190)], ORANGE, width=3, rng=rng, alpha=85)


def scene_products(d, rng):
    rough_rect(d, (210, 180, 1390, 720), outline=GREEN, width=4, fill=rgba(PAPER, 100), rng=rng)
    pipe_stack(d, rng, 860, 260, rows=3, cols=5, r=28, length=300)
    coil(d, rng, 1120, 585, 125, 80, 6)
    fittings(d, rng, 300, 330, 1.4, 25)
    for x in [360, 570, 780, 1010]:
        rough_line(d, [(x, 245), (x + 90, 145)], ORANGE, width=3, rng=rng, alpha=85)
        rough_rect(d, (x + 92, 112, x + 200, 160), outline=LINE, width=2, fill=rgba(IVORY, 150), rng=rng)


def scene_content(d, rng):
    factory_background(d, rng, 720)
    camera(d, rng, 290, 430, 1.25)
    coil(d, rng, 1050, 520, 155, 98, 6)
    rough_rect(d, (720, 220, 1180, 405), outline=GREEN, width=4, fill=rgba(PAPER, 120), rng=rng)
    for x in [750, 900, 1050]:
        rough_rect(d, (x, 248, x + 115, 365), outline=LINE, width=2, fill=rgba(GREEN_2, 24), rng=rng)
    person(d, rng, 675, 670, .95, "point")
    rough_line(d, [(565, 488), (900, 320)], ORANGE, width=4, rng=rng, alpha=100)


def scene_distribution(d, rng):
    factory_background(d, rng, 710)
    pipe_stack(d, rng, 280, 430, rows=5, cols=7, r=25, length=370)
    coil(d, rng, 1040, 420, 180, 115, 7)
    rough_rect(d, (985, 605, 1320, 735), outline=GREEN, width=4, fill=rgba(PAPER, 100), rng=rng)
    for x, y in [(1030, 635), (1110, 690), (1215, 645), (1280, 710)]:
        rough_ellipse(d, (x - 14, y - 14, x + 14, y + 14), outline=ORANGE, width=3, fill=rgba(ORANGE, 60), rng=rng)
    rough_line(d, [(1030, 635), (1110, 690), (1215, 645), (1280, 710)], ORANGE, width=4, rng=rng, alpha=115)
    fittings(d, rng, 580, 660, .9, 14)


def scene_projects(d, rng):
    rough_rect(d, (240, 190, 1260, 690), outline=GREEN, width=4, fill=rgba(PAPER, 110), rng=rng)
    for i in range(6):
        rough_line(d, [(310, 260 + i * 55), (850, 245 + i * 48)], LINE, width=2, rng=rng, alpha=80)
    rough_rect(d, (920, 240, 1195, 515), outline=GREEN, width=4, fill=rgba(IVORY, 130), rng=rng)
    for y in range(290, 480, 38):
        rough_line(d, [(950, y), (1165, y + rng.randint(-4, 4))], LINE, width=2, rng=rng, alpha=75)
    person(d, rng, 390, 740, 1.0)
    person(d, rng, 720, 735, 1.0, "point")
    pipe_stack(d, rng, 930, 650, rows=2, cols=5, r=22, length=245)
    fittings(d, rng, 565, 620, .8, 12)


def scene_crm(d, rng):
    factory_background(d, rng, 720)
    rough_rect(d, (250, 170, 1280, 625), outline=GREEN, width=4, fill=rgba(PAPER, 115), rng=rng)
    for i, x in enumerate([310, 505, 700, 895, 1090]):
        rough_rect(d, (x, 230, x + 145, 560), outline=LINE, width=2, fill=rgba(IVORY, 145), rng=rng)
        for y in range(270, 520, 70):
            rough_rect(d, (x + 20, y, x + 125, y + 38), outline=GREEN_2, width=2, fill=rgba(GREEN_2, 26), rng=rng)
        if i < 4:
            rough_line(d, [(x + 145, 380), (x + 195, 380)], ORANGE, width=4, rng=rng, alpha=120)
    fittings(d, rng, 290, 675, .75, 10)
    pipe_stack(d, rng, 930, 700, rows=1, cols=5, r=22, length=290)


def scene_roadmap(d, rng):
    rough_rect(d, (240, 185, 1290, 665), outline=GREEN, width=4, fill=rgba(PAPER, 100), rng=rng)
    for x in [360, 620, 880]:
        rough_rect(d, (x, 250, x + 185, 485), outline=LINE, width=3, fill=rgba(IVORY, 150), rng=rng)
        for y in range(300, 450, 42):
            rough_line(d, [(x + 30, y), (x + 155, y + rng.randint(-4, 4))], LINE, width=2, rng=rng, alpha=80)
        rough_ellipse(d, (x + 72, 515, x + 112, 555), outline=ORANGE, width=3, fill=rgba(ORANGE, 38), rng=rng)
    rough_line(d, [(545, 535), (620, 535), (805, 535), (880, 535)], ORANGE, width=5, rng=rng, alpha=110)
    for x in [340, 730, 1120]:
        person(d, rng, x, 735, .85, "point" if x == 730 else "stand")
    fittings(d, rng, 980, 620, .7, 9)


def scene_recommendation(d, rng):
    rough_rect(d, (250, 220, 1350, 670), outline=GREEN, width=5, fill=rgba(PAPER, 100), rng=rng)
    rough_ellipse(d, (690, 305, 930, 545), outline=ORANGE, width=8, fill=rgba(ORANGE, 22), rng=rng)
    rough_poly(d, [(745, 420), (820, 485), (910, 335)], outline=GREEN, width=8, rng=rng)
    for x in [385, 555, 1080, 1240]:
        person(d, rng, x, 720, .9)
    rough_rect(d, (520, 270, 650, 585), outline=LINE, width=3, fill=rgba(IVORY, 150), rng=rng)
    rough_rect(d, (990, 270, 1120, 585), outline=LINE, width=3, fill=rgba(IVORY, 150), rng=rng)
    pipe_stack(d, rng, 1040, 610, rows=2, cols=4, r=20, length=220)
    fittings(d, rng, 425, 615, .68, 8)


SCENES = {
    "hero": scene_hero,
    "executive_case": scene_executive_case,
    "dual_market": scene_dual_market,
    "digital_infra": scene_digital_infra,
    "search": scene_search,
    "keywords": scene_keywords,
    "social": scene_social,
    "paid": scene_paid,
    "brand": scene_brand,
    "products": scene_products,
    "content": scene_content,
    "distribution": scene_distribution,
    "projects": scene_projects,
    "crm": scene_crm,
    "roadmap": scene_roadmap,
    "recommendation": scene_recommendation,
}


def finish(img, d, rng):
    frame(d, rng)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay, "RGBA")
    od.rectangle((0, 0, W, H), outline=rgba(CHARCOAL, 25), width=22)
    for _ in range(80):
        x = rng.randint(80, W - 80)
        y = rng.randint(70, H - 70)
        od.ellipse((x, y, x + rng.randint(2, 8), y + rng.randint(2, 8)), fill=rgba(CHARCOAL, rng.randint(10, 24)))
    img.alpha_composite(overlay)
    return img.convert("RGB").filter(ImageFilter.UnsharpMask(radius=1.4, percent=120, threshold=2))


def render(name: str, scene: str, idx: int):
    img, d, rng = make_canvas(9300 + idx * 71)
    SCENES[scene](d, rng)
    img = finish(img, d, rng)
    out = OUT / name
    img.save(out, "WEBP", quality=92, method=6)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for i, (name, scene) in enumerate(ASSETS):
        out = render(name, scene, i)
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
