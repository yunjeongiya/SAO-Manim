from manim import *
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"
TEXT_SCALE = 0.6

GOTHIC = "NanumBarunGothic"
TITLE = Text("09학년도 수능 나형 25번", font=GOTHIC)

TRAILS = VGroup(
    *[VGroup(
        *[VDict({
            "UR": Arc(start_angle=PI/2, angle=-PI/2),
            "UL": Arc(start_angle=PI, angle=-PI/2),
            "DL": Arc(start_angle=PI, angle=PI/2),
            "DR": Arc(start_angle=-PI/2, angle=PI/2),
            "UP" : Dot().move_to(UP),
            "DOWN" : Dot().move_to(DOWN),
            "LEFT" : Dot().move_to(LEFT),
            "RIGHT" : Dot().move_to(RIGHT)
        }) for _ in range(4)]).arrange(RIGHT, buff=-DEFAULT_DOT_RADIUS*2)
    for _ in range(2)]
).arrange(DOWN, buff=-DEFAULT_DOT_RADIUS*2)

A = Tex("A 지점").next_to(TRAILS[1][0], LEFT)
B = Tex("B 지점").next_to(TRAILS[0][-1], RIGHT)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("{{직사각형 모양의 잔디밭에 산책로}}가 만들어져 있다. 이"),
    Tex("산책로는 그림과 같이 {{반지름의 길이가 같은 원 8개가 서로}}"),
    Tex("{{외접}}하고 있는 형태이다."),
    VGroup(TRAILS, A, B),
    Tex("{{A 지점에서 출발}}하여 산책로를 따라 {{최단 거리}}{{로 B 지점에}}"),
    Tex("{{도착}}하는 경우의 수를 구하시오. (단, 원 위에 표시된 점은 원과)"),
    Tex("직사각형 또는 원과 원의 접점을 나타낸다. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEXT_SCALE).to_corner(UL)