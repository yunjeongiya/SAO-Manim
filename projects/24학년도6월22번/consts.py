from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.5
TITLE = Text("24학년도 6월 22번", font=GOTHIC)

CONDITION = VGroup(
    Tex("함수 $f(x)$에 대하여"),
    MathTex(r'''{{ \left\{ \dfrac{f( x_1 ) - f( x_2 )}{x_1 - x_2} \right\} }}
            \times {{ \left\{ \dfrac{f( x_2 ) - f( x_3 )}{x_2 - x_3} \right\} }}
            <0 '''),
    Tex(r"을 만족시키는 세 실수 $x_1, x_2, x_3$이 열린구간 {{$\left( k, k+\dfrac{3}{2} \right)$}}에"),
    Tex("존재한다.")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex(r"정수 $a (a \ne 0)$에 대하여 함수 $f(x)$를"),
    MathTex("f(x)=x^3 -2ax^2"),
    Tex("이라 하자. 다음 조건을 만족시키는 {{모든 정수 $k$값의 곱이}}"),
    Tex("{{$-12$}}{{가 되도록}} 하는 $a$에 대하여 $f'(10)$의 값을 구하시오. [4점]"),
    CONDITION.add(SurroundingRectangle(CONDITION, buff=0.2, color=WHITE, stroke_width=2))
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)

TEXTS[2].shift(RIGHT)