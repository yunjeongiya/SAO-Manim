from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    fx = MathTex("f(x)=x^2+ax+b")
    gx = MathTex(r"g(x)= \dfrac{1}{3} x^3 + \dfrac{a}{2} x^2 +bx+c")
    VGroup(fx, gx).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).scale(TEX_SCALE).next_to(TEXTS[2])
    scene.play(Write(fx))
    scene.play(Write(gx))
    #3
    case1 = Tex("{{$i)$}} 극값이 존재하{{지 않}}는 경우").scale(0.7).to_corner(UR).shift(LEFT)
    scene.play(Write(case1))
    graphDict = BasicGraphDict(xrange=[0,7,1],
                               hideYAxis=True, yLengthRatio=7/27/2, 
                               func=lambda x: (x-4)**3, graphXRange=[1,7], graphKey="graphWithoutExtreme").scale(0.7).next_to(case1, DOWN).shift(RIGHT*0.3)
    graphDict["lineOn1"] = Line(graphDict["ax"].c2p(1,-27),
                                graphDict["ax"].c2p(1,27), stroke_width=2)
    scene.play(Create(graphDict.buildDotOnAxLabel(1, "$x=1$", buff=27)),
               Create(graphDict["lineOn1"]))
    scene.play(Create(graphDict["graphWithoutExtreme"]))
    graphDict["lineOn4"] = DashedLine(graphDict["ax"].c2p(4,-27),
                                       graphDict["ax"].i2gp(4, graphDict["graphWithoutExtreme"]), color=PURE_GREEN)
    scene.play(Create(graphDict.buildDotOnAxLabel(4, "$x=4$", buff=27).set_color(PURE_GREEN)),
               Create(graphDict["lineOn4"]))
    #4
    case2 = Tex("$i${{$i)$}} 극값이 존재하는 경우").scale(0.7).move_to(case1, aligned_edge=LEFT)
    scene.play(TransformMatchingTex(case1, case2),
               FadeOut(graphDict["graphWithoutExtreme"], graphDict["lineOn4"], graphDict["labelOn4"]))
    funcWithExtreme = lambda x: ((x-4)**2)*(x+2)+10
    scene.play(Create(graphDict.buildGraph(funcWithExtreme, xRange=[2,5.5], graphKey="graphWithExtreme")))
    graphDict["lineOn4"] = DashedLine(graphDict["ax"].c2p(4,-27),
                                         graphDict["ax"].c2p(4, funcWithExtreme(4)), color=PURE_GREEN)
    scene.play(Write(graphDict["labelOn4"]), Create(graphDict["lineOn4"]))
    graphDict["lineOnG(4)"] = DashedLine(graphDict["ax"].c2p(4, funcWithExtreme(4)),
                                        graphDict["ax"].c2p(0.5, funcWithExtreme(4)), color=PURE_GREEN)
    graphDict["labelOnG(4)"] = MathTex("g(4)", color=PURE_GREEN).scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["ax"].c2p(0, funcWithExtreme(4)))
    scene.play(Write(graphDict["labelOnG(4)"]), Create(graphDict["lineOnG(4)"]))
    #5
    scene.play(FadeToColor(VGroup(graphDict["graphWithExtreme"],
                                  graphDict["lineOn4"], graphDict["labelOn4"],
                                  graphDict["lineOnG(4)"], graphDict["labelOnG(4)"]), WHITE),
               Create(graphDict["ax"].set_color(PURE_GREEN)),
               Write(graphDict["xLabel"].set_color(PURE_GREEN)))
    #6
    funcWithExtreme = lambda x: ((x-4)**2)*(x+2)-10
    scene.play(Transform(graphDict["graphWithExtreme"],
                         graphDict["ax"].plot(funcWithExtreme, [2, 5.5])),
               Transform(graphDict["lineOn4"], DashedLine(graphDict["ax"].c2p(4,-27),
                                         graphDict["ax"].c2p(4, funcWithExtreme(4)))),
               Transform(graphDict["lineOnG(4)"], DashedLine(graphDict["ax"].c2p(4, funcWithExtreme(4)),
                                                             graphDict["ax"].c2p(0.5, funcWithExtreme(4)))),
               graphDict["labelOnG(4)"].animate.move_to(graphDict["ax"].c2p(0, funcWithExtreme(4))))
    #7
    funcWithExtreme = lambda x: abs(((x-4)**2)*(x+2)-10)
    scene.play(Transform(graphDict["graphWithExtreme"],
                         graphDict["ax"].plot(funcWithExtreme, [2, 5.5])),
               Transform(graphDict["lineOn4"], DashedLine(graphDict["ax"].c2p(4,-27),
                                         graphDict["ax"].c2p(4, funcWithExtreme(4)))),
               Transform(graphDict["lineOnG(4)"], DashedLine(graphDict["ax"].c2p(4, funcWithExtreme(4)),
                                                             graphDict["ax"].c2p(0.5, funcWithExtreme(4)))),
               graphDict["labelOnG(4)"].animate.move_to(graphDict["ax"].c2p(0, funcWithExtreme(4))))
    #8
    graphDict.remove("graphWithoutExtreme")
    scene.play(FadeOut(case2, graphDict))