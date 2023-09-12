from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    XSTART = -2
    XEND = 2
    YSTART = -3.5
    YEND = 2.5
    graphDict = BasicGraphDict(
        [XSTART, XEND], [YSTART, YEND],
        texScaleRatio=0.6,
        hideYAxis=True,
    ).next_to(TEXTS).shift(DOWN*1.3+RIGHT*0.5)
    graphDict.buildLine("lineOn-1", [-1, YSTART+0.3], [-1, YEND], isDashedLine=True)
    graphDict.buildLine("lineOn1/3", [1/3, YSTART+0.3], [1/3, YEND], isDashedLine=True)
    graphDict.buildDotOnAxLabel(-1, buff=-YSTART-0.2)
    graphDict.buildDotOnAxLabel(1/3, r"$\dfrac{1}{3}$", buff=-YSTART-0.1, labelKey="labelOn1/3")
    scene.play(Create(graphDict["lineOn-1"]), Write(graphDict["labelOn-1"]),
               Create(graphDict["lineOn1/3"]), Write(graphDict["labelOn1/3"]))
    scene.play(Create(graphDict["ax"]), Write(graphDict["xLabel"]))
    buff = 0.3
    graphDict.buildGraph(lambda x: 3*x**2+2*x-1, xRange=[-1-buff, 1/3+buff], 
                         graphKey="primeGraph")
    scene.play(Create(graphDict["primeGraph"]))
    #3
    midPoint = (-1+1/3)/2
    buff = 1.6
    graphDict.buildGraph(lambda x: x**3+x**2-x, xRange=[midPoint-buff, midPoint+buff])
    scene.play(Create(graphDict["graph"].shift(DOWN*3)))
    #4
    scene.play(graphDict["graph"].animate.shift(UP*3),
               FadeOut(graphDict["primeGraph"], graphDict["ax"], graphDict["xLabel"]))
    #5
    graphDict.buildLine("yArrow", [0, YSTART], [0, YEND], isArrow=True,
                        max_tip_length_to_length_ratio=0.03)
    graphDict.buildDotOnAxLabel(YEND-0.3, "$y$", isOnX=False, labelKey="yLabel")
    scene.play(Create(graphDict["yArrow"]), Write(graphDict["yLabel"]))
    scene.play(Create(graphDict["ax"]), Write(graphDict["xLabel"]))
    graphDict.buildDotOnAxLabel(0, r"$\rm O$").shift(LEFT*0.2)
    scene.play(Write(graphDict["labelOn0"]))
    #6
    graphDict.buildGraph(lambda x: 4*x, xRange=[YSTART/4, YEND/4], graphKey="gx").set_color(PURE_GREEN)
    scene.play(FadeOut(graphDict["lineOn-1"], graphDict["labelOn-1"],
                       graphDict["lineOn1/3"], graphDict["labelOn1/3"]),
               Create(graphDict["gx"]))
    scene.play(Transform(graphDict["gx"], graphDict["ax"].plot(lambda x: 4*abs(x), [-YEND/4, YEND/4, 0.001]).set_color(PURE_GREEN)))
    #7
    graphDict.buildDotOnAxLabel(-3, MathTex("k", color=PURE_GREEN), isOnX=False, labelKey="labelOnYk")
    scene.play(FadeIn(graphDict["labelOnYk"]),
               Transform(graphDict["gx"],
                         graphDict["ax"].plot(lambda x: 4*abs(x)-3, [-(YEND+3)/4, (YEND+3)/4, 0.001]).set_color(PURE_GREEN)))
    #8
    graphDict.buildDotOnAxLabel(1)
    graphDict.buildDotOnAxLabel(1, isOnX=False)
    graphDict["linesTo(1,1)"] = VGroup(
        graphDict["ax"].get_vertical_line(graphDict["ax"].c2p(1,1)),
        graphDict["ax"].get_horizontal_line(graphDict["ax"].c2p(1,1)).flip()
    )
    scene.play(Write(graphDict["labelOn1"]), Write(graphDict["labelOnY1"]),
               Create(graphDict["linesTo(1,1)"]))
    graphDict["linesTo(-1,1)"] = VGroup(
        graphDict["ax"].get_vertical_line(graphDict["ax"].c2p(-1,1)),
        graphDict["ax"].get_horizontal_line(graphDict["ax"].c2p(-1,1)).flip()
    )
    graphDict.buildDotOnAxLabel(-1)
    scene.play(Write(graphDict["labelOn-1"]),
               Create(graphDict["linesTo(-1,1)"]))
    #9
    graphDict.buildGraph(lambda x:4*x-3, xRange=[0, (YEND+3)/4], graphKey="gx").set_color(PURE_GREEN)
    graphDict.buildGraph(lambda x:-4*x-3, xRange=[-(YEND+3)/4, 0], graphKey="MINTGx").set_color(MINT)
    scene.play(FadeIn(graphDict["MINTGx"]))
    leftArea = graphDict["ax"].get_area(graphDict["graph"], bounded_graph=graphDict["MINTGx"], x_range=[-1, 0],
                                        color=MINT, opacity=0.5)
    rightArea = graphDict["ax"].get_area(graphDict["graph"], bounded_graph=graphDict["gx"], x_range=[0, 1],
                                        color=PURE_GREEN, opacity=0.5)
    scene.play(FadeIn(leftArea, rightArea))