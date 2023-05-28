from manim import *
from consts import *
from utils import *

def showProblem(scene):
    texts = Group(Group(TITLE, Underline(TITLE, buff=0.2, stroke_width=1)), TEXT1, TEXT2, TEXT3
                  ).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(UL)
    scene.add(texts)
    return texts

def describeProblem(scene:Scene, texts):
    ul = Underline(texts[1][:-1], color = YELLOW)
    fx = MathTex(r"f(x)=2x^2+\cdots").next_to(texts, DOWN*2).to_edge(LEFT)
    graph = Axes().plot(lambda x: 2*x**2, x_range = [-1, 1]).next_to(fx, RIGHT)
    
    box = SurroundingRectangle(texts[2].get_part_by_tex(r"$g(x)={\displaystyle\int_x^{x+1}}|f(t)|dt$"))
    ul2 = Underline(VGroup(texts[2].get_part_by_tex("$x=1$"),
                           texts[2].get_part_by_tex("과"),
                           texts[2].get_part_by_tex("$x=4$")), color = YELLOW)
    box2 = SurroundingRectangle(texts[2].get_part_by_tex("극소"))

    scene.play(Create(ul))
    scene.play(Write(fx))
    scene.play(Create(graph))
    scene.play(FadeOut(ul), FadeOut(fx), FadeOut(graph))
    scene.play(Create(box))
    scene.play(Create(ul2))
    scene.play(Create(box2))
    scene.play(FadeOut(box), FadeOut(box2), FadeOut(ul2))

def describeMinimum(scene:Scene, texts):
    minimum = Tex("극소").next_to(texts, DOWN*2).to_edge(LEFT)
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

def describeIntegral(scene:Scene, texts, minimumDescription):
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

def graphAnalysis(scene:Scene, gxDescription, minimumDescription, texts):
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
    label = ax.get_x_axis_label("t", direction=RIGHT).scale(0.7)
    graph = ax.plot(lambda x: x**2+1, x_range = [-2.5,2.5])
    numbering = Text("①").scale(0.6).next_to(ax, LEFT).shift(UP*0.5)
    graphGroup = VGroup(ax, label, graph, numbering)
    scene.play(Create(graphGroup[:-1]))
    x = ValueTracker(-2.3)
    label_x = always_redraw(lambda: MathTex("x").scale(0.5).next_to(ax.c2p(x.get_value()), DOWN*0.7))
    label_xPlus1 = always_redraw(lambda: MathTex("x+1").scale(0.5).next_to(ax.c2p(x.get_value()+1), DOWN*0.5))
    line_x = always_redraw(lambda: ax.get_vertical_line(ax.input_to_graph_point(x.get_value(),graph)))
    line_xPlus1 = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(x.get_value()+1, graph)))
    area = ax.get_area(graph, [x.get_value(), x.get_value()+1], color=YELLOW, opacity=0.5, stroke_width=0)
    
    scene.play(Create(line_x), Create(line_xPlus1), Write(label_x), Write(label_xPlus1))
    scene.play(FadeIn(area))
    
    ax2 = ax.copy().next_to(gxDescription[1], DOWN*2, aligned_edge=RIGHT)
    label2 = ax2.get_x_axis_label("t", direction=RIGHT).scale(0.7)
    graph2 = ax2.plot(lambda x: x**2-1, x_range = [-2.5,2.5])
    numbering2 = Text("②").scale(0.6).next_to(ax2, LEFT).shift(UP*0.5)
    graph2Group = VGroup(ax2, label2, graph2, numbering2)

    scene.play(Create(graph2Group[:-1]), Write(numbering), Write(numbering2))
    graph2abs = ax2.plot(lambda x: abs(x**2-1), x_range = [-2.5,2.5])
    scene.play(Indicate(gxDescription[1][0].get_parts_by_tex("|")))
    scene.play(Transform(graph2, graph2abs))
    #graph2 = graph2abs

    x2 = ValueTracker(-2.3)
    label_x2 = always_redraw(lambda: MathTex("x").scale(0.5).next_to(ax2.c2p(x2.get_value()), DOWN*0.7))
    label_x2Plus1 = always_redraw(lambda: MathTex("x+1").scale(0.5).next_to(ax2.c2p(x2.get_value()+1), DOWN*0.5))
    line_x2 = always_redraw(lambda: ax2.get_vertical_line(ax2.input_to_graph_point(x2.get_value(),graph2)))
    line_x2Plus1 = always_redraw(lambda: ax2.get_vertical_line(ax2.i2gp(x2.get_value()+1, graph2)))
    area2 = ax2.get_area(graph2, [x2.get_value(), x2.get_value()+1], color=YELLOW, opacity=0.5, stroke_width=0)
    scene.play(Create(line_x2), Create(line_x2Plus1), Write(label_x2), Write(label_x2Plus1))
    scene.play(FadeIn(area2))

    scene.play(FadeIn(minimumDescription.next_to(gxDescription, UP, aligned_edge=LEFT), shift=UP)) #이미 있던 텍스트 다시 보여주는거니까 write가 아니라 fadein
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

    wrong = Line([0, 0, 0], [0.5, 0.5, 0], color=RED).move_to(numbering)
    minNum = Text("극소 1개", font="NanumBarunGothic").scale(0.6).next_to(ax, DOWN)
    minNum2 = Text("극소 2개?", font="NanumBarunGothic").scale(0.6).next_to(ax2, DOWN)
    scene.play(Write(wrong), Write(minNum))
    scene.play(Write(minNum2))

    return texts

