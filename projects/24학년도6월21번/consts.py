from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6
TITLE = Text("24학년도 6월 21번", font=GOTHIC)

CONDITIONS = VGroup(
    Tex(r"$\tiny\bullet$ 명제 ㄱ이 참이면 $A=100$, 거짓이면 $A=0$이다."),
    Tex(r"$\tiny\bullet$ 명제 ㄴ이 참이면 $B=10$,  거짓이면 $B=0$이다."),
    Tex(r"$\tiny\bullet$ 명제 ㄷ이 참이면 $C=1$,   거짓이면 $C=0$이다."),
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
THESES = VGroup(
    Tex("$<$보기$>$"),
    Tex("ㄱ. $f(1)=1$이고 $f(2)=2$이다."),
    Tex("ㄴ. 실수 $t$의 값이 증가하면 $f(t)$의 값도 증가한다."),
    Tex(r"ㄷ. 모든 양의 실수 $t$에 대하여 $f(t) \geq t$이다.")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
THESES[0].shift(RIGHT*4.5)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex(r"실수 $t$에 대하여 두 곡선 {{$y=t- \log_2 x$}}와 {{$y=2^{x-t}$}}이 만나는"),
    Tex("점의 $x$좌표를 $f(t)$라 하자."),
    Tex("$<$보기$>$의 각 명제에 대하여 다음 규칙에 따라 $A, B, C$의"),
    Tex("값을 정할 때, $A+B+C$의 값을 구하시오."),
    Tex(r"(단, $A+B+C \ne 0$) [4점]"),
    CONDITIONS.add(SurroundingRectangle(CONDITIONS, color=WHITE, buff=0.2, stroke_width=2)),
    THESES.add(SurroundingRectangle(VGroup(THESES, Dot().next_to(THESES[2], buff=0.15)), color=WHITE, buff=0.2, stroke_width=2)) #명제들
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)