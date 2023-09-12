from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.7
TITLE = Text("23학년도 9월 20번", font=GOTHIC)
TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("상수 $k(k<0)$에 대하여 두 함수"),
    MathTex("f(x)=x^3+x^2-x, g(x) = 4|x|+k"),
    Tex("의 그래프가 만나는 점의 개수가 2일 때,"),
    Tex("두 함수의 그래프로 둘러싸인 부분의 넓이를 $S$라 하자."),
    Tex(r"$30\times S$의 값을 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)