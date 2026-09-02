#!/usr/bin/env python3
"""Render the AISeng Tech brand mark and the full browser icon set.

    python3 _tools/make_logo.py --all             # every asset listed in ASSETS
    python3 _tools/make_logo.py --size 1024 --out /tmp/mark.png
    python3 _tools/make_logo.py --contact-sheet /tmp/sheet.png

Why this is a script and not just a folder of PNGs
--------------------------------------------------
A logo gets re-exported constantly, and every size wants a different drawing --
not the same drawing scaled. Redrawing from geometry is the only way to get
that; scaling a master PNG down is what produced the grey mush this set
replaces. The design is also readable and adjustable here, which it is not
inside a binary.

The design
----------
An uppercase A drawn as a three-node graph: two legs, a crossbar, and a
circular node at each vertex. It carries the initial of AISeng, and the
node-and-edge treatment reads as the agentic-AI work the site is about without
reaching for the usual neural-net swirl. Legs white so they hold contrast
against the navy ground; crossbar and nodes in the brand teal.

Optical sizing
--------------
The single most important thing here. A mark drawn for 512px does not work at
16px -- the strokes go translucent, the counter inside the A fills in, and the
nodes turn to grey smudges. So there are three drawings, not one, and the tier
is chosen by the target size:

  DISPLAY (>= 64px)   the full mark, nodes included
  MEDIUM  (32-48px)   thicker strokes, wider stance, nodes dropped
  SMALL   (<= 24px)   thicker again, widest stance, nodes dropped

The nodes are a display-only detail. Rendered at 32px they crowd the
letterform and read as noise rather than as nodes, so detail drops out as size
drops -- which is how the letter stays legible rather than staying "complete".
Each tier's numbers came from rendering candidates and inspecting them at 1:1,
not from scaling the tier above.

Two numbers carry most of the legibility:

  CROSSBAR_T -- how far down the legs the crossbar sits, as a fraction of leg
      length. At the 0.615 a type designer would reach for first, the
      triangular counter above the bar closes up and the glyph becomes a blob
      below roughly 32px. It rises to 0.700 in SMALL.

  half -- half the distance between the two feet. Widening the stance as the
      size drops is what keeps the counter open once the strokes thicken.

Below 16px the mark collapses into a caret whatever you do; 16px is the floor.

Rendered at a supersample factor chosen so the working canvas is always at
least 2048px, then downsampled with Lanczos. ImageDraw has no anti-aliasing of
its own, so drawing at final size leaves visibly stepped diagonals on the legs.

Transparency and corners
------------------------
Everything except the Apple icon is drawn with transparent rounded corners, so
the mark sits correctly on a light or dark host page and platform icon masks
have nothing to fight.

apple-touch-icon.png is the exception: opaque, square, full bleed. iOS applies
its own rounded mask, so baking corners in produces a visibly double-rounded
icon with dark slivers at the corners. The mark occupies the middle ~62% of
the square, which keeps it inside the safe area that mask leaves.
"""
import argparse
import math
import os
import struct

from PIL import Image, ImageDraw

# Ground: the same near-black navy as the site's dark UI.
NAVY = (15, 26, 38, 255)
WHITE = (255, 255, 255, 255)
# Brand teal. The theme's link colour is #0085a1, which is too dark to hold
# against NAVY; this is the same hue lifted to keep contrast at small sizes.
TEAL = (26, 188, 216, 255)

# One entry per optical tier. `nodes` is (apex_radius, base_radius) or None.
DISPLAY = dict(leg=0.082, bar=0.060, t=0.665, apex_y=0.252, half=0.278,
               radius=0.22, nodes=(0.058, 0.052))
MEDIUM = dict(leg=0.118, bar=0.088, t=0.690, apex_y=0.205, half=0.305,
              radius=0.19, nodes=None)
SMALL = dict(leg=0.140, bar=0.100, t=0.700, apex_y=0.190, half=0.320,
             radius=0.16, nodes=None)


def tier_for(size):
    if size >= 64:
        return DISPLAY
    if size >= 32:
        return MEDIUM
    return SMALL


def _round_capped_line(draw, start, end, width, colour):
    """A line with round ends. ImageDraw.line only makes square ones, which
    leaves the legs of the A looking clipped where they meet the nodes."""
    draw.line([start, end], fill=colour, width=width)
    radius = width / 2
    for x, y in (start, end):
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=colour)


def render(size, tier=None, opaque=False, square=False):
    """Draw the mark at `size` px.

    opaque -- fill the whole square with NAVY instead of leaving the area
              outside the rounded rectangle transparent.
    square -- no rounded corners at all. Used together with opaque for the
              Apple icon, which iOS masks itself.
    """
    spec = tier or tier_for(size)
    # Keep the working canvas at or above 2048px so every tier gets the same
    # edge quality, and so a 512px render lands on exactly 4x as before.
    ss = max(4, math.ceil(2048 / size))
    canvas = size * ss

    img = Image.new("RGBA", (canvas, canvas), NAVY if opaque else (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if not square:
        draw.rounded_rectangle([0, 0, canvas - 1, canvas - 1],
                               radius=int(canvas * spec["radius"]), fill=NAVY)

    point = lambda x, y: (x * canvas, y * canvas)
    base_y = 1.0 - spec["apex_y"] - 0.01 if spec is not DISPLAY else 0.778
    apex = point(0.5, spec["apex_y"])
    left = point(0.5 - spec["half"], base_y)
    right = point(0.5 + spec["half"], base_y)

    def along(target):
        return (apex[0] + spec["t"] * (target[0] - apex[0]),
                apex[1] + spec["t"] * (target[1] - apex[1]))

    _round_capped_line(draw, apex, left, int(canvas * spec["leg"]), WHITE)
    _round_capped_line(draw, apex, right, int(canvas * spec["leg"]), WHITE)
    _round_capped_line(draw, along(left), along(right), int(canvas * spec["bar"]), TEAL)

    if spec["nodes"]:
        apex_r, base_r = spec["nodes"]
        for centre, rad in ((apex, apex_r), (left, base_r), (right, base_r)):
            r = rad * canvas
            draw.ellipse([centre[0] - r, centre[1] - r,
                          centre[0] + r, centre[1] + r], fill=TEAL)

    return img.resize((size, size), Image.LANCZOS)


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
        from io import BytesIO
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


# (path, size, kwargs) -- what --all produces.
ASSETS = [
    ("image/logo.png", 512, {}),
    ("image/apple-touch-icon.png", 180, dict(opaque=True, square=True)),
    ("image/favicon-32x32.png", 32, {}),
    ("image/favicon-16x16.png", 16, {}),
]

ICO_SIZES = [16, 32, 48]


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


def contact_sheet(path):
    """Every asset size at 1:1 and magnified, on light and dark, for review."""
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
    parser = argparse.ArgumentParser(description="Render the AISeng Tech brand assets.")
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
