from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    scene.next_section()
    #1
    scene.add(TEXTS)

def analyzeGraph(scene:Scene):
    #2
    TEXTS.save_state()
    scene.play(TEXTS.animate.shift(UP*5*TEX_SCALE), FadeOut(OPTIONS))
    #3
    graphDict = BasicGraphDict(
        xrange=[XSTART, XEND, 1], yrange=[YSTART, YEND, 1], y_axis_config={"include_tip": False, "stroke_width": 0},
        texScaleRatio=TEX_SCALE
    ).next_to(BOX, DOWN, aligned_edge=LEFT, buff=0.5)
    graphDict.remove("yLabel")
    scene.play(Create(graphDict))
    scene.play(Write(graphDict.buildDotOnAxLabel(-1)),
               Create(graphDict.buildGraph(lambda x: x+1, xRange=[-2, 0], graphKey="violetGraph1", color=VIOLET)))
    scene.play(Create(graphDict.buildGraph(lambda x: -x-1, xRange=[-2, 0], graphKey="mintGraph1", color=MINT)))
    #4
    graphDict["lineOn3"] = DashedLine(graphDict["ax"].c2p(3, YSTART), graphDict["ax"].c2p(3, YEND))
    graphDict["lineOn5"] = DashedLine(graphDict["ax"].c2p(5, YSTART), graphDict["ax"].c2p(5, YEND))
    scene.play(Write(graphDict.buildDotOnAxLabel(3).shift(LEFT*0.3*TEX_SCALE)), Create(graphDict["lineOn3"]),
               Write(graphDict.buildDotOnAxLabel(5).shift(LEFT*0.3*TEX_SCALE)), Create(graphDict["lineOn5"]))
    #5
    k = ValueTracker(4)
    graphDict["dotOnk"] = Dot(graphDict["ax"].c2p(k.get_value(), 0))
    scene.play(Create(graphDict["dotOnk"]),
               Write(graphDict.buildDotOnAxLabel(k, label=r"$k$")))
    #6
    buff = 0.1
    scene.play(Create(graphDict.buildGraph(lambda x: (x-k.get_value())**2, xRange=[3+buff,5-buff], graphKey="violetGraph2", color=VIOLET)))
    scene.play(Create(graphDict.buildGraph(lambda x: -(x-k.get_value())**2, xRange=[3+buff,5-buff], graphKey="mintGraph2", color=MINT)))
    #7
    violetFunc = lambda x : ((x+1)*(x-k.get_value())**2)*0.1
    scene.play(Transform(graphDict["violetGraph1"], graphDict["ax"].plot(violetFunc, [-2, 0], color=VIOLET)),
               Transform(graphDict["violetGraph2"], graphDict["ax"].plot(violetFunc, [3+buff,5-buff], color=VIOLET)),
               FadeIn(graphDict.buildGraph(violetFunc, graphKey="violetGraph3", color=VIOLET)))
    graphDict.remove("violetGraph1")
    graphDict.remove("violetGraph2")
    #8
    mintFunc = lambda x: -((x+1)*(x-k.get_value())**2)*0.1
    scene.play(Transform(graphDict["mintGraph1"], graphDict["ax"].plot(mintFunc, [-2, 0], color=MINT)),
               Transform(graphDict["mintGraph2"], graphDict["ax"].plot(mintFunc, [3+buff,5-buff], color=MINT)),
               FadeIn(graphDict.buildGraph(mintFunc, graphKey="mintGraph3", color=MINT)))
    graphDict.remove("mintGraph1")
    graphDict.remove("mintGraph2")

    return graphDict

def showAnswer(scene:Scene, graphDict:BasicGraphDict):
    #9
    scene.play(TEXTS.animate.restore(), FadeOut(graphDict))