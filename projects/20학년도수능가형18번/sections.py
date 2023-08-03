from manim import *
from consts import *
from utils import *
import scipy.stats as stats

def showProblem(scene: Scene):
    #1
    scene.add(TEXTS)
    TEXTS.save_state()

def findRangeOfM(scene: Scene):
    #2
    conditions = VGroup(VGroup(Tex("①"),
                          Tex("{{$X$}}$\sim${{N($10,2^2$)}}, "),
                          Tex("{{$Y$}}$\sim${{N($m,2^2$)}}")).arrange().to_corner(UL),
                        VGroup(Tex("②"), Tex("{{$f(12) \leq g(20)$}}")).arrange()).arrange(buff=2).to_corner(UL)
    scene.play(FadeOut(TEXTS), 
               TransformFromCopy(TEXTS[1].get_part_by_tex("X"), conditions[0][1].get_part_by_tex("X")),
               TransformFromCopy(TEXTS[1].get_part_by_tex("N($10,2^2$)"), conditions[0][1].get_part_by_tex("N($10,2^2$)")),
               TransformFromCopy(TEXTS[1].get_part_by_tex("Y"), conditions[0][2].get_part_by_tex("Y")),
               TransformFromCopy(TEXTS[2].get_part_by_tex("N($m,2^2$)"), conditions[0][2].get_part_by_tex("N($m,2^2$)")),
               FadeIn(conditions[0][0], conditions[0][1][1], conditions[0][1][-1], conditions[0][2][1]),
               TransformFromCopy(TEXTS[4], conditions[1][1]),
               FadeIn(conditions[1][0]))
    XgraphDict = BasicGraphDict(xrange=[5,15], xLabelTex="$X$",
                                xLengthRatio=0.6, yLengthRatio=15,
                                hideYAxis=True,
                                func=lambda x: stats.norm.pdf(x, 10, 2))
    YgraphDict = BasicGraphDict(xrange=[-5, 5], xLabelTex="$Y$",
                                xLengthRatio=0.6, yLengthRatio=15,
                                hideYAxis=True,
                                func=lambda y: stats.norm.pdf(y, 0, 2))
    VGroup(XgraphDict, YgraphDict).arrange().shift(DOWN)
    #3
    scene.play(Create(XgraphDict))
    scene.play(TransformFromCopy(XgraphDict, YgraphDict))
    #4
    for10copy = Tex("N({{10}}").move_to(conditions[0][1][2], aligned_edge=LEFT)
    XgraphDict["lineOn10"] = XgraphDict["ax"].get_vertical_line(XgraphDict["ax"].input_to_graph_point(10, XgraphDict["graph"])).flip(RIGHT)
    scene.play(Create(XgraphDict["lineOn10"]))
    scene.play(TransformFromCopy(for10copy[1], XgraphDict.buildDotOnAxLabel(10, buff=0.01)))
    formcopy = Tex("N({{$m$}}").move_to(conditions[0][2][2], aligned_edge=LEFT)
    YgraphDict["lineOnM"] = YgraphDict["ax"].get_vertical_line(YgraphDict["ax"].input_to_graph_point(0, YgraphDict["graph"])).flip(RIGHT)
    scene.play(TransformFromCopy(formcopy[1], YgraphDict.buildDotOnAxLabel(0, buff=0.01, label="$m$", labelKey="labelOnM")),
               Create(YgraphDict["lineOnM"]))
    #5
    inequationDivided = MathTex("f(12) {{\leq}} g(20)").move_to(conditions[1][1])
    scene.play(FadeToColor(inequationDivided[0], PURE_GREEN))
    XgraphDict["lineOn12"] = XgraphDict["ax"].get_vertical_line(XgraphDict["ax"].input_to_graph_point(12, XgraphDict["graph"]))
    scene.play(Create(XgraphDict["lineOn12"]),
               Write(XgraphDict.buildDotOnAxLabel(12, buff=0.01)))
    line = Line(XgraphDict["ax"].i2gp(8, XgraphDict["graph"]), 
                YgraphDict["ax"].i2gp(2, YgraphDict["graph"])).set_color(PURE_GREEN)
    scene.play(Create(line))
    YgraphDict["lineOnM+2"] = YgraphDict["ax"].get_vertical_line(YgraphDict["ax"].input_to_graph_point(2, YgraphDict["graph"])).flip(RIGHT)
    YgraphDict["lineOnM-2"] = YgraphDict["ax"].get_vertical_line(YgraphDict["ax"].input_to_graph_point(-2, YgraphDict["graph"])).flip(RIGHT)
    scene.play(Create(YgraphDict["lineOnM+2"]), Create(YgraphDict["lineOnM-2"]))
    arcs = VGroup(
        ArcBetweenPoints(XgraphDict["ax"].c2p(10,0), XgraphDict["ax"].c2p(12,0), angle=-PI/2),
        ArcBetweenPoints(YgraphDict["ax"].c2p(-2,0), YgraphDict["ax"].c2p(0,0), angle=-PI/2),
        ArcBetweenPoints(YgraphDict["ax"].c2p(0,0), YgraphDict["ax"].c2p(2,0), angle=-PI/2),
    )
    arcLabels = VGroup(*[Tex("2").next_to(arc, UP, buff=0.1).scale(XgraphDict.getScaleRatio()) for arc in arcs])            
    scene.play(FadeIn(arcs, arcLabels))                 
    scene.play(Write(YgraphDict.buildDotOnAxLabel(2, buff=0.01, label="$m+2$", labelKey="labelOnM+2")),
               Write(YgraphDict.buildDotOnAxLabel(-2, buff=0.01, label="$m-2$", labelKey="labelOnM-2")))
    #6
    scene.play(FadeToColor(inequationDivided[2], VIOLET))
    scene.play(FadeIn(YgraphDict.buildGraph(lambda y: stats.norm.pdf(y, 0, 2), xRange=[-2,2], color=VIOLET, graphKey="graphFragment")))
    #7
    TEXTS.restore()
    toRemove = VGroup(conditions, XgraphDict, YgraphDict, arcs, arcLabels, line, inequationDivided)
    TEXTS.next_to(toRemove, buff=1).to_edge(UP)
    scene.play(VGroup(toRemove).animate.shift(LEFT*14), VGroup(TEXTS, TABLE).animate.to_corner(UL))
    scene.remove(toRemove)
    rangeOfM = MathTex("18 \leq m \leq 22").to_corner(UR).shift(DL)
    scene.play(Write(rangeOfM))

    return rangeOfM

