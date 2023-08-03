from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)

def analyzeGraph(scene: Scene):
    #2
    scene.play(FadeOut(TEXTS), TEXTS[2].animate.to_edge(UP), TEXTS[4].animate.shift(UP*1.5))
    scene.add(TEXTS[2], TEXTS[4])
    #3
    inequation = MathTex("x^3 -3x^2 -9x \geq k-30").scale(TEX_SCALE).move_to(TEXTS[4], aligned_edge=LEFT)
    scene.play(ReplacementTransform(TEXTS[4], inequation))
    primeFunc = lambda x: (3*(x**2)-6*x-9)
    primeGraphDict = BasicGraphDict(xrange=[XSTART,XEND],
                                    yLengthRatio=0.1, hideYAxis=True,
                                    func=primeFunc, graphXRange=[XSTART+1, XEND-1]).scale(TEX_SCALE).to_corner(UR)
    pointOnMinus1 = primeGraphDict["ax"].c2p(LOCAL_MAX_XVAL,0)
    pointOn3 = primeGraphDict["ax"].c2p(LOCAL_MIN_XVAL,0)
    verticalLineOnMinus1 = DashedLine(pointOnMinus1+DOWN*4, pointOnMinus1+UP)
    verticalLineOn3 = DashedLine(pointOn3+DOWN*4, pointOn3+UP)
    labelMinus1 = MathTex(f"{LOCAL_MAX_XVAL}").scale(TEX_SCALE).next_to(verticalLineOnMinus1, DOWN, buff=0.1)
    label3 = MathTex(f"{LOCAL_MIN_XVAL}").scale(TEX_SCALE).next_to(verticalLineOn3, DOWN, buff=0.1)
    scene.play(Create(verticalLineOnMinus1), Create(verticalLineOn3), Write(labelMinus1), Write(label3))
    scene.play(Create(primeGraphDict))
    #4
    fluctuation = VGroup(
        MathTex("+").set_color(MINT).next_to(pointOnMinus1, UL),
        MathTex("-").set_color(PINK).next_to(pointOnMinus1, DR),
        MathTex("-").set_color(PINK).next_to(pointOn3, DL),
        MathTex("+").set_color(MINT).next_to(pointOn3, UR)
    )
    scene.play(FadeIn(fluctuation), run_time=2)
    func = lambda x: x**3-3*(x**2)-9*x
    graphDict = BasicGraphDict(xrange=[XSTART,XEND], yLengthRatio=0.1, 
                               hideXAxis=True, hideYAxis=True,
                               func = func).scale(TEX_SCALE).next_to(primeGraphDict, DOWN, aligned_edge=LEFT)
    scene.play(Create(graphDict))
    #5
    scene.play(FadeOut(TEXTS[2], fluctuation, primeGraphDict),
               inequation.animate.to_edge(UP), FadeIn(TEXTS[-2:].shift(UP*2)),
               graphDict.animate.to_edge(UP))
    #6
    greenLines = VGroup(
        Line(graphDict["ax"].c2p(XSTART,func(LOCAL_MAX_XVAL)), graphDict["ax"].c2p(XEND, func(LOCAL_MAX_XVAL))),
        Line(graphDict["ax"].c2p(XSTART,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p(XEND, func(LOCAL_MIN_XVAL)))
    ).set_color(PURE_GREEN)
    mintLines = VGroup(
        Line(graphDict["ax"].c2p(XSTART,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p(XSTART, func(LOCAL_MAX_XVAL))),
        Line(graphDict["ax"].c2p(LOCAL_MAX_XVAL,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p(LOCAL_MAX_XVAL, func(LOCAL_MAX_XVAL))),
        Line(graphDict["ax"].c2p((LOCAL_MIN_XVAL+LOCAL_MAX_XVAL)/2,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p((LOCAL_MIN_XVAL+LOCAL_MAX_XVAL)/2, func(LOCAL_MAX_XVAL))),
        Line(graphDict["ax"].c2p(LOCAL_MIN_XVAL,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p(LOCAL_MIN_XVAL, func(LOCAL_MAX_XVAL))),
        Line(graphDict["ax"].c2p(XEND,func(LOCAL_MIN_XVAL)), graphDict["ax"].c2p(XEND, func(LOCAL_MAX_XVAL))),
    ).set_color(MINT)
    scene.play(FadeIn(greenLines))
    scene.play(FadeIn(mintLines))
    #7
    verticalLineOn1 = DashedLine(primeGraphDict["ax"].c2p(1,0)+DOWN*4, graphDict["ax"].i2gp(1, graphDict["graph"]))
    verticalLineOn5 = DashedLine(primeGraphDict["ax"].c2p(5,0)+DOWN*4, graphDict["ax"].i2gp(5, graphDict["graph"]))
    label1 = MathTex("1").scale(TEX_SCALE).next_to(verticalLineOn1, DOWN, buff=0.1)
    label5 = MathTex("5").scale(TEX_SCALE).next_to(verticalLineOn5, DOWN, buff=0.1)
    scene.play(Create(verticalLineOn1), Write(label1))
    scene.play(Create(verticalLineOn5), Write(label5))
    #8
    verticalLineOnMinus1.become(DashedLine(primeGraphDict["ax"].c2p(LOCAL_MAX_XVAL,0)+DOWN*4, graphDict["ax"].i2gp(LOCAL_MAX_XVAL, graphDict["graph"])))
    verticalLineOn3.become(DashedLine(primeGraphDict["ax"].c2p(LOCAL_MIN_XVAL,0)+DOWN*4, graphDict["ax"].i2gp(LOCAL_MIN_XVAL, graphDict["graph"])))
    scene.play(FadeOut(greenLines, mintLines))
    verticalLineOn4 = DashedLine(primeGraphDict["ax"].c2p(4,0)+DOWN*4, graphDict["ax"].i2gp(4, graphDict["graph"]))
    label4 = MathTex("4").scale(TEX_SCALE).next_to(verticalLineOn4, DOWN, buff=0.1)
    scene.play(Create(verticalLineOn4), Write(label4))
    #9
    scene.play(FadeOut(verticalLineOn5, label5, graphDict["graph"]),
               FadeIn(graphDict.buildGraph(func, xRange=[-1, 4], graphKey="partialGraph")))
    graphDict["graph"] = graphDict["partialGraph"]
    graphDict.remove("partialGraph")
    scene.play(FadeToColor(graphDict["graph"], YELLOW))
    #10
    line = Line(graphDict["ax"].c2p(XSTART,-50), graphDict["ax"].c2p(XEND,-50))
    kMinus10Tex = MathTex("k-30").scale(TEX_SCALE).next_to(line, LEFT, buff=0.1)
    kMinus10Group = VGroup(line, kMinus10Tex).set_color(MINT)
    scene.play(Create(line), Write(kMinus10Tex))
    scene.play(kMinus10Group.animate.shift(UP))
    scene.play(kMinus10Group.animate.shift(DOWN*2))
    scene.play(kMinus10Group.animate.shift(UP))
    #11
    line2 = Line(graphDict["ax"].c2p(XSTART,func(LOCAL_MIN_XVAL)), graphDict["ax"].i2gp(LOCAL_MIN_XVAL, graphDict["graph"]), color=VIOLET)
    h3Tex = MathTex("h(3)", color=VIOLET).scale(TEX_SCALE).next_to(line2, LEFT, buff=0.1)
    scene.play(Write(h3Tex), Create(line2))
