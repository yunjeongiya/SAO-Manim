from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    ax = Axes(
        x_range=[XSTART, XEND, 1],
        y_range=[YSTART, YEND, 1],
        x_length=(XEND-XSTART)*3,
        y_length=(YEND-YSTART)*3,
        axis_config={
            "include_tip": True,
            "tip_width": 0.1,
            "tip_height": 0.15,
            "include_ticks": False,
            "include_numbers": False,
        },
    )
    axLabel = VGroup(ax.get_x_axis_label("x").shift(LEFT*0.3+DOWN*0.7),
                     ax.get_y_axis_label("y").shift(LEFT*0.7+DOWN*0.3),
                     MathTex(r"\mathrm{O}").next_to(ax.c2p(0, 0), DL*0.4))
    fx = fxGraphBuilder(0, ax)
    fxLabel = MathTex("y={{f(x)}}").next_to(fx, LEFT).shift(RIGHT*4+UP)

    aLabel = MathTex("a").next_to(ax.c2p(A, 0), DOWN*1.3)

    fxMinusA = VGroup(DashedVMobject(fxGraphBuilder(A, ax)[0], num_dashes=20),
                            DashedVMobject(fxGraphBuilder(A, ax)[1], num_dashes=35))
    fxMinusALabel = MathTex("y={{f(x-a)}}").next_to(fxMinusA, RIGHT).shift(LEFT*2+DOWN*0.5)
    graphDict = VDict({
        "ax" : ax, "axLabel" : axLabel,
        "aLabel" : aLabel, "fxMinusA": fxMinusA, "fxMinusALabel" : fxMinusALabel,
        "fx" : fx.set_z_index(4), "fxLabel" : fxLabel
    })
    ax2 = ax.copy()
    axLabel2 = axLabel.copy()
    gx = VGroup(ax.plot(lambda x : 0, x_range=[XSTART, 0], stroke_width=2),
                ax.plot(lambda x : x*(2-x), x_range=[0, 2], stroke_width=2),
                ax.plot(lambda x : 0, x_range=[2, XEND], stroke_width=2))
    gxLabel = MathTex("y=g(x)").next_to(gx, RIGHT).shift(LEFT*3+UP)
    gxVertex = VGroup(
        ax.get_lines_to_point(ax.c2p(1,1)),
        MathTex("1").next_to(ax.c2p(1,0), DOWN),
        MathTex("1").next_to(ax.c2p(0,1), LEFT)
    )
    graphDict2 = VDict({
        "ax" : ax2, "axLabel" : axLabel2,
        "gx" : gx, "gxLabel" : gxLabel, "gxVertex" : gxVertex,
        "2Label" : MathTex("2").next_to(ax.c2p(2,0), DOWN)
    })

    scene.add(TEXTS, VGroup(graphDict, graphDict2).arrange(RIGHT).scale(0.5).next_to(TEXTS, DOWN, aligned_edge=LEFT))
    
    return graphDict, graphDict2

def describeProblem(scene:Scene):
    scene.play(Circumscribe(TEXTS[2][0], fade_out=True), Circumscribe(TEXTS[2][1], fade_out=True))
    ul = Underline(TEXTS[4], color=YELLOW)
    scene.play(Create(ul))
    scene.remove(ul)
    ul2 = Underline(TEXTS[3].get_part_by_tex("양의 실수 $k, a, b$"), color=YELLOW)
    scene.play(Create(ul2),
               Indicate(TEXTS[4].get_part_by_tex("k")),
               Indicate(TEXTS[4].get_part_by_tex("a")),
               Indicate(TEXTS[4].get_part_by_tex("b")))
    scene.remove(ul2)
    ul3 = Underline(TEXTS[5].get_part_by_tex(r"0\leq h(x)\leq g(x)"), color=YELLOW)
    scene.play(Create(ul3))
    scene.remove(ul3)
    ul4 = Underline(TEXTS[6].get_part_by_tex("최소가 되게 하는 $k, a, b$"), color=YELLOW)
    box = SurroundingRectangle(TEXTS[6][0])
    scene.play(Create(ul4), Create(box))
    scene.remove(ul4, box)
    scene.play(Create(ul))
    scene.remove(ul)

