from manim import *
Tex.set_default(font_size=30)

TITLE = Tex("23학년도 6월 평가원 20번", tex_environment="flushleft")
TEXT = Tex(r"최고차항의 계수가 2인 이차함수 $f(x)$", r"에 대하여\\",
            "함수 ", r"$g(x)={\int_x^{x+1}}|f(t)|dt$", r"는 ", r"$x=1$과 $x=4$", "에서 ", "극소",r"이다.\\",
            r"$f(0)$의 값을 구하시오. [4점]", tex_environment="flushleft")