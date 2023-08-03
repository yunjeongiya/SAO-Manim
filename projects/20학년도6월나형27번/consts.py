from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6

TITLE = Text("20학년도 6월 나형 27번", font=GOTHIC)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("두 함수"),
    MathTex("f(x)=x^3 +3x^2 -k, g(x)=2x^2 +3x-10"),
    Tex("에 대하여 부등식"),
    MathTex("f(x) \geq 3g(x)"),
    Tex("가 닫힌 구간 [-1,4]에서 항상 성립하도록 하는 실수 $k$의"),
    Tex("최댓값을 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)

XSTART = -3
XEND = 5
LOCAL_MAX_XVAL = -1
LOCAL_MIN_XVAL = 3