def calculateGxIntegral(scene:Scene, texts):
    scene.clear()
    scene.add(texts)
    originGx = texts[2].get_part_by_tex(r"$g(x)={\displaystyle\int_x^{x+1}}|f(t)|dt$")
    #처음부터 부분 다 쪼개기 힘들면, 이런식으로 원본은 쪼개놓지 말고, 각각 섹션별로 '지금 필요한 대로 쪼갠 버전'으로 대체하기
    gx = MathTex((r"g(x)={\displaystyle\int_x^{x+1}}{{|f(t)|}}dt")).scale_to_fit_width(originGx.width).move_to(originGx)
    ft = MathTex("{{|f(t)|}}=p(t)").next_to(texts, DOWN*1.5, aligned_edge=LEFT)
    scene.play(TransformFromCopy(gx.get_part_by_tex("|f(t)|"), ft.get_part_by_tex("|f(t)|")))
    scene.play(Write(ft.get_part_by_tex("p(t)")))
    newGx = MathTex((r"g(x){{=}}{\displaystyle\int{{_x}}^{x+1}{{p(t)}}dt")).next_to(ft, DOWN*1.5, aligned_edge=LEFT)
    scene.play(FadeIn(gx.get_part_by_tex("|f(t)|").set_color(YELLOW)), TransformFromCopy(gx.get_part_by_tex("|f(t)|"), newGx.get_part_by_tex("p(t)").set_color(YELLOW)))
    scene.play(FadeIn(newGx[:5]), FadeIn(newGx[6:]))
    newGx2 = MathTex(r"{{=}}[{{P(t)}}]{{_x}}^{x+1}").next_to(newGx.get_part_by_tex("="), DOWN*2.5, aligned_edge=LEFT)
    scene.play(FadeToColor(newGx, WHITE), FadeToColor(gx.get_part_by_tex("|f(t)|"), WHITE), 
               Write(newGx2.get_part_by_tex("=")), TransformFromCopy(newGx.get_part_by_tex("p(t)"), newGx2.get_part_by_tex("P(t)")))
    scene.play(FadeIn(newGx2.get_part_by_tex("[")), FadeIn(newGx2.get_part_by_tex("]")))
    scene.play(TransformFromCopy(newGx.get_part_by_tex("_x"), newGx2.get_part_by_tex("_x")), TransformFromCopy(newGx.get_part_by_tex("x+1"), newGx2.get_part_by_tex("x+1")))
    newGx3 = Group(
        MathTex("="),
        MathTex("P({{t}})"),
        MathTex("-P({{t}})")
    ).arrange(RIGHT).next_to(newGx2, DOWN*1.5, aligned_edge=LEFT)
    Pt = newGx3[1].copy().move_to(newGx2.get_part_by_tex("P(t)"))
    scene.play(Write(newGx3[0]), TransformFromCopy(Pt, newGx3[1]))
    PxPlus1 = MathTex("P{{'}}({{x+1}})").move_to(newGx3[1], aligned_edge=LEFT)
    PxPlus1.get_part_by_tex("'").set_color(BLACK)
    PxPlus1.get_part_by_tex("x+1").set_color(BLACK)
    scene.play(TransformMatchingTex(newGx3[1], PxPlus1),
               TransformFromCopy(newGx2.get_part_by_tex("x+1"), PxPlus1.get_part_by_tex("x+1").set_color(WHITE).set_z_index(1)))

    scene.play(TransformFromCopy(Pt, newGx3[2].next_to(PxPlus1, RIGHT)))
    Px = MathTex("{{-}}P{{'}}({{x}})").next_to(PxPlus1, RIGHT)
    Px.get_part_by_tex("'").set_color(BLACK)
    Px.get_part_by_tex("x").set_color(BLACK)
    scene.play(TransformMatchingTex(newGx3[2], Px),
               TransformFromCopy(newGx2.get_part_by_tex("_x"), Px.get_part_by_tex("x").set_color(WHITE).set_z_index(1)))
    scene.play(FadeOut(newGx[2:]), FadeOut(newGx2), FadeOut(newGx3[0]), VGroup(PxPlus1, Px).animate.move_to(newGx[2:], aligned_edge=LEFT))

    return ft, VGroup(newGx[:2], PxPlus1, Px)

