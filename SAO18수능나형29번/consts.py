from manim import *

GOTHIC = "NanumBarunGothic"
TITLE = Text("18학년도 수능 나형 29번", font=GOTHIC)

Ga = Tex("(가) 함수 {{$f(x)$는 실수 전체의 집합에서 }}{{미분가능}}하다.")
Na = Tex(r"(나) 모든 실수 $x$에 대하여 {{$f(x) \geq g(x)$}}이다.")

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("두 실수 $a$와 $k$에 대하여 두 함수 $f(x)$와 $g(x)$는"),
    MathTex(r'''
        f(x) = \begin{cases} 
        0 &(x \leq a) \\
        {(x-1)}^2 (2x+1) &(x > a)
        \end{cases}, '''),
    MathTex(r'''
        g(x) = \begin{cases} 
        0 &(x \leq k) \\
        12(x-k) &(x > k)
        \end{cases}'''),
    Tex("이고, 다음 조건을 만족시킨다."),
    VGroup( Ga, Na.next_to(Ga, DOWN, aligned_edge=LEFT), SurroundingRectangle(VGroup(Ga, Na), buff=MED_SMALL_BUFF, color=WHITE, stroke_width=1)),
    Tex(r"$k$의 최솟값이 $\dfrac{q}{p}$일 때, $a+p+q$의 값을 구하시오."),
    Tex("(단, $p$와 $q$는 서로소인 자연수이다.) [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.6).to_corner(UL)

XSTART = -1
XEND = 2

YSTART = -3
YEND = 5

YLENRATIO = 0.5

CONTACTX = 2
CONTACTY = 5

Q = 19
P = 12
KMIN = Q/P

MINT = "#0CDAE0"