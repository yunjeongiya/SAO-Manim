from manim import *
from consts import *
from utils import *
import scipy.stats as stats

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    xDistribution = MathTex(r"X \sim N({{8}}, {{1.2}}^2)").scale(TEX_SCALE).to_corner(UL)
    probability = TEXTS[5].copy().next_to(xDistribution, buff=3)
    scene.play(FadeOut(TEXTS[:2], TEXTS[3:]),
               TransformMatchingShapes(TEXTS[2], xDistribution),
               TransformFromCopy(TEXTS[5], probability))
    scene.add(probability)
    #3
    xBarDistribution = MathTex(r"\overline{X} {{\sim N\left(}} 8{{,}} { \left( { {{1.2}} \over \sqrt{n} } \right) }^2 {{\right)}}").scale(TEX_SCALE).next_to(xDistribution, DOWN, aligned_edge=LEFT)
    scene.play(TransformFromCopy(probability[3], xBarDistribution[0]))
    scene.play(FadeIn(xBarDistribution[1], xBarDistribution[3], xBarDistribution[-1]))
    scene.play(TransformFromCopy(xDistribution[1], xBarDistribution[2]))
    scene.play(TransformFromCopy(xDistribution[3], xBarDistribution[5]))
    scene.play(FadeIn(xBarDistribution[4], xBarDistribution[6]))
    #4
    graphDict = BasicGraphDict(
        xrange = [8-0.5, 8+0.5, 1],
        xLengthRatio=5.2, yLengthRatio=1.2,
        xLabelTex=r"$\overline{X}$",
        hideYAxis=True,
        func = lambda x: stats.norm.pdf(x, 8, 1.2/(N**0.5)),
        texScaleRatio=0.15
    ).shift(DR*1.5)
    scene.play(Create(graphDict))
    graphDict["lineOn8.24"] = Line(graphDict["ax"].c2p(8.24,0),
                                   graphDict["ax"].i2gp(8.24, graphDict["graph"]),
                                   stroke_width=2)
    scene.play(TransformFromCopy(xBarDistribution[2], graphDict.buildDotOnAxLabel(8, buff=0.1)),
               TransformFromCopy(probability[5], graphDict.buildDotOnAxLabel(8.24, buff=0.1)),
               Create(graphDict["lineOn8.24"]))
    graphDict["lineOn8"] = Line(graphDict["ax"].c2p(8,0),
                                graphDict["ax"].i2gp(8, graphDict["graph"]),
                                stroke_width=2)
    scene.play(Create(graphDict["lineOn8"]))
    graphDict["lineOn7.76"] = Line(graphDict["ax"].c2p(7.76,0),
                                   graphDict["ax"].i2gp(7.76, graphDict["graph"]),
                                   stroke_width=2)
    scene.play(TransformFromCopy(probability[1], graphDict.buildDotOnAxLabel(7.76, buff=0.1)),
               Create(graphDict["lineOn7.76"]))
    graphDict["dashedLine"] = DashedLine(graphDict["ax"].i2gp(7.76, graphDict["graph"]),
                                         graphDict["ax"].i2gp(8.24, graphDict["graph"]),
                                         stroke_width=2)
    scene.play(Create(graphDict["dashedLine"]))
    graphDict["area"] = graphDict["ax"].get_area(graphDict["graph"], [7.76, 8.24], opacity=0.5, color=YELLOW, stroke_width=0)
    scene.play(FadeIn(graphDict["area"]))
    #5
    scene.play(graphDict.animate.shift(UP*2))
    graphDict2 = BasicGraphDict(
        xrange = [0-0.5, 0+0.5, 1],
        xLengthRatio=5.2, yLengthRatio=1.2,
        xLabelTex="$Z$",
        hideYAxis=True,
        func = lambda x: stats.norm.pdf(x, 0, 1.2/(N**0.5)),
        texScaleRatio=0.15
    ).move_to(graphDict)
    xLabelTemp = graphDict2["xLabel"]
    graphDict2.remove("xLabel")
    scene.add(graphDict2)
    scene.play(graphDict2.animate.shift(DOWN*3))
    graphDict2["xLabel"] = xLabelTemp.shift(DOWN*3)
    graphDict2["lineOn0"] = Line(graphDict2["ax"].c2p(0,0),
                                 graphDict2["ax"].i2gp(0, graphDict2["graph"]),
                                 stroke_width=2)
    scene.play(Write(graphDict2["xLabel"]),
               Create(graphDict2["lineOn0"]),
               Write(graphDict2.buildDotOnAxLabel(0, buff=0.1)))
    graphDict2["lineOn0.24"] = Line(graphDict2["ax"].i2gp(0.24, graphDict2["graph"]),
                                    graphDict2["ax"].c2p(0.24,0),
                                    stroke_width=2)
    graphDict2["lineOn-0.24"] = Line(graphDict2["ax"].i2gp(-0.24, graphDict2["graph"]),
                                     graphDict2["ax"].c2p(-0.24,0),
                                     stroke_width=2)
    scene.play(Create(graphDict2["lineOn0.24"]), Create(graphDict2["lineOn-0.24"]),
               Write(graphDict2.buildDotOnAxLabel(0.24, label=r"$\sqrt{n} \over 5$", buff=0.1)),
               Write(graphDict2.buildDotOnAxLabel(-0.24, label=r"$-{\sqrt{n} \over 5}$", buff=0.1)))
    graphDict2["area"] = graphDict2["ax"].get_area(graphDict2["graph"], [-0.24, 0.24], opacity=0.5, color=YELLOW, stroke_width=0)
    scene.play(FadeIn(graphDict2["area"]))
    #6
    scene.play(FadeOut(graphDict, probability, xDistribution, xBarDistribution),
               FadeIn(TEXTS.scale(0.8).to_corner(UL), shift=RIGHT),
               graphDict2.animate.shift(RIGHT*2))
    #7
    graphDict2["lineOn-0.1"] = Line(graphDict2["ax"].c2p(-0.1,0),
                                graphDict2["ax"].i2gp(-0.1, graphDict2["graph"]),
                                stroke_width=2)
    graphDict2["lineOn0.1"] = Line(graphDict2["ax"].c2p(0.1,0),
                                graphDict2["ax"].i2gp(0.1, graphDict2["graph"]),
                                stroke_width=2)
    scene.play(Create(graphDict2["lineOn-0.1"]), Create(graphDict2["lineOn0.1"]),
               Write(graphDict2.buildDotOnAxLabel(-0.1, label="-1", buff=0.1)),
               Write(graphDict2.buildDotOnAxLabel(0.1, label="1", buff=0.1)))
    scene.play(FadeOut(graphDict2["area"]),
               FadeToColor(VGroup(graphDict2["lineOn-0.1"], graphDict2["lineOn0.1"],
                                  graphDict2["labelOn-0.1"], graphDict2["labelOn0.1"]),
                           PURE_GREEN),
               FadeIn(graphDict2["ax"].get_area(graphDict2["graph"], [-0.1, 0.1], opacity=0.5, color=PURE_GREEN, stroke_width=0)))