from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.7
TITLE = Text("17학년도 수능 가형 18번, 나형 29번", font=GOTHIC)

CONDITIONS = VGroup(
    Tex("(가) $f(10)>f(20)$"),
    Tex("(나) $f(4)<f(22)$")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
CONDITIONS.add(SurroundingRectangle(VGroup(CONDITIONS, Dot().next_to(CONDITIONS)), color=WHITE, buff=0.2, corner_radius=0.2, stroke_width=2))

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("확률변수 {{$X$}}는 평균이 {{$m$}}, 표준편차가 {{$5$}}인 정규분포를 따르고,"),
    Tex("확률변수 $X$의 확률밀도함수 $f(x)$가 다음 조건을 만족시킨다."),
    CONDITIONS,
    Tex("$m$이 자연수일 때,"),
    Tex("P$(17 \leq X \leq 18)=a$이다."),
    Tex("$1000a$의 값을 오른쪽 표준정규"),
    Tex("분포표를 이용하여 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)
TABLE = MathTable([["z", r"\rm P\it(0\leq Z \leq z)"],
                   ["0.6", "0.226"],
                   ["0.8", "0.288"],
                   ["1.0", "0.341"],
                   ["1.2", "0.385"],
                   ["1.4", "0.419"]],
                  include_outer_lines=True,
                  v_buff=0.5, h_buff=0.5,
                  line_config={"stroke_width":2}).scale(TEX_SCALE*0.9).next_to(CONDITIONS, RIGHT, aligned_edge=UP, buff=2.7)
TEXTS.add(TABLE)

M = 14