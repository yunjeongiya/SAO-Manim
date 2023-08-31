from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    ul = Underline(TEXTS[2], color=YELLOW, stroke_width=2)
    scene.play(Create(ul))
    a = 1 #실제 값은 2인데 그림이랑 맞추느라 1로 함 -> 다른 x값들도 다 /2 해서 맞춤... -> 역시 원래 값으로 하고 비율 조정하는게 나음!
    smallbuff = 0.25
    largebuff = 0.7
    graphDictifAisPositive = BasicGraphDict(
        xrange=[-largebuff, 2*a+smallbuff, 1],
        xLengthRatio=1.4,
        hideYAxis=True,
        func = lambda x: x**2*(x-2*a),
        texScaleRatio=0.35
    ).buildDotOnAxLabel(0, buff=0.1).buildDotOnAxLabel(2*a, "$2a$", buff=0.1)
    graphDictifAisNegative = BasicGraphDict(
        xrange=[-2*a-smallbuff, largebuff, 1],
        xLengthRatio=1.4,
        hideYAxis=True,
        func = lambda x: x**2*(x+2*a),
        texScaleRatio=0.35
    ).buildDotOnAxLabel(0, buff=0.1).buildDotOnAxLabel(-2*a, "$2a$", buff=0.1)
    case1 = Tex("① $a>0$")
    case2 = Tex("② $a<0$")
    cases = VGroup(
        case1,
        graphDictifAisPositive,
        case2,
        graphDictifAisNegative
    ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).next_to(TEXTS, aligned_edge=UP, buff=2)
    scene.play(Create(graphDictifAisPositive))
    scene.play(Write(case1), Write(case2))
    scene.play(Create(graphDictifAisNegative))
    #3
    ul2 = VGroup(Underline(TEXTS[3][-1], color=YELLOW, stroke_width=2), Underline(TEXTS[4][0], color=YELLOW, stroke_width=2))
    scene.play(FadeOut(ul), 
               FadeToColor(CONDITION[1][0], PURE_GREEN),
               FadeToColor(CONDITION[1][2], VIOLET))
    scene.play(FadeToColor(CONDITION[2][1], YELLOW))
    scene.play(Create(ul2))
    #4
    kCondition = TEXTS[3][-1].copy()
    scene.play(FadeOut(ul2, TEXTS),
               kCondition.animate.scale(1.3).to_corner(UL),
               VGroup(VGroup(case1, graphDictifAisPositive), VGroup(case2, graphDictifAisNegative))
               .animate.arrange(buff=1).next_to(kCondition, DOWN).shift(UP))
    #5
    scene.play(graphDictifAisPositive.animate.scale(1.6, about_edge=UL), 
               graphDictifAisNegative.animate.scale(1.6, about_edge=UL).shift(RIGHT*10),
               case2.animate.shift(RIGHT*10))
    #6
    k = ValueTracker(-3/8)
    kPlus3Over2 = ValueTracker(k.get_value()+3/4).add_updater(lambda m: m.set_value(k.get_value()+3/4))
    graphDictifAisPositive.buildDotOnAxLabel(k, MathTex("k", color=PURE_GREEN).scale(0.8), labelKey = "dotOnk", buff=-0.2),
    graphDictifAisPositive["lineOnk"] = always_redraw( lambda:
                                        Line(graphDictifAisPositive["ax"].c2p(k.get_value(), 0), 
                                             graphDictifAisPositive["ax"].i2gp(k.get_value(), graphDictifAisPositive["graph"]),
                                             color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisPositive["dotOnk"]),
               Create(graphDictifAisPositive["lineOnk"]))
    graphDictifAisPositive.buildDotOnAxLabel(kPlus3Over2, MathTex(r"k+ { {3} \over {2} }", color=PURE_GREEN).scale(0.8), labelKey = "dotOnkPlus3Over2", buff=-0.5)
    graphDictifAisPositive["lineOnkPlus3Over2"] = always_redraw( lambda: 
                                                  Line(graphDictifAisPositive["ax"].c2p(kPlus3Over2.get_value(), 0),
                                                       graphDictifAisPositive["ax"].i2gp(kPlus3Over2.get_value(), graphDictifAisPositive["graph"]),
                                                       color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisPositive["dotOnkPlus3Over2"]),
               Create(graphDictifAisPositive["lineOnkPlus3Over2"]))
    graphDictifAisPositive["lineOn4Over3a"] = DashedLine(graphDictifAisPositive["ax"].c2p(4/3*a, 0),
                                                         graphDictifAisPositive["ax"].i2gp(4/3*a, graphDictifAisPositive["graph"]),
                                                         stroke_width=2)
    scene.play(Create(graphDictifAisPositive["lineOn4Over3a"]))
    scene.add(k, kPlus3Over2)
    scene.play(k.animate.set_value(2/3)) #k+1/2<4/3<k+3/4, k+5/4<2 -> k=2/3 #였으나 그냥 모양 맞추느라 다 바뀜
    graphDictifAisPositive.buildDotOnAxLabel(4/3*a, MathTex(r"{4}\over{3} a").scale(0.8), labelKey = "dotOn4Over3a", buff=0.1)
    scene.play(Write(graphDictifAisPositive["dotOn4Over3a"]))
    #7
    willBeKPlus1 = ValueTracker(k.get_value())
    graphDictifAisPositive.buildDotOnAxLabel(willBeKPlus1, MathTex("k+1", color=VIOLET).scale(0.8), labelKey = "dotOnkPlus1", buff=-0.2)
    graphDictifAisPositive["linkeOnkPlus1"] = always_redraw( lambda:
                                              Line(graphDictifAisPositive["ax"].c2p(willBeKPlus1.get_value(), 0),
                                                   graphDictifAisPositive["ax"].i2gp(willBeKPlus1.get_value(), graphDictifAisPositive["graph"]),
                                                   color=VIOLET, stroke_width=2))
    willBekPlus5Over2 = ValueTracker(kPlus3Over2.get_value())
    graphDictifAisPositive.buildDotOnAxLabel(willBekPlus5Over2, MathTex(r"k+ { {5} \over {2} }", color=VIOLET).scale(0.8), labelKey = "dotOnkPlus5Over2", buff=-0.5)
    graphDictifAisPositive["lineOnkPlus5Over2"] = always_redraw( lambda:
                                                  Line(graphDictifAisPositive["ax"].c2p(willBekPlus5Over2.get_value(), 0),
                                                       graphDictifAisPositive["ax"].i2gp(willBekPlus5Over2.get_value(), graphDictifAisPositive["graph"]),
                                                       color=VIOLET, stroke_width=2))
    scene.play(willBeKPlus1.animate.set_value(willBeKPlus1.get_value()+1/3),
               willBekPlus5Over2.animate.set_value(willBekPlus5Over2.get_value()+1/3))
    #8
    scene.play(case2.animate.move_to(case1, aligned_edge=LEFT),
               graphDictifAisNegative.animate.move_to(graphDictifAisPositive, aligned_edge=LEFT),
               VGroup(case1, graphDictifAisPositive).animate.shift(LEFT*10))
    k.set_value(-3/8)
    graphDictifAisNegative.buildDotOnAxLabel(k, MathTex("k", color=PURE_GREEN).scale(0.8), labelKey = "dotOnk", buff=0.1),
    graphDictifAisNegative["lineOnk"] = always_redraw( lambda:
                                        Line(graphDictifAisNegative["ax"].c2p(k.get_value(), 0),
                                                graphDictifAisNegative["ax"].i2gp(k.get_value(), graphDictifAisNegative["graph"]),
                                                color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisNegative["dotOnk"]),
                Create(graphDictifAisNegative["lineOnk"]))
    graphDictifAisNegative.buildDotOnAxLabel(kPlus3Over2, MathTex(r"k+ { {3} \over {2} }", color=PURE_GREEN).scale(0.8), labelKey = "dotOnkPlus3Over2", buff=0.1)
    graphDictifAisNegative["lineOnkPlus3Over2"] = always_redraw( lambda:
                                                    Line(graphDictifAisNegative["ax"].c2p(kPlus3Over2.get_value(), 0),
                                                            graphDictifAisNegative["ax"].i2gp(kPlus3Over2.get_value(), graphDictifAisNegative["graph"]),
                                                            color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisNegative["dotOnkPlus3Over2"]),
                Create(graphDictifAisNegative["lineOnkPlus3Over2"]))
    graphDictifAisNegative.buildDotOnAxLabel(-4/3*a, MathTex(r"{4}\over{3} a").scale(0.8), labelKey = "dotOn4Over3a", buff=0.1)
    graphDictifAisNegative["lineOn4Over3a"] = DashedLine(graphDictifAisNegative["ax"].c2p(-4/3*a, 0),
                                                            graphDictifAisNegative["ax"].i2gp(-4/3*a, graphDictifAisNegative["graph"]),
                                                            stroke_width=2)
    scene.play(Create(graphDictifAisNegative["lineOn4Over3a"]),
                Write(graphDictifAisNegative["dotOn4Over3a"]))
    #9
    scene.play(k.animate.set_value(-22/12))
    willBeKPlus1.set_value(k.get_value())
    graphDictifAisNegative.buildDotOnAxLabel(willBeKPlus1, MathTex("k+1", color=VIOLET).scale(0.8), labelKey = "dotOnkPlus1", buff=0.1)
    graphDictifAisNegative["lineOnkPlus1"] = always_redraw( lambda:
                                                Line(graphDictifAisNegative["ax"].c2p(willBeKPlus1.get_value(), 0),
                                                        graphDictifAisNegative["ax"].i2gp(willBeKPlus1.get_value(), graphDictifAisNegative["graph"]),
                                                        color=VIOLET, stroke_width=2))
    willBekPlus5Over2.set_value(kPlus3Over2.get_value())
    graphDictifAisNegative.buildDotOnAxLabel(willBekPlus5Over2, MathTex(r"k+ { {5} \over {2} }", color=VIOLET).scale(0.8), labelKey = "dotOnkPlus5Over2", buff=0.1)
    graphDictifAisNegative["lineOnkPlus5Over2"] = always_redraw( lambda:
                                                    Line(graphDictifAisNegative["ax"].c2p(willBekPlus5Over2.get_value(), 0),
                                                            graphDictifAisNegative["ax"].i2gp(willBekPlus5Over2.get_value(), graphDictifAisNegative["graph"]),
                                                            color=VIOLET, stroke_width=2))
    scene.play(willBeKPlus1.animate.set_value(willBeKPlus1.get_value()+1/3),
                willBekPlus5Over2.animate.set_value(willBekPlus5Over2.get_value()+1/3))
    #10
    scene.add(TEXTS.shift(RIGHT*10).set_color(WHITE))
    scene.play(VGroup(kCondition, case2, graphDictifAisNegative).animate.shift(LEFT*10),
               TEXTS.animate.shift(LEFT*10))