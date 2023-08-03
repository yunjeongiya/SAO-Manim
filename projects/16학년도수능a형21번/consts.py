from manim import *
#from library.consts import *
GOTHIC = "NanumBarunGothic"
TEX_SCALE = 0.6
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"
TITLE = Text("16학년도 수능 A형 21번", font=GOTHIC)

GA = Tex("(가) 함수 $|f(x)|$는 $x=-1$에서만 미분가능하지 않다.")
NA = VGroup(Tex("(나)"), 
            VGroup(Tex("방정식 $f(x)=0$은 닫힌 구간 $[3,5]$에서 적어도"),
            Tex("하나의 실근을 갖는다.")).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
            ).arrange(RIGHT, aligned_edge=UP, buff=0.3)
VGroup(GA, NA).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
BOX = SurroundingRectangle(VGroup(GA, NA, Dot().next_to(NA)),
                           color=WHITE, stroke_width=1, buff=0.5)

OPTIONS = VGroup(
    Tex("① $\dfrac{1}{15}$"),
    Tex("② $\dfrac{1}{10}$"),
    Tex("③ $\dfrac{2}{15}$"),
    Tex("④ $\dfrac{1}{6}$"),
    Tex("⑤ $\dfrac{1}{5}$")
).arrange(RIGHT, buff=1.5)
TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex(" 다음 조건을 만족시키는 모든 삼차함수 $f(x)$에 대하여"),
    Tex(r"$\dfrac{f'(0)}{f(0)}$의 최댓값을 $M$, 최솟값을 $m$이라 하자. $Mm$의 값은?"),
    Tex("[4점]"),
    VGroup(BOX, GA, NA),
    OPTIONS
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).scale(TEX_SCALE).to_corner(UL)
TEXTS[3].next_to(TEXTS[2], DOWN, buff=0.2, aligned_edge=RIGHT)

YSTART = -2
YEND = 2
XSTART = -2
XEND = 6