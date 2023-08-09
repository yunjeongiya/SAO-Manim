from manim import *
from consts import *
from utils import *
import scipy.stats as stats

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
def findMByGraph(scene: Scene):
    #2,3
    distribution = MathTex("{{X}} \sim N({{m}}, {{5}}^2)").scale(TEX_SCALE).to_corner(UL)
    scene.play(FadeOut(TEXTS[0], TEXTS[2:]),
               TransformMatchingShapes(TEXTS[1], distribution),
               CONDITIONS.animate.shift(UP))
    scene.add(CONDITIONS)
    #4
    graphDict1 = BasicGraphDict(
        xrange = [M-15, M+15, 1],
        xLengthRatio=0.2, yLengthRatio=30,
        hideYAxis=True,
        func = lambda x: stats.norm.pdf(x, M, 5),
        texScaleRatio=3
    )
    graphDict1.buildDotOnAxLabel(M, "$m$", buff=0.005, labelKey="labelOnM")
    graphDict1["lineOnM"] = Line(graphDict1["ax"].i2gp(M, graphDict1["graph"]),
                                graphDict1["ax"].c2p(M,0),
                                stroke_width=2)
    wrongM = 8.5
    graphDict2 = BasicGraphDict(
        xrange = [wrongM-15, wrongM+15, 1],
        xLengthRatio=0.2, yLengthRatio=30,
        hideYAxis=True,
        func = lambda x: stats.norm.pdf(x, wrongM, 5),
        texScaleRatio=3
    )
    graphDict2.buildDotOnAxLabel(wrongM, "$m$", buff=0.005, labelKey="labelOnM")
    graphDict2["lineOnM"] = Line(graphDict2["ax"].i2gp(wrongM, graphDict2["graph"]),
                                graphDict2["ax"].c2p(wrongM,0),
                                stroke_width=2)
    VGroup(graphDict1, graphDict2).arrange().shift(DOWN*1.3)
    scene.play(Create(graphDict1))
    graphDict1["lineOn10"] = Line(graphDict1["ax"].c2p(10,0),
                                  graphDict1["ax"].i2gp(10, graphDict1["graph"]),
                                  stroke_width=2, color=PURE_GREEN)
    scene.play(Create(graphDict1["lineOn10"]),
               Write(graphDict1.buildDotOnAxLabel(10, buff=0.005).set_color(PURE_GREEN)))
    #5
    graphDict1["verticalLineFrom10"] = DashedLine(
        graphDict1["ax"].i2gp(10, graphDict1["graph"]),
        graphDict1["ax"].i2gp(M+(M-10), graphDict1["graph"]),
        stroke_width=2
    )
    lineTemp = Line(graphDict1["ax"].i2gp(M+(M-10), graphDict1["graph"]),
                    graphDict1["ax"].c2p(M+(M-10),0),
                    stroke_width=2)
    scene.play(Create(graphDict1["verticalLineFrom10"]))
    scene.play(Create(lineTemp))
    #6
    toBe20 = ValueTracker(M+(M-10))
    graphDict1["lineOn20"] = always_redraw(lambda: Line(
        graphDict1["ax"].i2gp(toBe20.get_value(), graphDict1["graph"]),
        graphDict1["ax"].c2p(toBe20.get_value(),0), 
        stroke_width=2, color = MINT
    ).set_z_index(-1))
    scene.play(toBe20.animate.set_value(20))
    scene.play(Write(graphDict1.buildDotOnAxLabel(20, buff=0.005).set_color(MINT)),
               FadeOut(lineTemp))
    #7
    numbers = VGroup(Tex("①").next_to(graphDict1, UL),
                     Tex("②").next_to(graphDict2, UL))
    scene.play(Write(numbers), Create(graphDict2))
    graphDict2["lineOn10"] = Line(graphDict2["ax"].c2p(10,0),
                                    graphDict2["ax"].i2gp(10, graphDict2["graph"]),
                                    stroke_width=2, color=PURE_GREEN)
    scene.play(Create(graphDict2["lineOn10"]),
               Write(graphDict2.buildDotOnAxLabel(10, buff=0.005).set_color(PURE_GREEN)))
    toBe20_2 = ValueTracker(10)
    graphDict2["lineOn20"] = always_redraw(lambda: Line(
        graphDict2["ax"].i2gp(toBe20_2.get_value(), graphDict2["graph"]),
        graphDict2["ax"].c2p(toBe20_2.get_value(),0),
        stroke_width=2, color = MINT
    ).set_z_index(-1))
    scene.play(toBe20_2.animate.set_value(20))
    scene.play(Write(graphDict2.buildDotOnAxLabel(20, buff=0.005).set_color(MINT)))
    #8
    graphDict1["lineOn4"] = Line(graphDict1["ax"].c2p(4,0),
                                graphDict1["ax"].i2gp(4, graphDict1["graph"]),
                                stroke_width=2, color=YELLOW)
    scene.play(Create(graphDict1["lineOn4"]),
                Write(graphDict1.buildDotOnAxLabel(4, buff=0.005).set_color(YELLOW)))
    graphDict1["verticalLineFrom4"] = DashedLine(
        graphDict1["ax"].i2gp(4, graphDict1["graph"]),
        graphDict1["ax"].i2gp(M+(M-4), graphDict1["graph"]),
        stroke_width=2
    )
    lineTemp = Line(graphDict1["ax"].i2gp(M+(M-4), graphDict1["graph"]),
                    graphDict1["ax"].c2p(M+(M-4),0),
                    stroke_width=2)
    scene.play(Create(graphDict1["verticalLineFrom4"]))
    scene.play(Create(lineTemp))
    toBe22 = ValueTracker(M+(M-4))
    graphDict1["lineOn22"] = always_redraw(lambda: Line(
        graphDict1["ax"].i2gp(toBe22.get_value(), graphDict1["graph"]),
        graphDict1["ax"].c2p(toBe22.get_value(),0),
        stroke_width=2, color = VIOLET
    ).set_z_index(-1))
    scene.play(toBe22.animate.set_value(22))
    scene.play(Write(graphDict1.buildDotOnAxLabel(22, buff=0.005).set_color(VIOLET)),
                FadeOut(lineTemp))
    #9
    graphDict2["lineOn4"] = Line(graphDict2["ax"].c2p(4,0),
                                graphDict2["ax"].i2gp(4, graphDict2["graph"]),
                                stroke_width=2, color=YELLOW)
    scene.play(Create(graphDict2["lineOn4"]),
                Write(graphDict2.buildDotOnAxLabel(4, buff=0.005).set_color(YELLOW)))
    graphDict2["verticalLineFrom4"] = DashedLine(
        graphDict2["ax"].i2gp(4, graphDict2["graph"]),
        graphDict2["ax"].i2gp(wrongM+(wrongM-4), graphDict2["graph"]),
        stroke_width=2
    )
    lineTemp = Line(graphDict2["ax"].i2gp(wrongM+(wrongM-4), graphDict2["graph"]),
                    graphDict2["ax"].c2p(wrongM+(wrongM-4),0),
                    stroke_width=2)
    scene.play(Create(graphDict2["verticalLineFrom4"]))
    scene.play(Create(lineTemp))
    toBe22_2 = ValueTracker(wrongM+(wrongM-4))
    graphDict2["lineOn22"] = always_redraw(lambda: Line(
        graphDict2["ax"].i2gp(toBe22_2.get_value(), graphDict2["graph"]),
        graphDict2["ax"].c2p(toBe22_2.get_value(),0),
        stroke_width=2, color = VIOLET
    ).set_z_index(-1))
    scene.play(toBe22_2.animate.set_value(12))
    scene.play(Write(graphDict2.buildDotOnAxLabel(12, "$22$", buff=0.005).set_color(VIOLET)),
                FadeOut(lineTemp))
    #10
    scene.play(FadeOut(graphDict2))
    scene.play(Transform(distribution[2], MathTex(f"{M}").scale(TEX_SCALE).move_to(distribution[2], aligned_edge=DOWN)))
    
    scene.remove(graphDict1)
    scene.remove(numbers)
    return distribution

