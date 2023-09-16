from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6
TITLE = Text("23학년도 수능 21번", font=GOTHIC)
TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("자연수 $n$에 대하여 함수 $f(x)$를"),
    VGroup(
        MathTex("f(x)=\Biggl\{"),
        VGroup(
            MathTex(r"{{|}} 3^{x+2} {{-n}}|"),
            MathTex(r"{{|}} \log_2 (x+4) {{-n}}|")
        ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3),
        VGroup(
            MathTex("(x<0)"), MathTex(r"(x\ge 0)")
        ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)
    ).arrange(buff=0.3),
    Tex("이라 하자. 실수 $t$에 대하여 $x$에 대한 방정식 {{$f(x)=t$}}의 서로"),
    Tex("다른 실근의 개수를 $g(t)$라 할 때, 함수 $g(t)$의 최댓값이 $4$가"),
    Tex("되도록 하는 모든 자연수 $n$의 값의 합을 구하시오. [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)
TEXTS[2][-1].shift(RIGHT*0.5)