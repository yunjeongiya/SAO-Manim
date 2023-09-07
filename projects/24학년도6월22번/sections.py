from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    ul = Underline(TEXTS[2], color=YELLOW, stroke_width=2)
    scene.play(Create(ul))
    a = 2
    graphDictifAisPositive = BasicGraphDict(
        xrange=[-1.333, 4.474, 1],
        yLengthRatio=0.15,
        hideYAxis=True,
        func = lambda x: x**2*(x-2*a),
        texScaleRatio=0.6
    ).scale(0.9).buildDotOnAxLabel(0).buildDotOnAxLabel(2*a, "$2a$")
    graphDictifAisNegative = BasicGraphDict(
        xrange=[-4.474, 1.333, 1],
        yLengthRatio=0.15,
        hideYAxis=True,
        func = lambda x: x**2*(x+2*a),
        texScaleRatio=0.6
    ).scale(0.9).buildDotOnAxLabel(0).buildDotOnAxLabel(-2*a, "$2a$")
    case1 = Tex("① $a>0$")
    case2 = Tex("② $a<0$")
    cases = VGroup(
        case1,
        graphDictifAisPositive,
        case2,
        graphDictifAisNegative
    ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.3).next_to(TEXTS, aligned_edge=UP, buff=1)
    scene.play(Create(graphDictifAisPositive))
    scene.play(Write(case1), Write(case2))
    scene.play(Create(graphDictifAisNegative))
    #3
    ul2 = VGroup(Underline(TEXTS[3][-1], color=YELLOW, stroke_width=2),
                 Underline(VGroup(TEXTS[4][0], TEXTS[4][1]), color=YELLOW, stroke_width=2))
    scene.play(FadeOut(ul), 
               FadeToColor(CONDITION[1][0], PURE_GREEN),
               FadeToColor(CONDITION[1][2], VIOLET))
    scene.play(FadeToColor(CONDITION[2][1], YELLOW))
    scene.play(Create(ul2))
    #4
    kCondition = VGroup(TEXTS[3][-1].copy(), TEXTS[4][0].copy())
    scene.play(FadeOut(ul2, TEXTS),
               kCondition.animate.arrange(buff=0.2).scale(1.3).to_corner(UL),
               VGroup(VGroup(case1, graphDictifAisPositive), VGroup(case2, graphDictifAisNegative))
               .animate.arrange(buff=2).next_to(kCondition, DOWN, aligned_edge=LEFT).shift(UP))
    #5
    scene.play(graphDictifAisPositive.animate.scale(1.8, about_edge=UL), 
               graphDictifAisNegative.animate.scale(1.8, about_edge=UL).shift(RIGHT*15),
               case2.animate.shift(RIGHT*15))
    #6
    k = ValueTracker(-3/4)
    kPlus3Over2 = ValueTracker(k.get_value()+3/2).add_updater(lambda m: m.set_value(k.get_value()+3/2))
    graphDictifAisPositive.buildDotOnAxLabel(k, MathTex("k", color=PURE_GREEN).scale(0.7), labelKey = "dotOnk", buff=-2),
    graphDictifAisPositive["lineOnk"] = always_redraw( lambda:
                                        Line(graphDictifAisPositive["ax"].c2p(k.get_value(), 0), 
                                             graphDictifAisPositive["ax"].i2gp(k.get_value(), graphDictifAisPositive["graph"]),
                                             color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisPositive["dotOnk"]),
               Create(graphDictifAisPositive["lineOnk"]))
    graphDictifAisPositive.buildDotOnAxLabel(kPlus3Over2, MathTex(r"k+ { {3} \over {2} }", color=PURE_GREEN).scale(0.7), labelKey = "dotOnkPlus3Over2", buff=-3.5)
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
    scene.play(k.animate.set_value(4/3))
    graphDictifAisPositive.buildDotOnAxLabel(4/3*a, MathTex(r"\dfrac{4}{3} a").scale(0.7), labelKey = "dotOn4Over3a")
    scene.play(Write(graphDictifAisPositive["dotOn4Over3a"]))
    #7
    willBeKPlus1 = ValueTracker(k.get_value())
    graphDictifAisPositive.buildDotOnAxLabel(willBeKPlus1, MathTex("k+1", color=VIOLET).scale(0.7), labelKey = "dotOnkPlus1", buff=-2)
    graphDictifAisPositive["linkeOnkPlus1"] = always_redraw( lambda:
                                              Line(graphDictifAisPositive["ax"].c2p(willBeKPlus1.get_value(), 0),
                                                   graphDictifAisPositive["ax"].i2gp(willBeKPlus1.get_value(), graphDictifAisPositive["graph"]),
                                                   color=VIOLET, stroke_width=2))
    willBeKPlus5Over2 = ValueTracker(kPlus3Over2.get_value())
    graphDictifAisPositive.buildDotOnAxLabel(willBeKPlus5Over2, MathTex(r"k+ { {5} \over {2} }", color=VIOLET).scale(0.6), labelKey = "dotOnkPlus5Over2", buff=-3.5)
    graphDictifAisPositive["lineOnkPlus5Over2"] = always_redraw( lambda:
                                                  Line(graphDictifAisPositive["ax"].c2p(willBeKPlus5Over2.get_value(), 0),
                                                       graphDictifAisPositive["ax"].i2gp(willBeKPlus5Over2.get_value(), graphDictifAisPositive["graph"]),
                                                       color=VIOLET, stroke_width=2))
    scene.play(willBeKPlus1.animate.set_value(willBeKPlus1.get_value()+1),
               willBeKPlus5Over2.animate.set_value(willBeKPlus5Over2.get_value()+1))
    #8
    scene.play(case2.animate.move_to(case1, aligned_edge=LEFT),
               graphDictifAisNegative.animate.move_to(graphDictifAisPositive, aligned_edge=LEFT),
               VGroup(case1, graphDictifAisPositive).animate.shift(LEFT*15))
    k.set_value(-3/4)
    graphDictifAisNegative.buildDotOnAxLabel(k, MathTex("k", color=PURE_GREEN).scale(0.7), labelKey = "dotOnk"),
    graphDictifAisNegative["lineOnk"] = always_redraw( lambda:
                                        Line(graphDictifAisNegative["ax"].c2p(k.get_value(), 0),
                                                graphDictifAisNegative["ax"].i2gp(k.get_value(), graphDictifAisNegative["graph"]),
                                                color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisNegative["dotOnk"]),
                Create(graphDictifAisNegative["lineOnk"]))
    graphDictifAisNegative.buildDotOnAxLabel(kPlus3Over2, MathTex(r"k+ { {3} \over {2} }", color=PURE_GREEN).scale(0.7), labelKey = "dotOnkPlus3Over2")
    graphDictifAisNegative["lineOnkPlus3Over2"] = always_redraw( lambda:
                                                    Line(graphDictifAisNegative["ax"].c2p(kPlus3Over2.get_value(), 0),
                                                            graphDictifAisNegative["ax"].i2gp(kPlus3Over2.get_value(), graphDictifAisNegative["graph"]),
                                                            color=PURE_GREEN, stroke_width=2))
    scene.play(Write(graphDictifAisNegative["dotOnkPlus3Over2"]),
                Create(graphDictifAisNegative["lineOnkPlus3Over2"]))
    graphDictifAisNegative.buildDotOnAxLabel(-4/3*a, MathTex(r"\dfrac{4}{3} a").scale(0.7), labelKey = "dotOn4Over3a")
    graphDictifAisNegative["lineOn4Over3a"] = DashedLine(graphDictifAisNegative["ax"].c2p(-4/3*a, 0),
                                                            graphDictifAisNegative["ax"].i2gp(-4/3*a, graphDictifAisNegative["graph"]),
                                                            stroke_width=2)
    scene.play(Create(graphDictifAisNegative["lineOn4Over3a"]),
                Write(graphDictifAisNegative["dotOn4Over3a"]))
    #9
    scene.play(k.animate.set_value(-23/6))
    willBeKPlus1.set_value(k.get_value())
    willBeKPlus1MinusBuff = ValueTracker().add_updater(lambda m: m.set_value(willBeKPlus1.get_value()-0.1))
    scene.add(willBeKPlus1MinusBuff)
    graphDictifAisNegative.buildDotOnAxLabel(willBeKPlus1MinusBuff, MathTex("k+1", color=VIOLET).scale(0.7), labelKey = "dotOnkPlus1")
    graphDictifAisNegative["lineOnkPlus1"] = always_redraw( lambda:
                                                Line(graphDictifAisNegative["ax"].c2p(willBeKPlus1.get_value(), 0),
                                                        graphDictifAisNegative["ax"].i2gp(willBeKPlus1.get_value(), graphDictifAisNegative["graph"]),
                                                        color=VIOLET, stroke_width=2))
    willBeKPlus5Over2.set_value(kPlus3Over2.get_value())
    graphDictifAisNegative.buildDotOnAxLabel(willBeKPlus5Over2, MathTex(r"k+ { {5} \over {2} }", color=VIOLET).scale(0.7), labelKey = "dotOnkPlus5Over2")
    graphDictifAisNegative["lineOnkPlus5Over2"] = always_redraw( lambda:
                                                    Line(graphDictifAisNegative["ax"].c2p(willBeKPlus5Over2.get_value(), 0),
                                                            graphDictifAisNegative["ax"].i2gp(willBeKPlus5Over2.get_value(), graphDictifAisNegative["graph"]),
                                                            color=VIOLET, stroke_width=2))
    scene.play(willBeKPlus1.animate.set_value(willBeKPlus1.get_value()+1),
                willBeKPlus5Over2.animate.set_value(willBeKPlus5Over2.get_value()+1))
    #10
    scene.add(TEXTS.shift(RIGHT*15).set_color(WHITE))
    scene.play(VGroup(kCondition, case2, graphDictifAisNegative).animate.shift(LEFT*15),
               TEXTS.animate.shift(LEFT*15))