from manim import *
#from library.consts import *
#colors
MINT = "#0CDAE0"
VIOLET = "#FF6AFF"

#fonts
GOTHIC = "NanumBarunGothic"

TEX_SCALE = 0.8
TITLE = Text("18학년도 9월 나형 27번", font=GOTHIC)

TEXTS = VGroup(
    VGroup(TITLE.scale(0.8), Underline(TITLE)),
    Tex("대중교통을 이용하여 출근하는 어느 지역 직장인의 월 교통비는"),
    Tex("평균이 {{8}}이고 표준편차가 {{1.2}}인 정규분포를 따른다고 한다. 대중"),
    Tex("교통을 이용하여 출근하는 이 지역 직장인 중 임의추출한 $n$명의"),
    Tex(r"월 교통비의 표본평균을 $\overline{X}$라고 할 때,"),
    MathTex(r"\text{P}\left({{7.76}} \leq {{ \overline{X} }} \leq {{8.24}}\right) \geq 0.6826"),
    Tex("이 되기 위한 $n$의 최솟값을 오른쪽"),
    Tex("표준정규분포표를 이용하여 구하시오."),
    Tex("(단, 교통비의 단위는 만 원이다.) [4점]")
).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).to_corner(UL)

TABLE = MathTable([["z", r"\rm P\it(0\leq Z \leq z)"],
                   ["0.5", "0.1915"],
                   ["1.0", "0.3413"],
                   ["1.5", "0.4332"],
                   ["2.0", "0.4772"]],
                  include_outer_lines=True,
                  v_buff=0.5, h_buff=0.5,
                  line_config={"stroke_width":2}).scale(TEX_SCALE*0.9).next_to(TEXTS[4], RIGHT, aligned_edge=UP, buff=0.8)
TEXTS.add(TABLE)

N = 25