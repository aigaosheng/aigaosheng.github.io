#!/usr/bin/env python3
"""Render image/logo.png, the AISeng Tech brand mark.

    python3 _tools/make_logo.py                  # writes image/logo.png at 512px
    python3 _tools/make_logo.py --size 1024      # any square size
    python3 _tools/make_logo.py --out /tmp/x.png

Why this is a script and not just a PNG
---------------------------------------
A logo gets re-exported constantly -- a favicon, an apple-touch-icon, an
og:image overlay, a slide deck, a letterhead -- and each of those wants a
different pixel size. Redrawing from geometry at the target size gives clean
edges every time, where upscaling a 512px PNG does not. The design is also
readable and adjustable here in a way it is not inside a binary.

The design
----------
An uppercase A drawn as a three-node graph: two legs, a crossbar, and a circular
node at each vertex. It carries the initial of AISeng, and the node-and-edge
treatment reads as the agentic-AI work the site is actually about, without
resorting to the usual neural-net swirl.

Every number below was settled by rendering candidates and checking them at
24, 32, 40 and 60 pixels, because the mark's real job is `site.logo` -- the
publisher logo in the article JSON-LD -- plus whatever small-icon duty follows.
Two of those numbers matter more than the rest:

  CROSSBAR_T = 0.665
      How far down the legs the crossbar sits, as a fraction of leg length.
      This is the whole legibility of the letter. At 0.615 the triangular
      counter above the bar closes up and the glyph turns into a blob below
      about 32px; at 0.665 the counter stays open and it still reads as an A
      at 40px.

  Colour split
      Legs white, crossbar and nodes teal. An all-white bar renders a plainer,
      less distinctive mark -- correct, but generic. Putting the accent on the
      crossbar makes the letter specific to this site while leaving the two
      legs, which carry the letterform, at full contrast against the navy.

Drawn at SUPERSAMPLE times the target size and downsampled with Lanczos.
ImageDraw has no anti-aliasing of its own, so drawing at final size leaves
visibly stepped diagonals on the legs.

The rounded corners are cut with transparency rather than filled, so the mark
sits correctly on a light or a dark host page and platforms that apply their
own icon mask have nothing to fight.
"""
import argparse
import os

from PIL import Image, ImageDraw

SUPERSAMPLE = 4

# Ground: the same near-black navy the site's dark UI uses.
NAVY = (15, 26, 38, 255)
WHITE = (255, 255, 255, 255)
# Brand teal, lifted from the theme's link colour (#0085a1) to #1abcd8 so it
# holds contrast against NAVY -- the original is too dark on this ground.
TEAL = (26, 188, 216, 255)

CORNER_RADIUS = 0.22        # of tile width

APEX = (0.500, 0.252)       # vertex positions, as fractions of tile width
LEFT = (0.222, 0.778)
RIGHT = (0.778, 0.778)

LEG_WIDTH = 0.082
BAR_WIDTH = 0.060
CROSSBAR_T = 0.665

NODE_R_APEX = 0.058
NODE_R_BASE = 0.052


def _round_capped_line(draw, start, end, width, colour):
    """A line with round ends. ImageDraw.line only produces square ones, which
    leaves the legs of the A looking clipped where they meet the nodes."""
    draw.line([start, end], fill=colour, width=width)
    radius = width / 2
    for x, y in (start, end):
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=colour)


def render(size):
    canvas = size * SUPERSAMPLE
    img = Image.new("RGBA", (canvas, canvas), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle(
        [0, 0, canvas - 1, canvas - 1],
        radius=int(canvas * CORNER_RADIUS),
        fill=NAVY,
    )

    point = lambda p: (p[0] * canvas, p[1] * canvas)
    apex, left, right = point(APEX), point(LEFT), point(RIGHT)

    def along(target):
        return (apex[0] + CROSSBAR_T * (target[0] - apex[0]),
                apex[1] + CROSSBAR_T * (target[1] - apex[1]))

    _round_capped_line(draw, apex, left, int(canvas * LEG_WIDTH), WHITE)
    _round_capped_line(draw, apex, right, int(canvas * LEG_WIDTH), WHITE)
    _round_capped_line(draw, along(left), along(right), int(canvas * BAR_WIDTH), TEAL)

    for centre, radius in ((apex, NODE_R_APEX), (left, NODE_R_BASE), (right, NODE_R_BASE)):
        r = radius * canvas
        draw.ellipse([centre[0] - r, centre[1] - r, centre[0] + r, centre[1] + r], fill=TEAL)

    return img.resize((size, size), Image.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description="Render the AISeng Tech brand mark.")
    parser.add_argument("--size", type=int, default=512, help="square edge in pixels")
    parser.add_argument("--out", default=os.path.join("image", "logo.png"))
    args = parser.parse_args()

    render(args.size).save(args.out, "PNG", optimize=True)
    print(f"{args.out}  {args.size}x{args.size}  {os.path.getsize(args.out)} bytes")


if __name__ == "__main__":
    main()
