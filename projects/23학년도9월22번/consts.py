from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6
TITLE = Text("23학년도 9월 평가원 22번", font=GOTHIC)

TEXTS = Group(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("최고차항의 계수가 $1$이고 $x=3$에서 극대값 $8$을 갖는"),
    Tex("삼차함수 $f(x)$가 있다. 실수 $t$에 대하여 함수 $g(x)$를"),
    MathTex(r'''g(x)= \begin{cases}
                      f(x)  & (x\ge t) \\
                      -f(x)+2f(t) & (x<t)
                      \end{cases}'''),
    Tex("라 할 때, 방정식 $g(x)=0$의 서로 다른 실근의 개수를 $h(t)$라"),
    Tex("하자. 함수 $h(t)$가 $t=a$에서 불연속인 $a$의 값이 두 개일 때,"),
    Tex("$f(8)$의 값을 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).scale(TEX_SCALE).to_corner(UL)

XSTART = 1
XEND = 7
YSTART = -1
YEND = 12
G_XSTART = 1.645
G_XEND = 6.355