def specifyMinimum(scene:Scene, texts, gx, minimumDescription):
    prime = MathTex("g{{'}}").move_to(gx, aligned_edge=LEFT)
    scene.play(FadeIn(prime[1].set_color(YELLOW)))
    scene.play(FadeToColor(gx[1].get_part_by_tex("'"),YELLOW), FadeToColor(gx[2].get_part_by_tex("'"), YELLOW))
    pXplus1 = MathTex("{{p}}({{x+1}})").move_to(gx[1:], aligned_edge=LEFT)
    pX = MathTex("-{{p}}({{x}})").next_to(pXplus1, RIGHT)
    scene.play(TransformMatchingTex(gx[1:], VGroup(pXplus1, pX)))
    box = SurroundingRectangle(texts[2].get_part_by_tex("극소"))
    gprimex = MathTex("g'(x)").next_to(box, DOWN*3)
    gprimexSigns = minimumDescription[3].next_to(gprimex, RIGHT)
    arrow = Arrow(gprimexSigns[0].get_edge_center(RIGHT), gprimexSigns[1].get_edge_center(LEFT), buff=0.05)
    boxArrow = Arrow(box.get_edge_center(DOWN), gprimex.get_edge_center(UP), buff=0, color=YELLOW)
    scene.play(AnimationGroup(Create(box), Create(boxArrow), AnimationGroup(Write(gprimex), Write(gprimexSigns), Create(arrow)), lag_ratio=0.7))
    under0 = MathTex("{{<}}0").next_to(pX, RIGHT).set_color(RED)
    pXplus1_2 = pXplus1.copy().next_to(pXplus1, DOWN*2)
    pX_2 = pX.copy().next_to(pXplus1_2, RIGHT)
    over0 = MathTex("{{>}}0").next_to(pX_2, RIGHT).set_color(BLUE)
    arrow2 = Arrow(under0[0].get_edge_center(DOWN), over0[0].get_edge_center(UP), buff=0.1)
    scene.play(TransformFromCopy(gprimexSigns[0], under0))
    scene.play(Create(arrow2), TransformFromCopy(pXplus1, pXplus1_2), TransformFromCopy(pX, pX_2))
    scene.play(TransformFromCopy(gprimexSigns[1], over0))

    scene.play(FadeOut(VGroup(under0.get_part_by_tex("0"), over0.get_part_by_tex("0"),
                              box, boxArrow, gprimex, gprimexSigns, arrow, prime, gx[0]),
                              pX.get_part_by_tex("-"), pX_2.get_part_by_tex("-")),
                pXplus1.animate.next_to(under0, LEFT), pX[1:].animate.next_to(under0[0], RIGHT),
                pXplus1_2.animate.next_to(over0, LEFT), pX_2[1:].animate.next_to(over0[0], RIGHT))
    
    return VGroup(pXplus1, pX[1:], pXplus1_2, pX_2[1:], under0[0], over0[0], arrow2)