def finalAnswer(scene: Scene, distribution):
    #11
    scene.play(FadeIn(TEXTS[:3], TEXTS[4:]),
               CONDITIONS.animate.shift(DOWN),
               distribution.animate.next_to(TABLE, buff=2))
    graphDict = BasicGraphDict(
        xrange = [M-10, M+10, 1],
        xLengthRatio=0.25, yLengthRatio=25,
        hideYAxis=True,
        func = lambda x: stats.norm.pdf(x, M, 5),
        texScaleRatio=2
    )
    graphDict.buildDotOnAxLabel(M, buff=0.005, labelKey="labelOnM")
    graphDict["lineOnM"] = Line(graphDict["ax"].i2gp(M, graphDict["graph"]),
                                graphDict["ax"].c2p(M,0),
                                stroke_width=2)
    graphDict.buildDotOnAxLabel(M, buff=0.005)
    scene.play(Create(graphDict.shift(DOWN*3+RIGHT*4)))
    #12
    graphDict["lineOn17"] = Line(graphDict["ax"].c2p(17,0),
                                graphDict["ax"].i2gp(17, graphDict["graph"]),
                                stroke_width=2)
    graphDict["lineOn18"] = Line(graphDict["ax"].c2p(18,0),
                                graphDict["ax"].i2gp(18, graphDict["graph"]),
                                stroke_width=2)
    scene.play(Create(graphDict["lineOn17"]), Create(graphDict["lineOn18"]),
                Write(graphDict.buildDotOnAxLabel(17, buff=0.005)),
                Write(graphDict.buildDotOnAxLabel(18, buff=0.005)))
    scene.play(FadeIn(graphDict["ax"].get_area(graphDict["graph"], [17, 18], opacity=0.5, color=YELLOW, stroke_width=0)))