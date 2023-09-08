from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.5
TITLE = Text("23학년도 9월 14번", font=GOTHIC)

TEXTS = Group(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("최고차항의 계수가 1이고 $f(0)=0, f(1)=0$인"),
    Tex("삼차함수 $f(x)$에 대하여 함수 $g(t)$를"),
    MathTex(r"g({{t}})=\int_{{t}}^{{ {t+1} }} f(x)dx {{-}} \int_0^1 {{|}}f(x){{|}}dx"),
    Tex("라 할 때, $<$보기$>$에서 옳은 것만을 있는 대로 고른 것은? [4점]"),
    ImageMobject("OPTIONS.png").scale(1.5)
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)