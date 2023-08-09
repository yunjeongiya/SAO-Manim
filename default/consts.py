from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.8
TITLE = Text("", font=GOTHIC)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)