def findMinimum(scene:Scene, texts, targetSituation):
    ax = Axes(
        x_range=[0,6],
        y_range=[0,15],
        x_length=5,
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
    )
    axLabel = ax.get_x_axis_label("t", direction=RIGHT).scale(0.7)
    func = lambda x: abs(2*(x-3)**2-5)
    graph = ax.plot(func, x_range = [0,6])
    graphLabel = MathTex("y={{p}}({{t}})").scale(0.7).next_to(graph, UR).shift(LEFT*0.5)
    graphGroup = VGroup(ax, axLabel, graph, graphLabel).to_edge(RIGHT)

    scene.play(targetSituation.animate.set_color(WHITE).to_edge(LEFT))
    scene.play(FadeIn(graphGroup))

    x = ValueTracker(0.1)
    
    label_x = MathTex("x").scale(0.5).next_to(ax.c2p(x.get_value()), DOWN*0.7).add_updater(lambda m: m.next_to(ax.c2p(x.get_value()), DOWN*0.7))
    label_xPlus1 = MathTex("x+1").scale(0.5).next_to(ax.c2p(x.get_value()+1), DOWN*0.5).add_updater(lambda m: m.next_to(ax.c2p(x.get_value()+1), DOWN*0.5))

    line_x_white = always_redraw(lambda: ax.get_vertical_line(ax.input_to_graph_point(x.get_value(),graph)).set_color(WHITE))
    line_xPlus1_white = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(x.get_value()+1, graph)).set_color(WHITE))
    
    line_x = always_redraw(lambda: ax.get_vertical_line(ax.input_to_graph_point(x.get_value(),graph)).set_color(BLUE))
    line_xPlus1 = always_redraw(lambda: ax.get_vertical_line(ax.i2gp(x.get_value()+1, graph)).set_color(YELLOW))

    scene.play(Create(line_x_white), Create(line_xPlus1_white), Create(label_x), Create(label_xPlus1))
    scene.play(FadeToColor(label_xPlus1, YELLOW), FadeToColor(line_xPlus1_white, YELLOW),
               targetSituation[0].animate.set_color(YELLOW), targetSituation[2].animate.set_color(YELLOW))
    scene.remove(line_xPlus1_white)
    scene.add(line_xPlus1)

    scene.play(FadeToColor(label_x, BLUE), FadeToColor(line_x_white, BLUE),
               targetSituation[1].animate.set_color(BLUE), targetSituation[3].animate.set_color(BLUE))
    scene.remove(line_x_white)
    scene.add(line_x)

    scene.play(x.animate(rate_func=linear).set_value(1))
    minLine = Line(ax.c2p(0, func(x.get_value())), ax.c2p(6, func(x.get_value())), stroke_width=3)
    scene.play(Create(minLine))

    a = MathTex("a").scale(0.5).next_to(label_x, DOWN)
    aPointer = Arrow(ax.i2gp(x.get_value(), graph), a.get_edge_center(UP), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.1)
    aPlus1 = MathTex("{{a}}+1").scale(0.5).next_to(label_xPlus1, DOWN)
    aPlus1Pointer = Arrow(ax.i2gp(x.get_value()+1, graph), aPlus1.get_edge_center(UP), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.1)
    scene.play(Create(a.shift(DOWN*0.05)), Create(aPointer))
    scene.play(Create(aPlus1), Create(aPlus1Pointer))

    scene.play(x.animate(rate_func=linear).set_value(2.5))
    maxLine = Line(ax.c2p(0, func(x.get_value())), ax.c2p(6, func(x.get_value())), stroke_width=3)
    scene.play(Create(maxLine))
    arrow = targetSituation[-1]
    scene.play(Transform(arrow, arrow.copy().rotate(PI)))
    maxTex = Text("극대", font="NanumBarunGothic").scale(0.5).next_to(ax.i2gp(3, graph), UP)
    scene.play(Indicate(arrow), Write(maxTex))

    scene.play(Transform(arrow, arrow.copy().rotate(PI)), FadeOut(maxTex), FadeOut(maxLine))
    scene.play(x.animate(rate_func=linear).set_value(4))
    b = MathTex("b").scale(0.5).next_to(label_x, DOWN)
    bPointer = Arrow(ax.i2gp(x.get_value(), graph), b.get_edge_center(UP), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.1)
    bPlus1 = MathTex("{{b}}+1").scale(0.5).next_to(label_xPlus1, DOWN)
    bPlus1Pointer = Arrow(ax.i2gp(x.get_value()+1, graph), bPlus1.get_edge_center(UP), stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.1)
    scene.play(Create(b.shift(DOWN*0.05)), Create(bPointer))
    scene.play(Create(bPlus1), Create(bPlus1Pointer))

    aCircle = Circle(radius=0.2, color=YELLOW).move_to(a)
    bCircle = Circle(radius=0.2, color=BLUE).move_to(b)
    scene.play(Create(aCircle), Create(bCircle),
               FadeOut(Group(line_x, line_xPlus1, label_x, label_xPlus1, targetSituation)))
    box1 = SurroundingRectangle(texts[2].get_part_by_tex("x=1"), buff=0.1, color=YELLOW)
    box2 = SurroundingRectangle(texts[2].get_part_by_tex("x=4"), buff=0.1, color=BLUE)
    scene.play(Create(box1), Create(box2))
    aVal = MathTex("1").scale(0.5).move_to(a)
    aPlus1Val = MathTex("{{1}}+1").scale(0.5).move_to(aPlus1)
    bVal = MathTex("4").scale(0.5).move_to(b)
    bPlus1Val = MathTex("{{4}}+1").scale(0.5).move_to(bPlus1)
    scene.play(FadeOut(a), FadeOut(b), FadeOut(aPlus1[0]), FadeOut(bPlus1[0]),
               TransformFromCopy(texts[2].get_part_by_tex("x=1")[-1], aVal), TransformFromCopy(texts[2].get_part_by_tex("x=4")[-1], bVal),
               TransformFromCopy(texts[2].get_part_by_tex("x=1")[-1], aPlus1Val[0]), TransformFromCopy(texts[2].get_part_by_tex("x=4")[-1], bPlus1Val[0]))
    scene.play(FadeOut(Group(aCircle, bCircle, box1, box2, aPointer, bPointer, aPlus1Pointer, bPlus1Pointer, aPlus1[1:], bPlus1[1:])),
               Transform(aPlus1Val, MathTex("2").scale(0.5).move_to(aPlus1)), Transform(bPlus1Val, MathTex("5").scale(0.5).move_to(bPlus1)))
    verticalLines = VGroup(ax.get_vertical_line(ax.i2gp(1, graph)),
                           ax.get_vertical_line(ax.i2gp(2, graph)),
                           ax.get_vertical_line(ax.i2gp(4, graph)),
                           ax.get_vertical_line(ax.i2gp(5, graph)))
    scene.play(aVal.animate.next_to(ax.c2p(1), DOWN*0.5), aPlus1Val.animate.next_to(ax.c2p(2), DOWN*0.5),
               bVal.animate.next_to(ax.c2p(4), DOWN*0.5), bPlus1Val.animate.next_to(ax.c2p(5), DOWN*0.5),
               Create(verticalLines[0]), Create(verticalLines[1]), Create(verticalLines[2]), Create(verticalLines[3]))
    return graphGroup, minLine, verticalLines, VGroup(aVal, aPlus1Val, bVal, bPlus1Val)