def analyzeHx(scene:Scene, graphDict, graphDict2):
    hxTex = MathTex(r"h(x)={{k}}\{ {{f(x)}}-{{f(x-a)}}-{{f(x-b)}}+{{f(x-2)}}\}").scale_to_fit_height(TEXTS[4].height).move_to(TEXTS[4], aligned_edge=LEFT)
    ab2Ineq = TEXTS[3].get_part_by_tex("a<b<2").copy()
    scene.add(hxTex, ab2Ineq)
    scene.remove(TEXTS[4].set_color(BLACK), TEXTS[3].get_part_by_tex("a<b<2").set_color(BLACK))

    scene.play(FadeToColor(VGroup(
        hxTex.get_part_by_tex("f(x)"),
        graphDict["fx"], graphDict["fxLabel"].get_part_by_tex("f(x)")), YELLOW))
    
    newFxMinusA = fxGraphBuilder(A, graphDict["ax"]).set_stroke_color(MINT)
    scene.play(FadeToColor(VGroup(
        hxTex.get_part_by_tex("f(x-a)"), graphDict["fxMinusALabel"].get_part_by_tex("f(x-a)")), MINT),
        FadeIn(newFxMinusA.set_z_index(3)))
    scene.remove(graphDict["fxMinusA"])
    graphDict["fxMinusA"] = newFxMinusA
    scene.play(FadeOut(Group(graphDict2, TEXTS)),
               hxTex.animate.scale(1.5).to_corner(UL),
               ab2Ineq.animate.scale(1.5).to_corner(UR).shift(LEFT),
               graphDict.animate.scale(2).to_corner(DL),
               graphDict["fxLabel"].animate.scale(1.3).to_edge(UP).shift(DR*2+RIGHT*2),
               graphDict["fxMinusALabel"].animate.scale(1.3).to_edge(UP).shift(DR*2+RIGHT*2))
    
    bLabel = MathTex("b").next_to(graphDict["ax"].c2p(B,0), DOWN)
    fxMinusB = fxGraphBuilder(B, graphDict["ax"]).set_stroke_color(NEON_PURPLE).set_z_index(2)
    fxMinusBLabel = MathTex("y={{f(x-b)}}").set_color_by_tex("f(x-b)", NEON_PURPLE).scale_to_fit_height(graphDict["fxLabel"].height).next_to(fxMinusB, UR*0.8)
    twoLabel = MathTex("2").next_to(graphDict["ax"].c2p(2,0), DOWN)
    fxMinus2 = fxGraphBuilder(2, graphDict["ax"]).set_stroke_color(PURE_GREEN).set_z_index(1)
    fxMinus2Label = MathTex("y={{f(x-2)}}").set_color_by_tex("f(x-2)", PURE_GREEN).scale_to_fit_height(graphDict["fxLabel"].height).next_to(fxMinus2, UR*0.8)
    
    oldAx = graphDict["ax"]
    newAx = Axes(
        x_range=[XSTART, XEND+1, 1],
        y_range=[YSTART, YEND, 1],
        x_length=((XEND+1)-XSTART)*3,
        y_length=(YEND-YSTART)*3,
        axis_config={
            "include_tip": True,
            "tip_width": 0.1,
            "tip_height": 0.15,
            "include_ticks": False,
            "include_numbers": False,
        }).scale_to_fit_height(graphDict["ax"].height).move_to(graphDict["ax"], aligned_edge=LEFT)
    scene.play(FadeToColor(hxTex.get_part_by_tex("f(x-b)"), NEON_PURPLE),
               Create(fxMinusB), Write(bLabel),
               TransformFromCopy(graphDict["ax"], newAx), 
               graphDict["ax"].animate.set_color(BLACK).set_z_index(-1),
               graphDict["axLabel"][0].animate.shift(RIGHT*3))
    scene.play(Create(fxMinusBLabel))
    scene.play(FadeToColor(hxTex.get_part_by_tex("f(x-2)"), PURE_GREEN),
               Create(fxMinus2), Write(twoLabel))
    scene.play(Create(fxMinus2Label))
    graphDict.add([("bLabel", bLabel), ("fxMinusB", fxMinusB), ("fxMinusBLabel", fxMinusBLabel), 
                   ("twoLabel", twoLabel), ("fxMinus2", fxMinus2), ("fxMinus2Label", fxMinus2Label)])

    box = SurroundingRectangle(hxTex[3:6], color=RED)
    scene.play(FadeToColor(VGroup(fxMinusB, fxMinusBLabel, fxMinus2, hxTex.get_part_by_tex("f(x-b)"), fxMinus2Label, hxTex.get_part_by_tex("f(x-2)")), WHITE), Create(box))
    hx = VGroup(graphDict["ax"].plot(lambda x : 0, x_range=[XSTART, 0], color=RED).set_z_index(5))
    scene.play(Create(hx))
    graphDict["hx"] = hx

    a = ValueTracker(A)
    scene.add(a)
    graphDict["aLabel"].add_updater(lambda m: m.next_to(graphDict["ax"].c2p(a.get_value(), 0), DOWN*1.3))
    k = ValueTracker(1)
    scene.add(k)
    hx.add(always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*x, [0, a.get_value()], color=RED).set_z_index(5)))
    aVerticalLine = always_redraw(lambda: graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(a.get_value(), hx[1])))
    scene.play(Create(hx[-1]), Create(aVerticalLine))
    graphDict["aVerticalLine"] = aVerticalLine
    
    arrowNum = 4
    diff = VGroup()
    for i in range(arrowNum):
        x = A+(B-A)/(arrowNum-1)*i
        diff.add(DoubleArrow(graphDict["ax"].c2p(x, x), graphDict["ax"].c2p(x,x-A), tip_length=0.15))
        #diff.append(DoubleArrow(graphDict["ax"].i2gp(x, graphDict["fx"][1]), graphDict["ax"].i2gp(x, graphDict["fxMinusA"][1]), tip_length=0.2)) #TODO: 왜 약간 아래로 치우치는지..?
    
    #scene.play(AnimationGroup(Create(diff[i]) for i in range(arrowNum))) #TypeError: Object <generator object analyzeHx.<locals>.<genexpr> at 0x000001B3A06BFB50> cannot be converted to an animation
    #scene.play(Create(diff[i]) for i in range(arrowNum)) #TypeError: Unexpected argument <generator object analyzeHx.<locals>.<genexpr> at 0x000001B3A06BFB50> passed to Scene.play().
    scene.play(*[Create(diff[i]) for i in range(arrowNum)], run_time=0.5) #리스트컴프리헨션으로 리스트로 감싸고 다시 언패킹해서 넣어줘야 함
    
    hx.add(graphDict["ax"].plot(lambda x: k.get_value()*a.get_value(), [a.get_value(), XEND+1], color=RED).set_z_index(5))
    scene.play(FadeOut(diff), Create(hx[-1]))

    scene.play(FadeToColor(VGroup(hxTex.get_part_by_tex("f(x)"), hxTex.get_part_by_tex("f(x-a)")), WHITE),
               FadeOut(Group(graphDict["fx"], graphDict["fxLabel"], graphDict["fxMinusA"], graphDict["fxMinusALabel"])))
    graphDict.remove("fx")
    graphDict.remove("fxLabel")
    graphDict.remove("fxMinusA")
    graphDict.remove("fxMinusALabel")

    scene.play(FadeToColor(VGroup(hxTex.get_part_by_tex("f(x-b)"), fxMinusB), NEON_PURPLE))

    b = ValueTracker(B)
    scene.add(b)
    graphDict["bLabel"].add_updater(lambda m: m.next_to(graphDict["ax"].c2p(b.get_value(), 0), DOWN))
    bVerticalLine = always_redraw(lambda: graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(b.get_value(), hx[2])))
    scene.play(Create(bVerticalLine))

    scene.play(hxTex.get_parts_by_tex("-")[2].animate.scale(2).set_color(NEON_PURPLE), run_time=0.5)
    scene.play(hxTex.get_parts_by_tex("-")[2].animate(run_time=0.5).scale(1/2),
               Transform(fxMinusB[1], fxMinusB[1].copy().rotate(-PI/2, about_point=graphDict["ax"].c2p(B,0)).shift(UP*1.5).set_z_index(2)),
               (VGroup(*graphDict)-fxMinusB-fxMinusBLabel+newAx).animate.shift(UP*1.5),
               fxMinusB[0].animate.shift(UP*1.5),
               Transform(fxMinusBLabel, MathTex("y={{-}}{{f(x-b)}}").scale_to_fit_height(graphDict["fxMinusBLabel"].height).shift(DOWN*3+LEFT*2)))

    scene.play(Transform(box, SurroundingRectangle(hxTex[3:8], color=RED)))
    oldHxFromA = hx[-1]
    hx[-1] = always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*a.get_value(), [a.get_value(), b.get_value()], color=RED).set_z_index(5))
    hx.add(always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*(b.get_value()-x+a.get_value()), [b.get_value(), XEND+1], color=RED).set_z_index(5)))
    scene.play(FadeOut(oldHxFromA), Create(hx[-1]))

    scene.play(FadeToColor(VGroup(hxTex.get_part_by_tex("f(x-2)"), fxMinus2), PURE_GREEN),
               FadeToColor(VGroup(hxTex.get_parts_by_tex("-")[2], hxTex.get_part_by_tex("f(x-b)")), WHITE),
               FadeOut(Group(fxMinusB, fxMinusBLabel)))
    graphDict.remove("fxMinusB")
    graphDict.remove("fxMinusBLabel")
    twoVerticalLine = always_redraw(lambda: graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(2, hx[3])))
    scene.play(Create(twoVerticalLine))

    line = graphDict["ax"].plot(lambda x: b.get_value()-2+a.get_value(), [2, XEND+1])
    scene.play(Create(line))

    area = graphDict["ax"].get_area(fxMinus2[1], x_range=[2,XEND+1], color=YELLOW, opacity=0.5)
    area2 = graphDict["ax"].get_area(line, x_range=[2,XEND+1], color=YELLOW, opacity=0.5, bounded_graph=hx[-1])
    scene.play(FadeIn(VGroup(area, area2)))

    oldHxFrom2 = hx[-1]
    hx[-1] = always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*(b.get_value()-x+a.get_value()), [b.get_value(), 2], color=RED).set_z_index(5))
    hx.add(always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*(b.get_value()-2+a.get_value()), [2, XEND+1], color=RED).set_z_index(5)))
    scene.play(FadeOut(VGroup(oldHxFrom2, area, area2, line)), Create(hx[-1]),
               Transform(box, SurroundingRectangle(hxTex[3:-1], color=RED)),
               FadeToColor(hxTex.get_part_by_tex("f(x-2)"), WHITE),
               FadeOut(VGroup(fxMinus2, fxMinus2Label)))
    graphDict.remove("fxMinus2")
    graphDict.remove("fxMinus2Label")

    scene.play(FadeToColor(graphDict["aLabel"], YELLOW),
               a.animate.set_value(1/4))
    scene.play(a.animate.set_value(2/3))
    scene.play(FadeToColor(graphDict["aLabel"], WHITE), FadeToColor(graphDict["bLabel"], YELLOW),
               b.animate.set_value(7/4))
    scene.play(b.animate.set_value(4/3))
    scene.play(FadeToColor(graphDict["bLabel"], WHITE),
               hxTex.get_parts_by_tex("k").animate.scale(3/2).set_color(YELLOW), run_time=0.5)
    scene.play(hxTex.get_parts_by_tex("k").animate.scale(2/3), run_time=0.5)
    scene.play(k.animate.set_value(2))
    scene.play(k.animate.set_value(1/2))
    scene.play(k.animate.set_value(1))

    hxLabel = graphDict["ax"].get_graph_label(hx[2], "y=h(x)", x_val=1.5, color=WHITE)
    graphDict["hxLabel"] = hxLabel
    oldAx.set_color(WHITE)
    newHxFrom2 = always_redraw(lambda: graphDict["ax"].plot(lambda x: k.get_value()*(b.get_value()-2+a.get_value()), [2, XEND], color=RED).set_z_index(5))
    scene.play(Transform(box, SurroundingRectangle(hxTex[1:], color=RED)),
               Write(hxLabel), FadeToColor(hxTex.get_part_by_tex("k"), WHITE),
               Transform(newAx, oldAx), Transform(hx[-1], newHxFrom2), graphDict["axLabel"][0].animate.shift(LEFT*3),)
    hx[-1] = newHxFrom2
    scene.remove(newAx)
    return VGroup(hxTex, box, ab2Ineq)
    