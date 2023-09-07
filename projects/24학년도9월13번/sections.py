from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    fPrime = VGroup(MathTex(r"f'(x)=\Biggl\{"),
                    VGroup(MathTex("-x^2-2ax-b"), MathTex("x^2+2ax-b")).arrange(DOWN),
                    VGroup(MathTex("(x < 0)"), MathTex("(x \geq 0)")).arrange(DOWN)
                    ).arrange().scale(0.8).to_corner(UL)
    decrease = TEXTS[3][1].copy().scale(1.3).next_to(fPrime, DOWN, aligned_edge=LEFT)
    increase = TEXTS[3][3].copy().scale(1.3).next_to(decrease, DOWN, aligned_edge=LEFT)
    graphDict = BasicGraphDict(
        [XSTART, XEND, 1], [YSTART, YEND, 1],
        xLengthRatio=2, yLengthRatio=2,
        texScaleRatio=0.5
    ).scale(1).to_corner(UR).buildDotOnAxLabel(0, "$O$")
    graphDict["labelOn0"].shift(LEFT*0.2)
    scene.play(FadeOut(TEXTS), Write(fPrime))
    scene.play(Write(decrease), Write(increase))
    scene.play(Create(graphDict))
    graphDict.buildDotOnAxLabel(-1)
    graphDict["lineOn-1"] = DashedLine(graphDict["ax"].c2p(-1, YSTART),
                                       graphDict["ax"].c2p(-1, YEND))
    scene.play(Create(graphDict["lineOn-1"]), Write(graphDict["labelOn-1"]))
    #3
    scene.play(FadeToColor(decrease, YELLOW))
    decreaseArea = Polygon(
        graphDict["ax"].c2p(XSTART, 0),
        graphDict["ax"].c2p(XSTART, YSTART),
        graphDict["ax"].c2p(-1, YSTART),
        graphDict["ax"].c2p(-1, 0)
    , color=YELLOW).set_opacity(0.5)
    scene.play(FadeIn(decreaseArea))
    scene.play(FadeToColor(increase, MINT))
    increaseArea = Polygon(
        graphDict["ax"].c2p(-1, 0),
        graphDict["ax"].c2p(-1, YEND),
        graphDict["ax"].c2p(XEND, YEND),
        graphDict["ax"].c2p(XEND, 0)
    , color=MINT).set_opacity(0.5)
    scene.play(FadeIn(increaseArea))
    #4
    a=ValueTracker(2/3)
    minusA=ValueTracker(-a.get_value()).add_updater(lambda m: m.set_value(-a.get_value()))
    b=ValueTracker().add_updater(lambda m: m.set_value(2*a.get_value()-1))
    scene.add(a)
    scene.add(minusA)
    scene.add(b)
    graphDict.buildDotOnAxLabel(minusA, "$-a$", labelKey="labelOnMinusA")
    graphDict["lineOnMinusA"] = always_redraw(lambda: Line(graphDict["ax"].c2p(minusA.get_value(), YSTART),
                                                           graphDict["ax"].c2p(minusA.get_value(), YEND)))
    scene.play(FadeOut(increase, increaseArea, decrease, decreaseArea),
               Write(graphDict["labelOnMinusA"]), Create(graphDict["lineOnMinusA"]))
    scene.play(FadeToColor(fPrime[1][0], PURE_GREEN))
    tempGreenGraph = graphDict["ax"].plot(lambda x:-(x**2)-2*a.get_value()*x-b.get_value()).set_color(PURE_GREEN)
    scene.play(Create(tempGreenGraph))
    scene.play(FadeToColor(fPrime[1][1], VIOLET))
    tempVioletGraph = graphDict["ax"].plot(lambda x:(x**2)+2*a.get_value()*x-b.get_value()).set_color(VIOLET)
    scene.play(Create(tempVioletGraph))
    #5
    graphDict["greenGraph"] = always_redraw(lambda: graphDict["ax"].plot(lambda x:-(x**2)-2*a.get_value()*x-b.get_value(), [XSTART, 0]).set_color(PURE_GREEN))
    scene.play(FadeOut(tempGreenGraph), FadeIn(graphDict["greenGraph"]))
    graphDict["violetGraph"] = always_redraw(lambda: graphDict["ax"].plot(lambda x:(x**2)+2*a.get_value()*x-b.get_value(), [0, XEND]).set_color(VIOLET))
    scene.play(FadeOut(tempVioletGraph), FadeIn(graphDict["violetGraph"]))
    #6
    scene.play(a.animate.set_value(1/2))
    #TODO 이 다음순간 한 프레임이 바뀌는데 이유를 못찾음
    #7
    XSTART2 = -2
    XEND2 = 5
    YSTART2 = -1
    YEND2 = 6
    graphDictExpanded = BasicGraphDict(
        [XSTART2, XEND2, 1], [YSTART2, YEND2, 1],
    ).to_corner(UR).buildDotOnAxLabel(0, "$O$").buildDotOnAxLabel(-1)
    graphDictExpanded["labelOn0"].shift(LEFT*0.2)
    graphDictExpanded["greenGraph"] = always_redraw(lambda: graphDictExpanded["ax"].plot(lambda x:-(x**2)-2*a.get_value()*x-b.get_value(), [-1, 0]).set_color(PURE_GREEN))
    graphDictExpanded["violetGraph"] = always_redraw(lambda: graphDictExpanded["ax"].plot(lambda x:(x**2)+2*a.get_value()*x-b.get_value(), [0, XEND2]).set_color(VIOLET))
    graphDictExpanded.buildDotOnAxLabel(minusA, "$-a$", labelKey="labelOnMinusA")
    graphDictExpanded["lineOnMinusA"] = always_redraw(lambda: Line(graphDictExpanded["ax"].c2p(minusA.get_value(), YSTART2),
                                             graphDictExpanded["ax"].c2p(minusA.get_value(), YEND2)))
    scene.play(Transform(graphDict["ax"], graphDictExpanded["ax"]),
               Transform(graphDict["xLabel"], graphDictExpanded["xLabel"]),
               Transform(graphDict["yLabel"], graphDictExpanded["yLabel"]),
               Transform(graphDict["labelOn0"], graphDictExpanded["labelOn0"]),
               Transform(graphDict["labelOn-1"], graphDictExpanded["labelOn-1"]),
               Transform(graphDict["labelOnMinusA"], graphDictExpanded["labelOnMinusA"]),
               Transform(graphDict["lineOnMinusA"], graphDictExpanded["lineOnMinusA"]),
               Transform(graphDict["greenGraph"], graphDictExpanded["greenGraph"]),
               Transform(graphDict["violetGraph"], graphDictExpanded["violetGraph"]),
               FadeToColor(graphDict["lineOn-1"], BLACK))
    scene.remove(graphDict)
    scene.add(graphDictExpanded)
    scene.play(a.animate.set_value(-1-2**(1/2)), rate_func=linear, run_time=3)
    #8
    TEXTS.next_to(fPrime, LEFT, buff=10, aligned_edge=UP)
    scene.play(VGroup(TEXTS, fPrime, graphDictExpanded).animate.shift(RIGHT*18))
    aboutB = Tex("① $b=2a-1$").scale(0.8).next_to(TEXTS, buff=1)
    scene.play(Write(aboutB))
    aboutA = Tex(r"② $-1-\sqrt{2} \le a \le \dfrac{1}{2}$").scale(0.8).next_to(aboutB, DOWN, aligned_edge=LEFT)
    scene.play(Write(aboutA))