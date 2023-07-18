from manim import *
from library.consts import *

TITLE = Text("", font=GOTHIC)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).to_corner(UL)