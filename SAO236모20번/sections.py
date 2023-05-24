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
    fx = MathTex(r"f(x)=2x^2+\cdots").next_to(texts, DOWN*2).to_edge(LEFT)
    graph = Axes().plot(lambda x: 2*x**2, x_range = [-1, 1]).next_to(fx, RIGHT)
    
    box = SurroundingRectangle(texts[2].get_part_by_tex(r"$g(x)={\displaystyle\int_x^{x+1}}|f(t)|dt$"))
    ul2 = VGroup(Underline(texts[2].get_part_by_tex("$x=1$"), color=YELLOW),
                 Underline(texts[2].get_part_by_tex("과"), color=YELLOW),
                 Underline(texts[2].get_part_by_tex("$x=4$"), color=YELLOW))
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
    minimum = Text("극소", font="NanumBarunGothic").next_to(texts, DOWN*2).to_edge(LEFT)
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
    return VGroup(minimum, colon, gprimex, gprimexSigns, arrow)

def describeIntegral(scene, texts, minimumDescription):
    originGx = texts[2].get_part_by_tex(r"$g(x)={\displaystyle\int_x^{x+1}}|f(t)|dt$")
    box = SurroundingRectangle(originGx)
    gx = MathTex(r"g(x)={{{\int}}^{x+1}{{_x}}}{{|f(t)|}}dt").scale_to_fit_width(originGx.get_width()).move_to(originGx)
    gxDescription = Group(
        MathTex("|{{f(t)}}|").set_color(YELLOW),
        Text("를", font="NanumBarunGothic"),
        MathTex("x").set_color(RED),
        Text("부터", font="NanumBarunGothic"),
        MathTex("x+1").set_color(BLUE),
        Text("까지", font="NanumBarunGothic"),
        Text("적분", font="NanumBarunGothic").set_color(GREEN)
    ).arrange().next_to(gx, DOWN*2, aligned_edge=LEFT)
    
    scene.play(Create(box))
    scene.play(FadeOut(Group(box, texts, minimumDescription)), FadeIn(gx)) #gx만 남기고 사라지게
    scene.play(FadeToColor(gx.get_part_by_tex("|f(t)|"), YELLOW), 
               TransformFromCopy(gx.get_part_by_tex("|f(t)|"), gxDescription[0]))
    scene.play(Write(gxDescription[1]))
    scene.play(FadeToColor(gx.get_part_by_tex("_x"), RED), 
               TransformFromCopy(gx.get_part_by_tex("_x"), gxDescription[2]),
               FadeToColor(gx.get_part_by_tex("x+1"), BLUE), 
               TransformFromCopy(gx.get_part_by_tex("x+1"), gxDescription[4]))
    scene.play(Write(gxDescription[3]), Write(gxDescription[5]))
    scene.play(FadeToColor(Group(gx.get_part_by_tex("int"), gx.get_part_by_tex("dt")), GREEN), Write(gxDescription[6]))
    gxCopy = gx.get_part_by_tex("g(x)=").copy()
    scene.play(gxDescription.animate.set_color(WHITE).next_to(gx.get_part_by_tex("g(x)="), RIGHT), FadeOut(gx), FadeIn(gxCopy))
    return Group(gxCopy, gxDescription)