def findMaxOfP(scene: Scene, rangeOfM):
    #8
    scene.play(VGroup(TEXTS, rangeOfM).animate.shift(LEFT*4))
    m = ValueTracker(19)
    scene.add(m)
    func = lambda y: stats.norm.pdf(y, m.get_value(), 2)
    graphDict = BasicGraphDict(xrange=[XSTART, XEND], xLabelTex="$Y$",
                               xLengthRatio=0.85, yLengthRatio=13, hideYAxis=True).shift(RIGHT*2.5, DOWN)
    scene.play(Create(graphDict))
    graphDict["lineOn21"] = Line(graphDict["ax"].c2p(21,0), graphDict["ax"].c2p(21, func(m.get_value())))
    graphDict["lineOn24"] = Line(graphDict["ax"].c2p(24,0), graphDict["ax"].c2p(24, func(m.get_value())))
    scene.play(Write(graphDict.buildDotOnAxLabel(21, buff=0.01)),
               Write(graphDict.buildDotOnAxLabel(24, buff=0.01)),
               Create(graphDict["lineOn21"]), Create(graphDict["lineOn24"]))
    box = SurroundingRectangle(VGroup(graphDict["lineOn21"], graphDict["lineOn24"]), 
                               fill_color=YELLOW, fill_opacity=0.6, stroke_width=0, buff=0)
    scene.play(FadeIn(box))
    #9
    scene.play(FadeOut(box))
    graphDict["graph"] = always_redraw(lambda: graphDict["ax"].plot(func))
    graphDict["lineOnM"] = always_redraw(lambda: graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(m.get_value(), graphDict["graph"])))
    scene.play(Create(graphDict["graph"]), Create(graphDict["lineOnM"]),
               Write(graphDict.buildDotOnAxLabel(m, buff=0.01, label="$m$", labelKey="labelOnM")))
    area = always_redraw(lambda: graphDict["ax"].get_area(graphDict["graph"], [21, 24], opacity=0.5, color=YELLOW, stroke_width=0))
    scene.play(FadeIn(area))
    #10
    scene.play(m.animate.set_value(22.5), rate_func=linear)
    scene.play(Transform(graphDict["labelOnM"], MathTex("22.5").scale(graphDict.getScaleRatio()).next_to(graphDict["ax"].c2p(22.5, -0.01), DOWN, aligned_edge=UP, buff=0)))
    #11
    scene.play(FadeToColor(rangeOfM, PURE_GREEN))
    line = Line(graphDict["ax"].c2p(18,0), graphDict["ax"].c2p(22,0), color=PURE_GREEN, stroke_width=4)
    scene.play(FadeOut(graphDict["labelOnM"]), Create(line),
               Write(graphDict.buildDotOnAxLabel(18, buff=0.01).set_color(PURE_GREEN)), 
               Write(graphDict.buildDotOnAxLabel(22, buff=0.01).set_color(PURE_GREEN)))
    graphDict.remove("labelOnM")
    #12
    scene.play(m.animate.set_value(22), rate_func=linear)
    #13
    toFadeOut = VGroup(rangeOfM, line, graphDict["labelOn18"])
    graphDict.remove("labelOn18")
    scene.play(FadeOut(toFadeOut),
               VGroup(TEXTS).animate.shift(RIGHT*4), graphDict.animate.shift(DR*1.8),
               graphDict["labelOn22"].animate.set_color(WHITE).shift(DR*1.8))
    scene.remove(area)
    area = VGroup(graphDict["ax"].get_area(graphDict["graph"], [21, m.get_value()], opacity=0.5, color=YELLOW, stroke_width=0),
                  graphDict["ax"].get_area(graphDict["graph"], [m.get_value(), 24], opacity=0.5, color=YELLOW, stroke_width=0))
    scene.add(area)
    scene.play(FadeToColor(area[1], BLUE),
               Transform(graphDict["lineOn21"], graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(21, graphDict["graph"]), line_func=Line)),
               Transform(graphDict["lineOn24"], graphDict["ax"].get_vertical_line(graphDict["ax"].i2gp(24, graphDict["graph"]), line_func=Line)))