from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.6

TITLE = Text("20학년도 수능 가형 18번", font=GOTHIC)

OPTIONS = VGroup(
    VGroup(Tex("① 0.5328"), Tex("② 0.6247"), Tex("③ 0.7745")).arrange(buff=2),
    VGroup(Tex("④ 0.8185"), Tex("⑤ 0.9104")).arrange(buff=2)
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("확률변수 {{$X$}}는 정규분포 {{N($10,2^2$)}}, 확률변수 {{$Y$}}는"),
    Tex("정규분포 {{N($m,2^2$)}}를 따르고, 확률변수 $X$와 $Y$의"),
    Tex("확률밀도함수는 각각 $f(x)$와 $g(x)$이다."),
    MathTex("f(12) \leq g(20)"),
    Tex("을 만족시키는 $m$에 대하여"),
    Tex("P$(21\leq Y \leq 24)$의 최댓값을 오른쪽"),
    Tex("표준정규분포표를 이용하여 구한 것은? [4점]"),
    OPTIONS
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)
TEXTS[4].shift(RIGHT)
OPTIONS.shift(DOWN*0.3)

TABLE = MathTable([["z", r"\rm P\it(0\leq Z \leq z)"],
            ["0.5", "0.1915"],
            ["1.0", "0.3413"],
            ["1.5", "0.4332"],
            ["2.0", "0.4772"]],
            include_outer_lines=True,
            v_buff=0.5, h_buff=0.5,
            line_config={"stroke_width":2}).scale(TEX_SCALE*0.9).next_to(TEXTS)
TEXTS.add(TABLE)

XSTART = 18
XEND = 27