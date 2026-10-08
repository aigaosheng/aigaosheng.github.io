#!/usr/bin/env python3
"""Render the AI Seng Tech brand mark, the browser icon set and the brand kit.

    python3 _tools/make_logo.py --all             # site icons + brand kit
    python3 _tools/make_logo.py --size 1024 --out /tmp/mark.png
    python3 _tools/make_logo.py --contact-sheet /tmp/sheet.png

Needs rsvg-convert (brew install librsvg) and Pillow. The caption on the
"name" brand file is live text set in Avenir Next, so render it on a Mac or a
machine with that font installed.

Why this is a script and not just a folder of PNGs
--------------------------------------------------
A logo gets re-exported constantly, and every size wants a different drawing --
not the same drawing scaled. Redrawing from geometry is the only way to get
that; scaling a master PNG down produces grey mush at tab size. The design is
also readable and adjustable here, which it is not inside a binary.

The design
----------
An "AS" monogram in glass. A frosted white A wears a robot head at its apex --
helmet, dark visor, glowing eye, antenna -- and a blue glass S sits beside it.
A glowing orbit line runs from the A's crossbar, behind the S, out to a node.
Everything is lit from the top-left: each shape is extruded down-right for
depth, carries a bright rim on its lit edges, a darker refraction on its far
edges and a few specular streaks, over a soft drop shadow. The ground is
near-black with a blue glow in the top-right corner.

The S is not a font glyph. It is a ribbon swept along a Catmull-Rom centreline
(S_PTS) with a width that swells through the spine and tapers at both
terminals, so the shape owns its contrast and needs no font to render.

Optical sizing
--------------
A mark drawn for 512px does not work at 16px: the glass highlights, the robot's
face and the orbit line all turn to noise, and the thin right leg of the A
disappears. So there are two drawings, chosen by target size:

  DISPLAY (>= 64px)   the full glass mark
  SMALL   (<  64px)   flat, heavy A and S side by side, no robot, no effects

The SMALL drawing keeps the two colours that identify the mark -- white A,
blue S -- and drops everything else, which is how it stays legible rather than
staying "complete". Below 16px it collapses whatever you do; 16px is the floor.

Transparency and corners
------------------------
Site icons are clipped to a rounded square with transparent corners, so the
mark sits correctly on a light or dark host page and platform icon masks have
nothing to fight.

apple-touch-icon.png is the exception: opaque, square, full bleed. iOS applies
its own rounded mask, so baking corners in produces a visibly double-rounded
icon with dark slivers at the corners. The mark is drawn smaller there so it
stays inside the safe area that mask leaves.

The brand kit in img/logo/ is square and full bleed, which is what LinkedIn and
most profile uploaders expect.
"""
import argparse
import math
import os
import struct
import subprocess
from io import BytesIO

from PIL import Image, ImageDraw

# Ground of the mark. _config.yml's chrome-tab-theme-color matches it.
GROUND = "#03060F"


# --- geometry -----------------------------------------------------------------

