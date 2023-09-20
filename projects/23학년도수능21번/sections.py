from manim import *
from consts import *
from utils import *
import math

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    XSTART = -6
    XEND = 6
    YSTART = -5
    YEND = 10
    graphDict = BasicGraphDict( [XSTART, XEND], [YSTART, YEND], texScaleRatio=1.5, hideXAxis=True ).scale(0.38).next_to(TEXTS, aligned_edge=UP)
    graphDict["fakeXAx"] = Arrow(graphDict["ax"].c2p(XSTART, 0),
                                 graphDict["ax"].c2p(XEND, 0),
                                 max_tip_length_to_length_ratio=0.02,
                                 stroke_width=2, buff=0)
    graphDict["xLabel"] = MathTex("x").scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).next_to(graphDict["ax"].c2p(XEND, 0), buff=0.1)
    graphDict["yLabel"].shift(UP*1.4+RIGHT*0.2)
    graphDict.buildDotOnAxLabel(1, isOnX=False, buff=-0.4)
    graphDict.buildDotOnAxLabel(0, isOnX=False, buff=0.3)
    graphDict.buildGraph(lambda x: 3**x, xRange=[XSTART, 0], graphKey="leftGraph").set_color(PURE_GREEN)
    threePowerx = MathTex("3^x", color=PURE_GREEN).scale(TEX_SCALE).move_to(TEXTS[2][1][0][1], aligned_edge=LEFT).shift(DOWN*0.02)
    scene.play(FadeIn(threePowerx), Create(graphDict))
    #3
    graphDict.buildDotOnAxLabel(9, isOnX=False, buff=-0.4)
    scene.play(FadeToColor(TEXTS[2][1][0][1], PURE_GREEN),
               Transform(graphDict["leftGraph"], graphDict["ax"].plot(lambda x:3**(x+2), [XSTART, 0]).set_color(PURE_GREEN)),
               FadeOut(graphDict["labelOnY1"]), FadeIn(graphDict["labelOnY9"]))
    graphDict.remove("labelOnY1")
    #4
    graphDict.buildGraph(lambda x: math.log(x, 2), xRange=[0.1, XEND, 0.001], graphKey="rightGraph").set_color(VIOLET)
    graphDict.buildDotOnAxLabel(1)
    log2x = MathTex(r"\log_2\: x", color=VIOLET).scale(TEX_SCALE).move_to(TEXTS[2][1][1][1], aligned_edge=LEFT).shift(DOWN*0.01)
    scene.play(FadeIn(log2x), Create(graphDict["rightGraph"]), Write(graphDict["labelOn1"]))
    #5
    graphDict.buildDotOnAxLabel(2, isOnX=False)
    scene.play(FadeToColor(TEXTS[2][1][1][1], VIOLET),
               Transform(graphDict["rightGraph"], graphDict["ax"].plot(lambda x:math.log(x+4, 2), [0, XEND, 0.001]).set_color(VIOLET)),
               FadeIn(graphDict["labelOnY2"]), graphDict["labelOn1"].animate.set_opacity(0))
    graphDictCopy = graphDict.copy()
    graphDictCopy["leftGraph"].set_color(WHITE)
    graphDictCopy["rightGraph"].set_color(WHITE)
    #6
    n = 2.7
    graphDict.buildLine("lineYN", [XSTART, n], [XEND, n], color=YELLOW)
    graphDict["YNLabel"] = MathTex("y=n", color=YELLOW).scale(0.5).next_to(graphDict["lineYN"], buff=0.1)
    scene.play(FadeToColor(VGroup(TEXTS[2][1][0][1], TEXTS[2][1][1][1],
                                  graphDict["leftGraph"], graphDict["rightGraph"]), WHITE),
               FadeOut(log2x, threePowerx),
               FadeToColor(VGroup(TEXTS[2][1][0][2], TEXTS[2][1][1][2]), YELLOW),
               Create(graphDict["lineYN"]), Write(graphDict["YNLabel"]))
    #7
    newLabelOnY9 = MathTex("9{{-}}n").set_color_by_tex("n", YELLOW).scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["labelOnY9"], aligned_edge=LEFT)
    newLabelOnY2 = MathTex("2{{-}}n").set_color_by_tex("n", YELLOW).scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["labelOnY2"], aligned_edge=RIGHT)
    scene.play(TransformMatchingTex(graphDict["labelOnY9"], newLabelOnY9),
               TransformMatchingTex(graphDict["labelOnY2"], newLabelOnY2),
               Transform(graphDict["fakeXAx"], Arrow(graphDict["ax"].c2p(XSTART, n),
                               graphDict["ax"].c2p(XEND, n),
                               max_tip_length_to_length_ratio=0.02,
                               stroke_width=2, buff=0).set_color(YELLOW)),
               graphDict["xLabel"].animate.set_color(YELLOW).next_to(graphDict["ax"].c2p(XEND, n), buff=0.1),
               VGroup(graphDict["lineYN"], graphDict["YNLabel"], graphDict["labelOnY0"]).animate.set_opacity(0))
    graphDict["labelOnY9"] = newLabelOnY9
    graphDict["labelOnY2"] = newLabelOnY2
    #8
    absGroup = VGroup(VGroup(TEXTS[2][1][0][0], TEXTS[2][1][0][-1]).copy().set_color(PURE_GREEN), 
    VGroup(TEXTS[2][1][1][0], TEXTS[2][1][1][-1]).copy().set_color(VIOLET))
    absGroup.add(absGroup.copy().shift(RIGHT*0.01))
    scene.play(FadeToColor(VGroup(TEXTS[2][1][0][2], TEXTS[2][1][1][2]), WHITE),
               FadeIn(absGroup),
               FadeToColor(VGroup(graphDict["labelOnY9"], graphDict["labelOnY2"], graphDict["fakeXAx"], graphDict["xLabel"]), WHITE),
               Transform(graphDict["leftGraph"], graphDict["ax"].plot(lambda x:abs(3**(x+2)-n)+n, [XSTART, 0, 0.001]).set_color(PURE_GREEN)), #그림 상으로 x축이 위로 올라와있어서 그래프 접어올린 후에 다시 올려야 맞음
               Transform(graphDict["rightGraph"], graphDict["ax"].plot(lambda x:abs(math.log(x+4, 2)-n)+n, [0, XEND, 0.001]).set_color(VIOLET)),
               )
    #9
    t = 3
    graphDict.buildLine("lineYT", [XSTART, t], [XEND, t], color=MINT)
    graphDict["YTLabel"] = MathTex("y=t", color=MINT).scale(0.5).next_to(graphDict["lineYT"], buff=0.1)
    ul = Underline(TEXTS[3][1], color=MINT, stroke_width=2)
    scene.play(Create(ul), Create(graphDict["lineYT"]), Write(graphDict["YTLabel"]))
    #10
    scene.play(FadeToColor(TEXTS, WHITE), FadeOut(absGroup, graphDict, ul), FadeIn(graphDictCopy))
    scene.next_section(skip_animations=True)