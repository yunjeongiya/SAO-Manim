from manim import *
#from library.consts import *
GOTHIC = "NanumBarunGothic"
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

TEX_SCALE = 0.6
STROKE_WIDTH = 2
RADIUS = 1.7

TITLE = Text("12학년도 6월 가형 15번", font=GOTHIC)

TRIANGLE = Triangle(color=WHITE, radius=RADIUS, stroke_width=STROKE_WIDTH)
CIRCLES = VGroup(
    Circle(color=WHITE, radius=RADIUS*1/2*3**(1/2), stroke_width=STROKE_WIDTH).move_to(TRIANGLE.get_vertices()[0]),
    Circle(color=WHITE, radius=RADIUS*1/2*3**(1/2), stroke_width=STROKE_WIDTH).move_to(TRIANGLE.get_vertices()[1]),
    Circle(color=WHITE, radius=RADIUS*1/2*3**(1/2), stroke_width=STROKE_WIDTH).move_to(TRIANGLE.get_vertices()[2])
)
PARTS = VGroup(
    Dot(fill_opacity=0),
    Difference(TRIANGLE, Union(*CIRCLES), stroke_width=STROKE_WIDTH),
    Intersection(TRIANGLE, CIRCLES[0], stroke_width=STROKE_WIDTH),
    Intersection(TRIANGLE, CIRCLES[1], stroke_width=STROKE_WIDTH),
    Intersection(TRIANGLE, CIRCLES[2], stroke_width=STROKE_WIDTH),
    Difference(CIRCLES[0], TRIANGLE, stroke_width=STROKE_WIDTH),
    Difference(CIRCLES[1], TRIANGLE, stroke_width=STROKE_WIDTH),
    Difference(CIRCLES[2], TRIANGLE, stroke_width=STROKE_WIDTH)
)

OPTIONS = VGroup(
    Tex("① 1260"),
    Tex("② 1680"),
    Tex("③ 2520"),
    Tex("④ 3760"),
    Tex("⑤ 5040")
).arrange(RIGHT, buff=1)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("그림과 같이 {{서로 접하고 크기가 같은 원 3개}}와 이 {{세 원의}}"),
    Tex("{{중심을 꼭짓점으로 하는 정삼각형}}이 있다. 원의 내부 또는"),
    Tex("{{정삼각형의 내부에 만들어지는 7개의 영역}}에 서로 다른 7가지"),
    Tex("색을 모두 사용하여 칠하려고 한다. 한 영역에 한 가지 색만을"),
    Tex("칠할 때, 색칠한 결과로 나올 수 있는 경우의 수는?"),
    Tex("(단, 회전하여 일치하는 것은 같은 것으로 본다.) [4점]"),
    PARTS,
    OPTIONS
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)

PARTS.shift(RIGHT)
TRIANGLE.scale(TEX_SCALE).move_to(PARTS)
CIRCLES.scale(TEX_SCALE).move_to(PARTS)