def catmull(pts, n=40):
    """Sample a Catmull-Rom spline through `pts`, n samples per segment."""
    P = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i-1], P[i], P[i+1], P[i+2]
        for k in range(n):
            t = k / n
            t2, t3 = t*t, t*t*t
            out.append(tuple(0.5*((2*p1[j]) + (-p0[j]+p2[j])*t + (2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2
                                  + (-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3) for j in (0, 1)))
    out.append(pts[-1])
    return out


def _frame(c):
    """Arc-length fraction and unit normal at every sample of a polyline."""
    L = [0.0]
    for a, b in zip(c, c[1:]):
        L.append(L[-1] + math.dist(a, b))
    for i, p in enumerate(c):
        a, b = c[max(i-1, 0)], c[min(i+1, len(c)-1)]
        dx, dy = b[0]-a[0], b[1]-a[1]
        d = math.hypot(dx, dy) or 1
        yield L[i] / L[-1], p, (-dy/d, dx/d)


def _poly(left, right):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in left + right[::-1]) + ' Z'


def ribbon(pts, wfun):
    """Closed outline of a stroke along `pts` whose width at arc fraction s is wfun(s)."""
    left, right = [], []
    for s, p, (nx, ny) in _frame(catmull(pts)):
        w = wfun(s) / 2
        left.append((p[0]+nx*w, p[1]+ny*w))
        right.append((p[0]-nx*w, p[1]-ny*w))
    return _poly(left, right)


def streak(pts, wfun, s0, s1, off, maxw):
    """Tapered specular streak along a ribbon between arc fractions s0..s1,
    offset `off` (-1..1) across the ribbon's width."""
    left, right = [], []
    for s, p, (nx, ny) in _frame(catmull(pts)):
        if not s0 <= s <= s1:
            continue
        o = off * wfun(s) / 2
        h = maxw * math.sin(math.pi * (s - s0) / (s1 - s0)) / 2
        cx, cy = p[0] + nx*o, p[1] + ny*o
        left.append((cx + nx*h, cy + ny*h))
        right.append((cx - nx*h, cy - ny*h))
    return _poly(left, right)


# The S, on a 1000-unit canvas. Thin at the terminals, full through the spine.
S_PTS = [(820, 318), (745, 284), (650, 278), (560, 296), (502, 348), (500, 418), (565, 468),
         (680, 505), (790, 552), (832, 622), (800, 684), (700, 716), (590, 714), (505, 682)]
S_W = lambda s: 24 + 74*math.sin(math.pi*s)**0.55
S_D = ribbon(S_PTS, S_W)
S_CORE = ribbon(S_PTS, lambda s: 0.4*S_W(s))                  # glass inner light
S_SPEC = [streak(S_PTS, S_W, 0.04, 0.36, 0.55, 14),            # top arc + upper-left curve
          streak(S_PTS, S_W, 0.50, 0.66, 0.50, 10),            # down the spine
          streak(S_PTS, S_W, 0.70, 0.84, 0.45, 8)]             # lower bowl

# The A as one outline (legs + crossbar unioned, counter cut out). It has to be
# a single filled shape: the glass is translucent, so overlapping pieces would
# show their seams through it.
A_D = ("M355.3 337.7 L428 353.6 L500.4 592 L454.4 592 L445.4 562 L334.9 562 L275.8 680 L184.2 680 Z "
       "M403.6 424.4 L436.3 532 L349.9 532 Z")

# Orbit line: tapers from the A's crossbar out to the node at top-right.
O_D = ribbon([(345, 600), (470, 585), (620, 545), (760, 470), (872, 368)], lambda s: 16 - 10*s)

# Bounding centre of the mark (A foot to orbit node), used to centre it on a canvas.
MARK_CX, MARK_CY = 562, 492


# --- drawing ------------------------------------------------------------------

DEFS = f'''<defs>
  <radialGradient id="bgglow" cx="1000" cy="0" r="950" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#1446B8" stop-opacity="0.85"/><stop offset="0.55" stop-color="#0A2466" stop-opacity="0.35"/><stop offset="1" stop-color="{GROUND}" stop-opacity="0"/></radialGradient>
  <linearGradient id="glass" x1="480" y1="270" x2="850" y2="730" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#9AF0FF" stop-opacity="0.92"/><stop offset="0.35" stop-color="#46A8FF" stop-opacity="0.72"/>
    <stop offset="0.7" stop-color="#2F7BFF" stop-opacity="0.72"/><stop offset="1" stop-color="#1C4FE0" stop-opacity="0.9"/></linearGradient>
  <linearGradient id="aglass" x1="200" y1="680" x2="440" y2="340" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#BCD4FF" stop-opacity="0.86"/><stop offset="0.5" stop-color="#E6EEFF" stop-opacity="0.82"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.94"/></linearGradient>
  <linearGradient id="hglass" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.96"/><stop offset="0.55" stop-color="#E4ECFF" stop-opacity="0.84"/><stop offset="1" stop-color="#A9BFF0" stop-opacity="0.88"/></linearGradient>
  <linearGradient id="visor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A2850"/><stop offset="1" stop-color="#050A1C"/></linearGradient>
  <linearGradient id="og" x1="345" y1="600" x2="880" y2="360" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#1E5BFF"/><stop offset="1" stop-color="#6FE3FF"/></linearGradient>
  <radialGradient id="ball" cx="0.35" cy="0.35" r="0.7"><stop offset="0" stop-color="#E6FBFF"/><stop offset="0.5" stop-color="#5FD6FF"/><stop offset="1" stop-color="#1E7BFF"/></radialGradient>
  <radialGradient id="gball" cx="0.35" cy="0.35" r="0.75"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.5" stop-color="#C9DAFF"/><stop offset="1" stop-color="#6F86C9"/></radialGradient>
  <radialGradient id="eye" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#D9F8FF"/><stop offset="0.45" stop-color="#3FD0FF"/><stop offset="1" stop-color="#1468FF"/></radialGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="26"/></filter>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="b2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2"/></filter>
  <filter id="b4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="b6" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>
  <path id="Sp" d="{S_D}"/>
  <clipPath id="sclip"><path d="{S_D}"/></clipPath>
  <path id="Ap" fill-rule="evenodd" d="{A_D}"/>
  <clipPath id="aclip"><path clip-rule="evenodd" d="{A_D}"/></clipPath>
  <rect id="Hp" x="340" y="328" width="150" height="110" rx="54"/>
  <clipPath id="hclip"><rect x="340" y="328" width="150" height="110" rx="54"/></clipPath>
  <clipPath id="vclip"><rect x="356" y="358" width="132" height="50" rx="25"/></clipPath>
  <clipPath id="rounded"><rect width="1000" height="1000" rx="220"/></clipPath>
</defs>'''

GROUND_SVG = f'<rect width="1000" height="1000" fill="{GROUND}"/><rect width="1000" height="1000" fill="url(#bgglow)"/>'

SPARKLE = 'M0 -1 Q0.125 -0.125 1 0 Q0.125 0.125 0 1 Q-0.125 0.125 -1 0 Q-0.125 -0.125 0 -1 Z'


def _lerp(c1, c2, t):
    a = [int(c1[i:i+2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i+2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x + (y - x) * t):02X}' for x, y in zip(a, b))


def _extrude(ref, near, far, depth=16, dx=0.75, dy=1.0):
    """3D side: copies stepped down-right, darkening with depth (light from top-left)."""
    return ''.join(f'<use href="#{ref}" transform="translate({i*dx:.2f} {i*dy:.2f})" fill="{_lerp(near, far, i / depth)}"/>'
                   for i in range(depth, 0, -1))


def _glass_edges(ref, clip, dark_w, dark_shift, rim_w, rim_shift, dark_blur='b6'):
    """Refraction on the far edge, bright rim on the lit edge, hairline all round."""
    return (f'<g clip-path="url(#{clip})">'
            f'<use href="#{ref}" fill="none" stroke="#3B5BA8" stroke-width="{dark_w}" opacity="0.45" '
            f'transform="translate({-dark_shift} {-dark_shift - 1})" filter="url(#{dark_blur})"/>'
            f'<use href="#{ref}" fill="none" stroke="#FFFFFF" stroke-width="{rim_w}" opacity="0.9" '
            f'transform="translate({rim_shift} {rim_shift + 1})" filter="url(#b2)"/>'
            f'<use href="#{ref}" fill="none" stroke="#FFFFFF" stroke-width="2.5" opacity="0.8"/>')


SHADOW = ('<g opacity="0.8" filter="url(#shadow)" transform="translate(28 34)">'
          '<use href="#Sp" fill="#000"/><use href="#Ap" fill="#000"/></g>')

A_GLASS = (f'<g opacity="0.9">{_extrude("Ap", "#9DB7EE", "#2E3F74")}</g>'
           '<use href="#Ap" fill="url(#aglass)"/>'
           + _glass_edges('Ap', 'aclip', 26, 9, 10, 4) +
           '<line x1="216" y1="640" x2="356" y2="360" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0.95"/>'
           '<line x1="404" y1="400" x2="453" y2="560" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.7"/>'
           '<line x1="356" y1="538" x2="436" y2="538" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.85"/>'
           '</g>'
           f'<path transform="translate(262 590) scale(11)" d="{SPARKLE}" fill="#FFFFFF" filter="url(#glow)"/>')

ORBIT = (f'<path d="{O_D}" fill="url(#og)" filter="url(#glow)"/>'
         f'<path d="{O_D}" fill="#DFF8FF" opacity="0.5" transform="translate(0 -2)" filter="url(#b2)"/>'
         '<line x1="872" y1="368" x2="893" y2="350" stroke="#6FE3FF" stroke-width="6" stroke-linecap="round"/>'
         '<circle cx="896" cy="347" r="21" fill="url(#ball)" filter="url(#glow)"/>'
         '<circle cx="889" cy="340" r="6" fill="#FFFFFF" opacity="0.85"/>')

S_GLASS = (f'<path d="{S_D}" fill="#2B7BFF" opacity="0.40" filter="url(#soft)"/>'
           f'<g opacity="0.85">{_extrude("Sp", "#2F78F0", "#0A2470")}</g>'
           '<use href="#Sp" fill="url(#glass)"/>'
           '<g clip-path="url(#sclip)">'
           '<use href="#Sp" fill="none" stroke="#0A2A9A" stroke-width="30" opacity="0.55" transform="translate(-11 -12)" filter="url(#b6)"/>'
           f'<path d="{S_CORE}" fill="#BFF4FF" opacity="0.35" filter="url(#b6)"/>'
           '<use href="#Sp" fill="none" stroke="#E6FBFF" stroke-width="12" opacity="0.85" transform="translate(5 6)" filter="url(#b2)"/>'
           '<use href="#Sp" fill="none" stroke="#DFF9FF" stroke-width="3" opacity="0.7"/>'
           + ''.join(f'<path d="{d}" fill="#FFFFFF" opacity="{o}"/>' for d, o in zip(S_SPEC, (0.95, 0.6, 0.45))) +
           '</g>'
           f'<path transform="translate(560 300) scale(16)" d="{SPARKLE}" fill="#FFFFFF" filter="url(#glow)"/>')

HEAD = ('<g transform="rotate(-6 412 382)">'
        '<line x1="398" y1="334" x2="382" y2="300" stroke="#C9D1F2" stroke-width="7" stroke-linecap="round"/>'
        '<circle cx="383" cy="299" r="13" fill="#4A5C96" opacity="0.9"/>'
        '<circle cx="380" cy="295" r="13" fill="url(#gball)"/>'
        '<circle cx="376" cy="290" r="4" fill="#FFFFFF"/>'
        f'<g opacity="0.9">{_extrude("Hp", "#9DB7EE", "#2E3F74", depth=12)}</g>'
        '<use href="#Hp" fill="url(#hglass)"/>'
        + _glass_edges('Hp', 'hclip', 18, 6, 8, 3, dark_blur='b4') + '</g>'
        '<path d="M364 346 Q394 330 434 332" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0.9"/>'
        '<rect x="356" y="358" width="132" height="50" rx="25" fill="url(#visor)"/>'
        '<g clip-path="url(#vclip)">'
        '<polygon points="430,358 456,358 426,408 400,408" fill="#FFFFFF" opacity="0.14"/>'
        '<polygon points="462,358 472,358 442,408 432,408" fill="#FFFFFF" opacity="0.10"/></g>'
        '<path d="M374 366 Q420 358 474 368" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.45"/>'
        '<circle cx="384" cy="383" r="21" fill="#0A1430" stroke="#2C7CFF" stroke-width="3"/>'
        '<circle cx="384" cy="383" r="14" fill="url(#eye)" filter="url(#glow)"/>'
        '<circle cx="379" cy="378" r="4" fill="#FFFFFF" opacity="0.9"/>'
        '<rect x="420" y="377" width="52" height="12" rx="6" fill="#3FD0FF" filter="url(#glow)"/>'
        '</g>')

MARK = SHADOW + A_GLASS + ORBIT + S_GLASS + HEAD


def _caption_line(x1, x2, fade_left):
    stops = ('<stop offset="0" stop-color="#1E5BFF" stop-opacity="0.2"/><stop offset="1" stop-color="#4FC8FF"/>'
             if fade_left else
             '<stop offset="0" stop-color="#4FC8FF"/><stop offset="1" stop-color="#1E5BFF" stop-opacity="0.2"/>')
    gid = f'cap{x1}'
    return (f'<linearGradient id="{gid}" x1="{x1}" y1="0" x2="{x2}" y2="0" gradientUnits="userSpaceOnUse">{stops}</linearGradient>'
            f'<line x1="{x1}" y1="826" x2="{x2}" y2="826" stroke="url(#{gid})" stroke-width="5" stroke-linecap="round"/>')


CAPTIONS = {
    # Full company name. Live text in Avenir Next -- see the module docstring.
    'name': (_caption_line(120, 205, True) + _caption_line(795, 880, False)
             + '<text x="500" y="846" text-anchor="middle" font-family="Avenir Next, Helvetica Neue, Arial" '
               'font-weight="500" font-size="58" letter-spacing="14" fill="#FFFFFF">AI SENG TECH</text>'),
    # "AI" with a crossbar-less A, as in the original reference. Drawn, not set.
    'ai': (_caption_line(278, 422, True) + _caption_line(656, 800, False)
           + '<polyline points="458,860 489,792 520,860" fill="none" stroke="#FFFFFF" stroke-width="11"/>'
             '<line x1="575" y1="792" x2="575" y2="860" stroke="#FFFFFF" stroke-width="11"/>'),
}


def display_svg(scale=1.16, caption=None, frame='square'):
    """The full glass mark on its ground, 1000x1000 units.

    scale   -- size of the mark on the canvas; 1.16 fills a square edge to edge.
    caption -- None, 'name' or 'ai'. With a caption the mark is drawn at its
               native size and lifted to leave room underneath, and `scale` is
               ignored.
    frame   -- 'square' (opaque, full bleed) or 'rounded' (transparent corners).
    """
    if caption:
        body = f'<g transform="translate(0 -40)">{MARK}</g>' + CAPTIONS[caption]
    else:
        body = f'<g transform="translate(500 500) scale({scale}) translate({-MARK_CX} {-MARK_CY})">{MARK}</g>'
    content = GROUND_SVG + body
    if frame == 'rounded':
        content = f'<g clip-path="url(#rounded)">{content}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">{DEFS}{content}</svg>'


# SMALL tier: a heavy, flat A beside a heavy S. Both strokes are about 11% of
# the canvas, which is what keeps them at ~2px when the icon lands at 16px.
SMALL_S_D = ribbon([(x + 45, y + 22) for x, y in S_PTS], lambda s: 95 + 25*math.sin(math.pi*s))


def small_svg(frame='rounded'):
    content = (f'<rect width="1000" height="1000" fill="{GROUND}"/><rect width="1000" height="1000" fill="url(#bgglow)"/>'
               '<path d="M100 770 L290 270 L480 770" fill="none" stroke="#F2F5FF" stroke-width="112" stroke-linejoin="bevel"/>'
               '<line x1="180" y1="590" x2="400" y2="590" stroke="#F2F5FF" stroke-width="78"/>'
               f'<path d="{SMALL_S_D}" fill="#3D9BFF"/>')
    if frame == 'rounded':
        content = f'<g clip-path="url(#rounded)">{content}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">{DEFS}{content}</svg>'


def svg_for(size, frame='rounded'):
    """Pick the optical tier for a target size."""
    return display_svg(scale=1.05, frame=frame) if size >= 64 else small_svg(frame=frame)


def rasterise(svg, size):
    png = subprocess.run(['rsvg-convert', '-w', str(size), '-h', str(size)],
                         input=svg.encode(), capture_output=True, check=True).stdout
    return Image.open(BytesIO(png)).convert('RGBA')


def render(size, opaque=False):
    """The site icon at `size` px. opaque -- square, full bleed, mark shrunk into
    the iOS safe area (the Apple icon)."""
    if opaque:
        return rasterise(display_svg(scale=0.86, frame='square'), size)
    return rasterise(svg_for(size), size)


# --- outputs ------------------------------------------------------------------

def write_ico(path, images):
    """Write a multi-resolution .ico whose entries are each drawn separately.

    Pillow's ICO writer takes one image and a list of sizes, resizing that one
    image for every entry -- which is precisely the naive downscale this whole
    script exists to avoid. So the container is assembled here instead. It is a
    simple format: a 6-byte header, a 16-byte directory entry per image, then
    the payloads. Entries are stored as PNG, which every browser in use has
    supported for well over a decade.
    """
    payloads = []
    for img in images:
        buf = BytesIO()
        img.save(buf, "PNG", optimize=True)
        payloads.append(buf.getvalue())

    offset = 6 + 16 * len(images)
    header = struct.pack("<HHH", 0, 1, len(images))
    directory, body = b"", b""
    for img, data in zip(images, payloads):
        w, h = img.size
        directory += struct.pack(
            "<BBBBHHII",
            0 if w >= 256 else w,   # 0 means 256 in the ICO directory
            0 if h >= 256 else h,
            0,                      # palette size: 0 for a PNG entry
            0,                      # reserved
            1,                      # colour planes
            32,                     # bits per pixel
            len(data),
            offset,
        )
        body += data
        offset += len(data)

    with open(path, "wb") as fh:
        fh.write(header + directory + body)


# (path, size, kwargs) -- the site icons --all produces.
ASSETS = [
    ("image/logo.png", 512, {}),
    ("image/apple-touch-icon.png", 180, dict(opaque=True)),
    ("image/favicon-32x32.png", 32, {}),
    ("image/favicon-16x16.png", 16, {}),
]

ICO_SIZES = [16, 32, 48]

# (basename, svg) -- the brand kit in img/logo/, each as .svg plus 300 and 1024 px.
# 300px is LinkedIn's recommended page-logo size.
BRAND_DIR = "img/logo"
BRAND = [
    ("ai-seng-tech-logo", lambda: display_svg()),
    ("ai-seng-tech-logo-name", lambda: display_svg(caption='name')),
    ("ai-seng-tech-logo-ai", lambda: display_svg(caption='ai')),
]


def build_all():
    for path, size, kwargs in ASSETS:
        img = render(size, **kwargs)
        if kwargs.get("opaque"):
            img = img.convert("RGB")     # iOS wants no alpha channel at all
        img.save(path, "PNG", optimize=True)
        print(f"{path:34s} {size}x{size:<5d} {os.path.getsize(path):>7,d} bytes")

    write_ico("image/favicon.ico", [render(s) for s in ICO_SIZES])
    print(f"{'image/favicon.ico':34s} {'+'.join(map(str, ICO_SIZES)):11s} "
          f"{os.path.getsize('image/favicon.ico'):>7,d} bytes")

    os.makedirs(BRAND_DIR, exist_ok=True)
    for name, make in BRAND:
        svg = make()
        with open(os.path.join(BRAND_DIR, name + ".svg"), "w") as fh:
            fh.write(svg)
        for size in (300, 1024):
            path = os.path.join(BRAND_DIR, f"{name}-{size}.png")
            rasterise(svg, size).convert("RGB").save(path, "PNG", optimize=True)
            print(f"{path:34s} {size}x{size:<5d} {os.path.getsize(path):>7,d} bytes")


def contact_sheet(path):
    """Every icon size at 1:1 and magnified, on light and dark, for review."""
    sizes = [180, 64, 48, 32, 24, 16]
    zoom = 6
    pad = 18
    width = sum(min(s, 64) * zoom + pad for s in sizes) + pad
    row = 64 * zoom + 40
    sheet = Image.new("RGBA", (width, row * 2 + pad), (250, 250, 250, 255))
    ImageDraw.Draw(sheet).rectangle([0, row + pad, width, row * 2 + pad],
                                    fill=(22, 24, 27, 255))
    x = pad
    for s in sizes:
        img = render(s)
        shown = min(s, 64)
        mag = img.resize((shown * zoom, shown * zoom), Image.NEAREST)
        sheet.alpha_composite(mag, (x, pad))
        sheet.alpha_composite(img.resize((shown, shown), Image.LANCZOS),
                              (x, pad + 64 * zoom + 8))
        sheet.alpha_composite(mag, (x, row + pad * 2))
        sheet.alpha_composite(img.resize((shown, shown), Image.LANCZOS),
                              (x, row + pad * 2 + 64 * zoom + 8))
        x += shown * zoom + pad
    sheet.convert("RGB").save(path, "PNG")
    print("contact sheet ->", path)


def main():
    parser = argparse.ArgumentParser(description="Render the AI Seng Tech brand assets.")
    parser.add_argument("--all", action="store_true", help="write every asset")
    parser.add_argument("--size", type=int, default=512, help="square edge in pixels")
    parser.add_argument("--out", default=os.path.join("image", "logo.png"))
    parser.add_argument("--contact-sheet", metavar="PATH")
    args = parser.parse_args()

    if args.contact_sheet:
        contact_sheet(args.contact_sheet)
        return
    if args.all:
        build_all()
        return
    render(args.size).save(args.out, "PNG", optimize=True)
    print(f"{args.out}  {args.size}x{args.size}  {os.path.getsize(args.out):,d} bytes")


if __name__ == "__main__":
    main()
