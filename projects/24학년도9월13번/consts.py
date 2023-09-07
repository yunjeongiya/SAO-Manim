from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6
TITLE = Text("24학년도 9월 평가원 13번", font=GOTHIC)
OPTIONS = VGroup(
    VGroup(Tex(r"① $\dfrac{3}{2} +3\sqrt2$"), Tex(r"② $3+3\sqrt2$"), Tex(r"③ $\dfrac{9}{2} +3\sqrt2$")).arrange(buff=2),
    VGroup(Tex(r"④ $6+3\sqrt2$"), Tex(r"⑤ $\dfrac{15}{2} +3\sqrt2$")).arrange(buff=2)
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("두 실수 $a, b$에 대하여 함수"),
    MathTex(r'''f(x)=\begin{cases}
      - \dfrac{1}{3} x^3 -ax^2 -bx  & ( x < 0 ) \\
        \dfrac{1}{3} x^3 +ax^2 -bx & (x \geq 0)
        \end{cases}'''),
    Tex(r"이 구간 {{$(-\infty,-1]$에서 감소}}하고 구간 {{$[-1,\infty)$에서 증가}}할 때,"),
    Tex("$a+b$의 최댓값을 $M$, 최솟값을 $m$이라 하자. $M-m$의 값은?"),
    Tex("[4점]"),
    OPTIONS
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)
TEXTS[-2].shift(RIGHT*7.5)

YSTART = -1
YEND = 2
XSTART = -2
XEND = 2