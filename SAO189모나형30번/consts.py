from manim import *

MINT = "#0CDAE0"
NEON_PURPLE = "#FF6AFF"

XSTART = -1/2
XEND = 5/2
YSTART = -1/4
YEND = 5/4

INITIAL_A = 1/2
INITIAL_B = 4/3

A = 2/3
B = 4/3
K = 4/3

TITLE = Tex("18학년도 9월 나형 30번")
TEXTS = VGroup(
    VGroup(TITLE, Underline(TITLE, buff=0.2, stroke_width=1)),
    Tex("두 함수 $f(x)$와 $g(x)$가"),
    VGroup(
        MathTex(r'''
        f(x) = \begin{cases} 
        0 &(x \leq 0) \\
        x &(x > 0)
        \end{cases} ,'''),
        MathTex(r'''
        g(x) = \begin{cases} 
        x(2-x) &(|x-1| \leq 1) \\
        0 &(|x-1| > 1)
        \end{cases}''')
    ).arrange(RIGHT, buff=0.5),
    Tex("이다. {{양의 실수 $k, a, b$}}{{$(a<b<2)$}}에 대하여, 함수 $h(x)$를"),
    MathTex(r"h(x)={{k}}\{f(x)-f(x-{{a}})-f(x-{{b}})+f(x-2)\}"),
    Tex(r"라 정의하자. 모든 실수 $x$에 대하여 {{$0\leq h(x)\leq g(x)$}}일 때,"),
    Tex(r"{{${\displaystyle\int_0^2}\{g(x)-h(x)\}dx$}}의 값이 {{최소가 되게 하는 $k, a, b$}}에 대하여"),
    Tex("{{$60(k+a+b)$}}의 값을 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.6).to_corner(UL)

FX = lambda x: x if x > 0 else 0
GX = lambda x: x*(2-x) if abs(x-1) <= 1 else 0