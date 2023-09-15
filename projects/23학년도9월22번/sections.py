from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    func = lambda x: (x-3)**2*(x-6)+8
    graphDict = BasicGraphDict([XSTART,XEND], [YSTART, YEND], 
                               hideXAxis=True, hideYAxis=True,
                               yLengthRatio=0.5,
                               func=func,
                               graphLabelTex=MathTex("y={{f}}(x)"),
                               graphXRange=[G_XSTART, G_XEND]).scale(0.7).next_to(TEXTS)
    scene.play(Create(graphDict))

    graphDict["lineOn3"] = DashedLine(graphDict["ax"].c2p(3, YSTART),
                                      graphDict["ax"].i2gp(3, graphDict["graph"]),
                                      stroke_width=2)
    graphDict["labelOn3"] = MathTex("3").next_to(graphDict["lineOn3"], DOWN)
    scene.play(Create(graphDict["lineOn3"]), Write(graphDict["labelOn3"]))
    graphDict["lineOnY8"] = DashedLine(graphDict["ax"].c2p(XSTART, 8),
                                       graphDict["ax"].c2p(XEND, 8),
                                       stroke_width=2)
    graphDict["labelOnY8"] = MathTex("8").next_to(graphDict["lineOnY8"])
    scene.play(Create(graphDict["lineOnY8"]), Write(graphDict["labelOnY8"]))
    #3
    t = ValueTracker(2.5)
    scene.add(t)
    
    graphDict["lineOnT"] = always_redraw(lambda:
                           Line(graphDict["ax"].c2p(t.get_value(), YSTART),
                                graphDict["ax"].c2p(t.get_value(), YEND),
                                stroke_width=2))
    graphDict["labelOnT"] = MathTex("t").add_updater(lambda m: m.next_to(graphDict["lineOnT"], DOWN))
    scene.play(Create(graphDict["lineOnT"]), Write(graphDict["labelOnT"]))
    graphDict["graph"] = VGroup(
        graphDict["ax"].plot(func, [G_XSTART, t.get_value()]),
        graphDict["ax"].plot(func, [t.get_value(), G_XEND])
    )
    offset = ValueTracker(func(t.get_value())*2)
    scene.add(offset)
    dividedGraph = always_redraw(lambda: VGroup(
        graphDict["ax"].plot(lambda x: -func(x)+offset.get_value(), [G_XSTART, t.get_value()]).set_color(PURE_GREEN),
        graphDict["ax"].plot(func, [t.get_value(), G_XEND])
    ))
    gxLabel = MathTex("y={{g}}(x)").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["graphLabel"], aligned_edge=LEFT)
    scene.play(ReplacementTransform(graphDict["graph"], dividedGraph),
               TransformMatchingTex(graphDict["graphLabel"], gxLabel))
    graphDict["graphLabel"] = gxLabel
    graphDict["graph"] = dividedGraph
    scene.play(offset.animate.set_value(offset.get_value()+2))
    scene.play(offset.animate.set_value(offset.get_value()-4))
    scene.play(offset.animate.set_value(offset.get_value()+2))
    #4
    offset.add_updater(lambda m: m.set_value(func(t.get_value())*2))
    scene.play(t.animate.set_value(4.5), rate_func=linear, run_time=3)
    scene.play(t.animate.set_value(2.5), rate_func=linear, run_time=3)
    #5
    graphDict.shift(LEFT*8.5)
    fxLabel = MathTex("y={{f}}(x)").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["graphLabel"], aligned_edge=LEFT)
    graphDict.shift(RIGHT*8.5)
    graphDict["ax"].shift(LEFT*8.5)
    scene.play(Group(TEXTS, graphDict["graph"][1],
                     graphDict["labelOn3"], graphDict["lineOn3"],
                     graphDict["labelOnY8"], graphDict["lineOnY8"]).animate.shift(LEFT*8.5),
               VGroup(graphDict["lineOnT"].clear_updaters(), graphDict["labelOnT"].clear_updaters()).animate.shift(LEFT*8.5).set_opacity(0),
               TransformMatchingTex(graphDict["graphLabel"], fxLabel),
               Transform(graphDict["graph"][0], graphDict["ax"].plot(func, [G_XSTART, t.get_value()])))
    graphDict["graphLabel"] = fxLabel
    t.set_value(G_XSTART)
    graphDict["fakeXAx"] = VGroup(
        Arrow(graphDict["ax"].c2p(XSTART, 6),
              graphDict["ax"].c2p(XEND, 6),
              max_tip_length_to_length_ratio=0.04,
              stroke_width=2, buff=0),
        MathTex("x").next_to(graphDict["ax"].c2p(XEND, 6), DOWN, buff=0.2)
    )
    scene.play(Create(graphDict["fakeXAx"]))
    #6
    t.set_value(2)
    graphDict["lineOnT"] = always_redraw(lambda:
                           Line(graphDict["ax"].c2p(t.get_value(), YSTART),
                                graphDict["ax"].c2p(t.get_value(), YEND),
                                stroke_width=2, color=PURE_GREEN))
    graphDict["labelOnT"] = MathTex("t").add_updater(lambda m: m.next_to(graphDict["lineOnT"], DOWN))
    scene.play(Create(graphDict["lineOnT"]), Write(graphDict["labelOnT"]))
    graphDict["graph"].become(VGroup(
        graphDict["ax"].plot(func, [G_XSTART, t.get_value()]),
        graphDict["ax"].plot(func, [t.get_value(), G_XEND])
    ))
    dividedGraph = always_redraw(lambda: VGroup(
        graphDict["ax"].plot(lambda x: -func(x)+offset.get_value(), [1.387, t.get_value()]),
        graphDict["ax"].plot(func, [t.get_value(), G_XEND])
    ))
    gxLabel = MathTex("y={{g}}(x)").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["graphLabel"], aligned_edge=LEFT)
    scene.play(ReplacementTransform(graphDict["graph"], dividedGraph),
               TransformMatchingTex(graphDict["graphLabel"], gxLabel))
    graphDict["graphLabel"] = gxLabel
    graphDict["graph"] = dividedGraph
    
    dots = VGroup(
        Dot().move_to(graphDict["ax"].c2p(1.804, 6)),
        Dot().move_to(graphDict["ax"].c2p(2.268, 6)),
        Dot().move_to(graphDict["ax"].c2p(4, 6)),
        Dot().move_to(graphDict["ax"].c2p(5.732, 6))
    ).set_color(VIOLET)
    scene.play(FadeIn(dots))
    #7
    hGraphDict = BasicGraphDict([1.5, XEND], [-1, 5], yLengthRatio=0.8, xLengthRatio=1.8,
                                xLabelTex="$t$", hideYAxis=True)
    hGraphDict["lines"] = VGroup(
        *[Line(hGraphDict["ax"].c2p(1.5, i), hGraphDict["ax"].c2p(XEND, i), stroke_width=2)
          for i in range(5)]
    )
    hGraphDict["numbersOnY"] = VGroup(
        *[MathTex(f"{i}").next_to(hGraphDict["lines"][i], LEFT)
          for i in range(5)]
    )
    scene.play(Create(hGraphDict.scale(0.8).to_edge(RIGHT).shift(UP)))
    hGraphDict.buildLine("greenBar", [t.get_value(), -0.5], [t.get_value(), 4.5], color=PURE_GREEN)
    hGraphDict["greenBar"].add_updater(lambda m: m.move_to(hGraphDict["ax"].c2p(t.get_value(), -0.5), aligned_edge=DOWN))
    scene.play(Create(hGraphDict["greenBar"]))
    hGraphDict["graphLabel"] = MathTex("y=h(t)", color=VIOLET).scale(0.8).next_to(hGraphDict["greenBar"], UP)
    dot = Dot(hGraphDict["ax"].c2p(t.get_value(), 4), color=VIOLET).add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 4)))
    scene.play(Write(hGraphDict["graphLabel"]), Create(dot))
    #8
    hGraphDict.buildLine("0", (t.get_value(), 4), (4-3**(1/2), 4), color=VIOLET, stroke_width=3)
    scene.play(t.animate.set_value(4-3**(1/2)),
               dots[0].animate.move_to(graphDict["ax"].c2p(2.268, 6)),
               Create(hGraphDict["0"]), rate_func=linear)
    dot.clear_updaters()
    oldDots = VGroup(Dot(hGraphDict["ax"].c2p(t.get_value(), 4), fill_opacity=0, color=VIOLET, stroke_width=2))
    scene.add(oldDots)
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    #9
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("1", (t.get_value(), 2), (3.65270, 2), color=VIOLET, stroke_width=3)
    dots[0].set_opacity(0)
    dots[1].set_opacity(0)
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("dashed0", (t.get_value(), 4), (t.get_value(), 2), isDashedLine=True)
    scene.play(t.animate.set_value(3.65270),
               Create(hGraphDict["1"]), rate_func=linear, run_time=2)
    dots[1].set_opacity(1).move_to(graphDict["ax"].c2p(3, 6))
    oldDots.add(oldDots[0].copy().move_to(dot))
    dot.clear_updaters()
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    #10
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 4)))
    hGraphDict.buildLine("2", (t.get_value(), 4), (4, 4), color=VIOLET, stroke_width=3)
    hGraphDict.buildLine("dashed1", (t.get_value(), 4), (t.get_value(), 2), isDashedLine=True)
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 4)))
    scene.play(t.animate(rate_func=linear).set_value(4),
               dots[0].set_opacity(1).move_to(graphDict["ax"].c2p(3, 6)).animate(rate_func=slow_into).move_to(graphDict["ax"].c2p(4, 6)),
               dots[1].animate(rate_func=slow_into).move_to(graphDict["ax"].c2p(4-3**(1/2), 6)),
               Create(hGraphDict["2"], rate_func=linear))
    dots[0].set_opacity(0)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("dashed2", (t.get_value(), 4), (t.get_value(), 2), isDashedLine=True)
    #11
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("3", (t.get_value(), 2), (5.53208, 2), color=VIOLET, stroke_width=3)
    dots[2].set_opacity(0)
    scene.play(t.animate(rate_func=linear).set_value(5.53208),
               dots[1].animate().move_to(graphDict["ax"].c2p(2, 6)),
               Create(hGraphDict["3"], rate_func=linear))
    dots[2].move_to(graphDict["ax"].c2p(5, 6)).set_opacity(1)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 4)))
    hGraphDict.buildLine("dashed3", (t.get_value(), 4), (t.get_value(), 2), isDashedLine=True)
    #12
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 4)))
    hGraphDict.buildLine("4", (t.get_value(), 4), (4+3**(1/2), 4), color=VIOLET, stroke_width=3)
    scene.play(t.animate.set_value(4+3**(1/2)),
               dots[0].set_opacity(1).move_to(graphDict["ax"].c2p(5, 6)).animate.move_to(dots[3]),
               dots[1].animate.move_to(graphDict["ax"].c2p(2.268, 6)),
               dots[2].animate.move_to(graphDict["ax"].c2p(4, 6)),
               Create(hGraphDict["4"]), rate_func=linear)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("dashed4", (t.get_value(), 4), (t.get_value(), 2), isDashedLine=True)
    #13
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("5", (t.get_value(), 2), (5.87938, 2), color=VIOLET, stroke_width=3)
    dots[0].set_opacity(0)
    dots[3].set_opacity(0)
    scene.play(t.animate.set_value(5.87938),
               dots[1].animate.move_to(graphDict["ax"].c2p(3, 6)),
               dots[2].animate.move_to(graphDict["ax"].c2p(3, 6)),
               Create(hGraphDict["5"]), rate_func=linear)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 1)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 0)))
    hGraphDict.buildLine("dashed5", (t.get_value(), 2), (t.get_value(), 0), isDashedLine=True)
    #14
    dots[2].set_opacity(0)
    dots[1].set_opacity(0)
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 0)))
    hGraphDict.buildLine("6", (t.get_value(), 0), (XEND, 0), color=VIOLET, stroke_width=3)
    scene.play(t.animate.set_value(XEND),
               Create(hGraphDict["6"]), rate_func=linear)
    #15
    dot.clear_updaters()
    scene.play(t.animate.set_value(1.8),
               FadeOut(dot, oldDots),
               *[hGraphDict[f"{i}"].animate.set_opacity(0) for i in range(7)], *[hGraphDict[f"dashed{i}"].animate.set_opacity(0) for i in range(6)])
    scene.play(Transform(graphDict["fakeXAx"],
        VGroup(
        Arrow(graphDict["ax"].c2p(XSTART, 4),
              graphDict["ax"].c2p(XEND, 4),
              max_tip_length_to_length_ratio=0.04,
              stroke_width=2, buff=0),
        MathTex("x").next_to(graphDict["ax"].c2p(XEND, 4), DOWN, buff=0.2)
    )))
    scene.add(dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 3))))
    dots[0].move_to(graphDict["ax"].c2p(1.638, 4)).set_opacity(1)
    dots[1].move_to(graphDict["ax"].c2p(2, 4)).set_opacity(1)
    dots[2].move_to(graphDict["ax"].c2p(5, 4)).set_opacity(1)
    #16
    next_t = 2
    hGraphDict.buildLine("0", (t.get_value(), 3), (next_t, 3), color=VIOLET, stroke_width=3)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               Create(hGraphDict["0"], rate_func=linear),
               dots[0].animate(rate_func=linear).move_to(dots[1]))
    dots[0].set_opacity(0)
    dot.clear_updaters()
    oldDots = VGroup(oldDots[0].move_to(dot))
    scene.add(oldDots)
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 1)))
    hGraphDict.buildLine("dashed0", (t.get_value(), 3), (t.get_value(), 1), isDashedLine=True)
    #17
    next_t = 4
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 1)))
    hGraphDict.buildLine("1", (t.get_value(), 1), (next_t, 1), color=VIOLET, stroke_width=3)
    dots[1].set_opacity(0)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               Create(hGraphDict["1"], rate_func=linear))
    dots[1].move_to(graphDict["ax"].c2p(3, 4)).set_opacity(1)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    hGraphDict.buildLine("dashed1", (t.get_value(), 3), (t.get_value(), 1), isDashedLine=True)
    #18
    next_t = 5
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 3)))
    hGraphDict.buildLine("2", (t.get_value(), 3), (next_t, 3), color=VIOLET, stroke_width=3)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               dots[0].move_to(dots[1]).set_opacity(1).animate(rate_func=slow_into).move_to(graphDict["ax"].c2p(2,4)),
               dots[1].set_opacity(1).animate().move_to(dots[2]),
               Create(hGraphDict["2"], rate_func=linear))
    dots[2].set_opacity(0)
    dot.clear_updaters()
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 2)))
    hGraphDict.buildLine("dashed2", (t.get_value(), 3), (t.get_value(), 2), isDashedLine=True)
    #19
    scene.play(t.animate.set_value(1.5),
               dots.animate.set_opacity(0),
               FadeOut(dot, oldDots),
               *[hGraphDict[f"{i}"].animate.set_opacity(0) for i in range(7)], *[hGraphDict[f"dashed{i}"].animate.set_opacity(0) for i in range(6)])
    scene.play(Transform(graphDict["fakeXAx"],
        VGroup(
        Arrow(graphDict["ax"].c2p(XSTART, -1),
              graphDict["ax"].c2p(XEND, -1),
              max_tip_length_to_length_ratio=0.04,
              stroke_width=2, buff=0),
        MathTex("x").next_to(graphDict["ax"].c2p(XEND, -1), DOWN, buff=0.2)
    )))
    scene.add(dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 2))))
    scene.add(dots.set_opacity(0))
    dots[0].set_opacity(1).move_to(graphDict["ax"].c2p(1.431, -1))
    dots[1].set_opacity(1).move_to(graphDict["ax"].c2p(1.574, -1))
    #20
    next_t = 1.574
    hGraphDict.buildLine("0", (t.get_value(), 2), (next_t, 2), color=VIOLET, stroke_width=3)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               Create(hGraphDict["0"], rate_func=linear),
               dots[0].animate(rate_func=linear).move_to(graphDict["ax"].c2p(1.574,-1)),
               dots[1].animate(rate_func=linear).move_to(graphDict["ax"].c2p(1.574,-1)))
    dots[0].set_opacity(0)
    dot.clear_updaters()
    oldDots = VGroup(oldDots[0].move_to(dot))
    scene.add(oldDots)
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 1)))
    oldDots.add(dot.copy())
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(oldDots[-1].animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 0)))
    hGraphDict.buildLine("dashed0", (t.get_value(), 2), (t.get_value(), 0), isDashedLine=True)
    #21
    next_t = 5
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 0)))
    hGraphDict.buildLine("1", (t.get_value(), 0), (next_t, 0), color=VIOLET, stroke_width=3)
    dots[1].set_opacity(0)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               Create(hGraphDict["1"], rate_func=linear), run_time=2)
    dot.clear_updaters()
    #22
    scene.play(Transform(graphDict["fakeXAx"],
        VGroup(
        Arrow(graphDict["ax"].c2p(XSTART, 0),
              graphDict["ax"].c2p(XEND, 0),
              max_tip_length_to_length_ratio=0.04,
              stroke_width=2, buff=0),
        MathTex("x").next_to(graphDict["ax"].c2p(XEND, 0), DOWN, buff=0.2)
    )))
    dots[0].set_opacity(1).move_to(graphDict["ax"].c2p(3, 0))
    oldDots.add(oldDots[0].copy().move_to(dot))
    scene.play(dot.animate.move_to(hGraphDict["ax"].c2p(t.get_value(), 1)))
    oldDots.add(dot.copy())
    hGraphDict.buildLine("dashed1", (t.get_value(), 1), (t.get_value(), 0), isDashedLine=True)
    #23
    next_t = XEND
    dot.add_updater(lambda m : m.move_to(hGraphDict["ax"].c2p(t.get_value(), 0)))
    hGraphDict.buildLine("2", (t.get_value(), 0), (next_t, 0), color=VIOLET, stroke_width=3)
    dots[0].set_opacity(0)
    scene.play(t.animate(rate_func=linear).set_value(next_t),
               Create(hGraphDict["2"], rate_func=linear), run_time=2)
    dot.clear_updaters()
    #24
    scene.play(FadeOut(hGraphDict, oldDots, dot))
    scene.play(t.animate.set_value(5), rate_fun=linear)
    #25
    graphDict["lineOnY4"] = DashedLine(graphDict["ax"].c2p(XSTART, 4),
                                       graphDict["ax"].c2p(XEND, 4),
                                       stroke_width=2)
    graphDict["labelOnY4"] = MathTex("4").next_to(graphDict["lineOnY4"])
    scene.play(Create(graphDict["lineOnY4"]), Write(graphDict["labelOnY4"]))
    graphDict["graph"].clear_updaters()
    scene.play(Transform(graphDict["graph"][0], graphDict["ax"].plot(func, [G_XSTART, t.get_value()])))
    #26
    scene.play(Group(TEXTS, graphDict).animate.shift(RIGHT*8.5))