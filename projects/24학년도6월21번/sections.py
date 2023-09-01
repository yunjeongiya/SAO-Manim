from manim import *
from consts import *
from utils import *
import math

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    copies = VGroup(TEXTS[1][1], TEXTS[1][3]).copy().scale(1.3).shift(RIGHT*5, DOWN*0.5)
    scene.play(TransformFromCopy(VGroup(TEXTS[1][1], TEXTS[1][3]), copies))
    #3
    tForGreen = ValueTracker(0)
    scene.add(tForGreen)
    graphDict = BasicGraphDict(
        xrange = [-1, 5],
        yrange = [-1, 5],
    ).scale(0.8).next_to(copies, DOWN)
    greenGraphLabel = MathTex(r"y={{t}}-\log_2 x").scale(TEX_SCALE*1.3).move_to(copies[0], aligned_edge=LEFT)
    tempGraphLabel = MathTex(r"{{y=}}-\log_2 x").scale(TEX_SCALE*1.3).move_to(copies[0], aligned_edge=LEFT)
    scene.remove(copies[0])
    scene.play(Create(graphDict), FadeOut(copies[1]),
               TransformMatchingTex(greenGraphLabel, tempGraphLabel))
    
    #make window for graph
    scene.add(Difference(Rectangle(BLACK, 10, 15), Square(graphDict.height).move_to(graphDict), fill_color=BLACK, fill_opacity=1, stroke_width=0).set_z_index(-1))
    
    graphDict["greenGraph"] = always_redraw(lambda: graphDict["ax"].plot(lambda x: tForGreen.get_value()-math.log(x, 2) if x>0 else 0, [0.05,5])
                                            .set_color(PURE_GREEN).set_z_index(-2))
    graphDict.buildDotOnAxLabel(1)
    graphDict["lineOn1"] = always_redraw(lambda: DashedLine(graphDict["ax"].c2p(1, 0),
                                                            graphDict["ax"].i2gp(1, graphDict["greenGraph"]),
                                                            stroke_width=2))
    scene.play(FadeToColor(tempGraphLabel, PURE_GREEN),
               Create(graphDict["greenGraph"]),
               Write(graphDict["labelOn1"]))
    #4
    scene.play(TransformMatchingTex(tempGraphLabel, greenGraphLabel.set_color(PURE_GREEN)))
    graphDict["yEqualsT"] = VGroup(always_redraw(lambda: Line(graphDict["ax"].c2p(-1, tForGreen.get_value()), graphDict["ax"].c2p(5,tForGreen.get_value()), stroke_width=2)))
    graphDict["yEqualsT"].add(MathTex("y=t").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio)
                              .add_updater(lambda m: m.next_to(graphDict["yEqualsT"][0])))
    graphDict.buildDotOnAxLabel(tForGreen, isOnX=False, label="$t$", labelKey="labelOnYt")
    scene.play(tForGreen.animate.set_value(3))
    #5
    violetGraphLabel = MathTex(r"y=2^{x {{-t}} }", color=VIOLET).scale(TEX_SCALE*1.3).move_to(copies[1], aligned_edge=DL)
    tempGraphLabel = MathTex(r"y=2^{x}", color=VIOLET).scale(TEX_SCALE*1.3).move_to(copies[1], aligned_edge=DL)
    scene.play(Write(tempGraphLabel))
    tForViolet = ValueTracker(0)
    graphDict["violetGraph"] = always_redraw(lambda: graphDict["ax"].plot(lambda x: 2**(x-tForViolet.get_value()))
                                             .set_color(VIOLET).set_z_index(-2))
    graphDict.buildDotOnAxLabel(1, isOnX=False, labelKey="labelOnY1")
    graphDict["lineOnY1"] = always_redraw(lambda: DashedLine(graphDict["ax"].c2p(0, 1),
                                                             graphDict["ax"].c2p(tForViolet.get_value(), 1),
                                                             stroke_width=2))
    scene.play(Create(graphDict["violetGraph"]), Write(graphDict["labelOnY1"]))
    #6
    scene.play(FadeIn(violetGraphLabel), FadeOut(tempGraphLabel))
    graphDict["xEqualsT"] = VGroup(always_redraw(lambda: Line(graphDict["ax"].c2p(tForViolet.get_value(), -1), graphDict["ax"].c2p(tForViolet.get_value(), 5), stroke_width=2)))
    graphDict["xEqualsT"].add(MathTex("x=t").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio)
                              .add_updater(lambda m: m.next_to(graphDict["xEqualsT"][0], DOWN)))
    graphDict.buildDotOnAxLabel(tForViolet, label="$t$", labelKey="labelOnt")
    scene.play(tForViolet.animate.set_value(3))
    #7
    scene.play(tForViolet.animate.set_value(4))
    #8
    scene.play(tForGreen.animate.set_value(4))
    #9
    scene.play(tForGreen.animate.set_value(3),
               tForViolet.animate.set_value(3))
    #10
    toExpand = VGroup(graphDict["ax"], graphDict["greenGraph"], graphDict["violetGraph"],
                      DashedLine(graphDict["ax"].c2p(tForViolet.get_value(), 0),
                                 graphDict["ax"].i2gp(tForViolet.get_value(), graphDict["violetGraph"])),
                      graphDict["lineOnY1"].clear_updaters())
    toRemain = VGroup(graphDict["labelOnt"])
    scene.remove(graphDict)
    scene.add(toExpand, toRemain)
    scene.play(toExpand.set_z_index(-2)
               .animate.scale(2, about_point=graphDict["ax"].c2p(3,-1)),
               toRemain.animate.scale(2),
               graphDict["labelOnY1"].clear_updaters().animate.scale(1.8, about_point=graphDict["ax"].c2p(3,-1)).shift(RIGHT*1.3+UP*0.6).set_z_index(1))
    #11
    scene.play(tForGreen.animate.set_value(1.7))
    #12
    scene.play(FadeOut(toRemain, toExpand, greenGraphLabel, violetGraphLabel, graphDict["labelOnY1"]))
    graphDict = BasicGraphDict(xrange=[-1,3.5,1], yrange=[-1.5,2.5,1], texScaleRatio=0.5).scale(1.1).next_to(TEXTS, buff=0)
    scene.play(Create(graphDict))
    graphDict.buildGraph(lambda t: math.log(t, 2), labelTex=r"$y=\log_2 t$", xRange=[1/4,3.5], graphKey="logGraph", graphLabelKey="logGraphLabel")
    scene.play(Create(graphDict["logGraph"]), Write(graphDict["logGraphLabel"].shift(DOWN*0.5)))
    scene.play(Write(graphDict.buildDotOnAxLabel(2)),
               Write(graphDict.buildDotOnAxLabel(1, isOnX=False)),
               Create(DashedLine(graphDict["ax"].c2p(2,1), graphDict["ax"].c2p(0,1), stroke_width=2)),
               Create(DashedLine(graphDict["ax"].c2p(2,1), graphDict["ax"].c2p(2,0), stroke_width=2)))
    graphDict.buildGraph(lambda t: t-1, r"$y=t-1$", graphKey="lineGraph", graphLabelKey="lineGraphLabel")
    scene.play(Create(graphDict["lineGraph"]), Write(graphDict["lineGraphLabel"].shift(UP*0.3)))