def graphAnalysis(scene, gxDescription, minimumDescription, texts):
    ax = Axes(
        x_range=[-2.5,2.5],
        y_range=[0,7.25],
        x_length=3,
        y_length=3,
        x_axis_config={
            "include_tip": True,
            "tip_width": 0.1,
            "tip_height": 0.15,
            "include_ticks": False
        },
        y_axis_config={
            "include_tip": False,
            "stroke_width": 0
        }
    ).next_to(gxDescription[1], DOWN*2, aligned_edge=LEFT)
    graph = ax.plot(lambda x: x**2+1, x_range = [-2.5,2.5])
    numbering = Text("①").scale(0.6).next_to(ax, LEFT).shift(UP*0.5)

    scene.play(Create(ax), Create(graph))
    x = ValueTracker(-2.3)
    label_x = always_redraw(lambda: MathTex("x").scale(0.5).next_to(ax.c2p(x.get_value()), DOWN*0.5))
    label_xPlus1 = always_redraw(lambda: MathTex("x+1").scale(0.5).next_to(ax.c2p(x.get_value()+1), DOWN*0.5))
    line_x = always_redraw(lambda: ax.get_vertical_line(ax.input_to_graph_point(x.get_value(),graph)))
    line_xPlus1 = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(x.get_value()+1, graph)))
    area = ax.get_area(graph, [x.get_value(), x.get_value()+1], color=YELLOW, opacity=0.5, stroke_width=0)
    
    scene.play(Create(line_x), Create(line_xPlus1), Write(label_x), Write(label_xPlus1))
    scene.play(FadeIn(area))
    
    ax2 = ax.copy().next_to(gxDescription[1], DOWN*2, aligned_edge=RIGHT)
    graph2 = ax2.plot(lambda x: x**2-1, x_range = [-2.5,2.5])
    numbering2 = Text("②").scale(0.6).next_to(ax2, LEFT).shift(UP*0.5)

    scene.play(Create(ax2), Create(graph2), Write(numbering), Write(numbering2))
    graph2abs = ax2.plot(lambda x: abs(x**2-1), x_range = [-2.5,2.5])
    scene.play(Indicate(gxDescription[1][0].get_parts_by_tex("|")))
    scene.play(Transform(graph2, graph2abs))
    #graph2 = graph2abs

    x2 = ValueTracker(-2.3)
    label_x2 = always_redraw(lambda: MathTex("x").scale(0.5).next_to(ax2.c2p(x2.get_value()), DOWN*0.5))
    label_x2Plus1 = always_redraw(lambda: MathTex("x+1").scale(0.5).next_to(ax2.c2p(x2.get_value()+1), DOWN*0.5))
    line_x2 = always_redraw(lambda: ax2.get_vertical_line(ax2.input_to_graph_point(x2.get_value(),graph2)))
    line_x2Plus1 = always_redraw(lambda: ax2.get_vertical_line(ax2.i2gp(x2.get_value()+1, graph2)))
    area2 = ax2.get_area(graph2, [x2.get_value(), x2.get_value()+1], color=YELLOW, opacity=0.5, stroke_width=0)
    scene.play(Create(line_x2), Create(line_x2Plus1), Write(label_x2), Write(label_x2Plus1))
    scene.play(FadeIn(area2))

    scene.play(Write(minimumDescription.next_to(gxDescription, UP, aligned_edge=LEFT)))
    scene.play(Transform(minimumDescription[2], Text("넓이의 순간변화율", font="NanumBarunGothic", color=YELLOW, t2c={"의":WHITE}).next_to(minimumDescription[1], RIGHT)),
               minimumDescription[3:].animate.shift(RIGHT*4))

    area_RED = always_redraw(lambda: ax.get_area(graph, [x.get_value(), x.get_value()+1], color=RED, opacity=0.5, stroke_width=0))
    scene.remove(area)
    scene.add(area_RED)
    scene.play(x.animate.set_value(-0.5))
    area_BLUE = always_redraw(lambda: ax.get_area(graph, [x.get_value(), x.get_value()+1], color=BLUE, opacity=0.5, stroke_width=0))
    scene.remove(area_RED)
    scene.add(area_BLUE)
    scene.play(x.animate.set_value(1.3))

    scene.play(FadeIn(texts.scale(0.7).to_corner(UL)), FadeOut(gxDescription), FadeOut(minimumDescription))
    box = SurroundingRectangle(texts[2].get_part_by_tex("$x=1$"), color=YELLOW)
    box2 = SurroundingRectangle(texts[2].get_part_by_tex("$x=4$"), color=YELLOW)
    scene.play(Create(box), Create(box2))

    scene.next_section(skip_animations=False)
    wrong = Line([0, 0, 0], [0.5, 0.5, 0], color=RED).move_to(numbering)
    minNum = Text("극소 1개", font="NanumBarunGothic").scale(0.6).next_to(ax, DOWN)
    minNum2 = Text("극소 2개?", font="NanumBarunGothic").scale(0.6).next_to(ax2, DOWN)
    scene.play(Write(wrong), Write(minNum))
    scene.play(Write(minNum2))