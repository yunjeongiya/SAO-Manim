from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6
TITLE = Text("24학년도 6월 20번", font=GOTHIC)
CONDITIONS = VGroup(
    Tex(r"$x\ge 1$인 모든 실수 $x$에 대하여"),
    Tex(r"$g(x)\ge g(4)$이고 $|g(x)| \ge |g(3)|$이다.")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("최고차항의 계수가 1인 이차함수 $f(x)$에 대하여 함수"),
    MathTex(r"g(x)=\int_0^x f(t)dt"),
    Tex("가 다음 조건을 만족시킬 때, $f(9)$의 값을 구하시오. [4점]"),
    CONDITIONS.add(SurroundingRectangle(VGroup(CONDITIONS, Dot().next_to(CONDITIONS, buff=2.5)), color=WHITE, buff=0.3, stroke_width=1))
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).scale(TEX_SCALE).to_corner(UL)
TEXTS[2].shift(RIGHT)