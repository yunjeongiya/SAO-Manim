from manim import *
from consts import *
from utils import *

def showProblem(scene):
    texts = Group(Group(TITLE, Underline(TITLE, buff=0.2, stroke_width=1)), TEXT1, TEXT2, TEXT3
                  ).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(UL)
    scene.add(texts)
    return texts

def describeProblem(scene, texts):
    ul = Underline(texts[1].get_part_by_tex(r"최고차항의 계수가 2인 이차함수 $f(x)$"), color = YELLOW)
    fx = MathTex(r"f(x)=2x^2+\cdots").to_edge(LEFT)
    graph = Axes().plot(lambda x: 2*x**2, x_range = [-1, 1]).next_to(fx, RIGHT)
    
    box = SurroundingRectangle(texts[2].get_part_by_tex(r"$g(x)={\int_x^{x+1}}|f(t)|dt$"))
    ul2 = Underline(texts[2].get_part_by_tex(r"$x=1$과 $x=4$"), color = YELLOW)
    box2 = SurroundingRectangle(texts[2].get_part_by_tex("극소"))

    scene.play(Create(ul))
    scene.play(Write(fx))
    scene.play(Create(graph))
    scene.play(FadeOut(ul), FadeOut(fx), FadeOut(graph))
    scene.play(Create(box))
    scene.play(Create(ul2))
    scene.play(Create(box2))
    scene.play(FadeOut(box), FadeOut(box2), FadeOut(ul2))