def findFx(scene:Scene, texts, ft, graphGroup, minLine, verticalLines, vals):
    
    #TODO graphGroup -> VMap 으로 바꾸기
    ax = graphGroup[0]
    axLabel = graphGroup[1]
    abs_graph = graphGroup[2]
    graphLabel_old = graphGroup[3]

    lineOfSymmetry = DashedLine(ax.c2p(3, 15), ax.c2p(3, -7), stroke_width=2)
    val3 = MathTex("3").scale(0.5).next_to(ax.c2p(3, 0), DOWN*0.5).shift(LEFT*0.1)
    vals += val3
    scene.play(Create(lineOfSymmetry), Write(val3))

    #ft = MathTex("{{|f(t)|}}=p(t)").next_to(texts, DOWN*1.5, aligned_edge=LEFT)
    ft_dividedByT = MathTex("{{|}}f({{t}}){{|}}{{=}}p({{t}})").move_to(ft).set_color_by_tex("x", YELLOW)
    fx_dividedByX = MathTex("{{|}}f({{x}}){{|}}{{=}}p({{x}})").move_to(ft).set_color_by_tex("x", YELLOW)
    fx_forTransform = MathTex("f(x)").move_to(fx_dividedByX[1], aligned_edge=LEFT)
    fx = MathTex("f(x){{=}}(x-3)^2{{+}}k").next_to(ft, DOWN*1.5, aligned_edge=LEFT).shift(RIGHT*0.1)

    graphLabel = MathTex("y={{p}}({{x}})").set_color_by_tex("x", YELLOW).scale(0.7).move_to(graphLabel_old)
    scene.add(ft_dividedByT)
    scene.play(Transform(axLabel, MathTex("x").scale(0.7).set_color(YELLOW).move_to(axLabel)),
               TransformMatchingTex(graphLabel_old, graphLabel),
               FadeOut(ft, run_time=0.1),
               TransformMatchingTex(ft_dividedByT, fx_dividedByX))
    graphLabel_new = MathTex("y={{f}}({{x}})").scale(0.7).move_to(graphLabel)
    func = lambda x: 2*(x-3)**2-5
    graph = ax.plot(func, x_range = [0,6])
    minLine2 = Line(ax.c2p(0, func(2)), ax.c2p(6, func(4)), stroke_width=3)
    scene.play(TransformMatchingTex(graphLabel, graphLabel_new),
               FadeToColor(fx_dividedByX, WHITE), FadeToColor(axLabel, WHITE),
               TransformFromCopy(fx_forTransform.set_color(WHITE), fx[:2]),
               Transform(abs_graph, graph),
               TransformFromCopy(minLine, minLine2),
               Transform(verticalLines[1], ax.get_vertical_line(ax.i2gp(2, graph))),
               Transform(verticalLines[2], ax.get_vertical_line(ax.i2gp(4, graph))))
    graphGroup -= graphLabel_old
    graphGroup += graphLabel_new

    scene.play(FadeToColor(lineOfSymmetry, YELLOW), FadeToColor(val3, YELLOW))
    scene.play(Write(fx.get_part_by_tex("(x-3)^2").set_color(YELLOW)))
    scene.play(Write(fx.get_part_by_tex("+").set_color(BLUE)), Write(fx.get_part_by_tex("k").set_color(BLUE)))
    fx2 = MathTex("f(x){{=}}{{2}}(x-3)^2{{+}}k").move_to(fx, aligned_edge=LEFT)
    fx2.get_part_by_tex("2").set_color(BLACK)
    ul = Underline(VGroup(texts[1].get_part_by_tex("최고차항의 계수가"), texts[1].get_part_by_tex("2")), color=YELLOW)
    fx2copy = fx2.get_part_by_tex("2").copy().set_color(YELLOW).set_z_index(1)
    scene.play(Create(ul), TransformMatchingTex(fx, fx2),
               TransformFromCopy(texts[1].get_part_by_tex("2"), fx2copy),
               FadeToColor(lineOfSymmetry, WHITE), FadeToColor(val3, WHITE))
    scene.play(FadeOut(ul), FadeToColor(fx2copy, WHITE), FadeToColor(fx2.get_part_by_tex("2"), WHITE), FadeToColor(fx2.get_part_by_tex("k"), BLUE))
    scene.remove(fx2copy)

    scene.play(FadeOut(fx_dividedByX), FadeToColor(fx2.get_part_by_tex("k"), WHITE), Indicate(ax, scale_factor=1), Indicate(axLabel))
    scene.play(Indicate(minLine, color=BLUE), Indicate(minLine2, color=BLUE))

    f1Line = VGroup(Line(ax.c2p(1,0), ax.c2p(1,func(1))), Line(ax.c2p(1,func(1)), ax.c2p(0,func(1)))).set_color(YELLOW)
    f1 = MathTex("f({{1}})").scale(0.7).next_to(f1Line[1], LEFT).set_color_by_tex("1", YELLOW)
    scene.play(FadeToColor(vals[0], YELLOW))
    scene.play(Create(f1Line))
    scene.play(Write(f1))
    f2Line = VGroup(Line(ax.c2p(2,0), ax.c2p(2,func(2))), Line(ax.c2p(2,func(2)), ax.c2p(0,func(2)))).set_color(BLUE)
    f2 = MathTex("f({{2}})").scale(0.7).next_to(f2Line[1], LEFT).set_color_by_tex("2", BLUE)
    scene.play(FadeToColor(vals[1], BLUE))
    scene.play(Create(f2Line))
    scene.play(Write(f2))

    f1f2eq = VGroup(f1.copy().scale(10/7), MathTex("= -"), f2.copy().scale(10/7)).arrange(RIGHT).next_to(fx2, DOWN*4, aligned_edge=LEFT)
    scene.play(TransformFromCopy(f1, f1f2eq[0]), TransformFromCopy(f2, f1f2eq[2]))
    scene.play(Write(f1f2eq[1]))
    scene.play(FadeOut(Group(graphGroup, f1, f2, f1Line, f2Line, minLine, minLine2, verticalLines, vals, lineOfSymmetry)))
    return fx2, f1f2eq