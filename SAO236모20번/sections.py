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

def describeMinimum(scene, texts):
    minimum = Tex("극소").to_edge(LEFT)
    colon = Tex(": ").next_to(minimum, RIGHT)
    gx = Tex("$g(x)$  ").next_to(colon, RIGHT)
    gxShapes = Tex("↘", "↗").next_to(gx, RIGHT*2).scale(1.2)
    gprimex = Tex("$g${{$'$}}$(x)$").next_to(gx, DOWN)
    gprimexSigns = Tex("$(-)$", "$(+)$").next_to(gprimex, RIGHT)
    scene.play(TransformFromCopy(texts[2].get_part_by_tex("극소"), minimum))
    scene.play(Write(colon), Write(gx), Write(gxShapes[0].set_color(RED)), Write(gxShapes[1].set_color(BLUE).shift(RIGHT*0.5)), lag_ratio=1)
    scene.play(TransformFromCopy(gx, gprimex))
    scene.play(Indicate(gprimex.get_part_by_tex("$'$"), scale_factor=2))
    scene.play(TransformFromCopy(gxShapes[0], gprimexSigns[0].set_color(RED)), TransformFromCopy(gxShapes[1], gprimexSigns[1].set_color(BLUE).shift(RIGHT*0.4)))
    arrow = Arrow(gprimexSigns[0].get_edge_center(RIGHT), gprimexSigns[1].get_edge_center(LEFT), buff=0.05)
    scene.play(Create(arrow))
    scene.play(FadeOut(Group(gx, gxShapes)), Group(gprimex, gprimexSigns, arrow).animate.move_to(Group(gx, gxShapes)).shift(RIGHT*0.1))
    return Group(gprimex, gprimexSigns, arrow)