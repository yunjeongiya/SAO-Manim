from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)
    #2
    fx = MathTex("f(x)=x(x-1)(x-a)").scale(0.8).next_to(TEXTS, aligned_edge=UP).shift(LEFT*1.5)
    scene.play(Write(fx))
    graphDicts = VGroup(
    VGroup(*[BasicGraphDict(
        [-0.2, 2.2], hideYAxis=True,
        func = lambda x: x*(x-1)*(x-2),
        texScaleRatio=0.7
    ) for _ in range(3)]).arrange(),
    VGroup(BasicGraphDict(
        [-0.2, 2.2], hideYAxis=True,
        func = lambda x: x*(x-1)*(x-2),
        texScaleRatio=0.7
    ).set_color(BLACK).set_opacity(0),
    BasicGraphDict(
        [-0.2, 2.2], hideYAxis=True,
        func = lambda x: x*(x-1)*(x-2)-0.385, #중근 0.423, 실근 2.155
        texScaleRatio=0.7,
    ),
    BasicGraphDict(
        [-0.2, 2.2], hideYAxis=True,
        func = lambda x: x*(x-1)*(x-2)+0.385, #실근 -0.155 중근 1.577
        texScaleRatio=0.7,
    )).arrange()
    ).arrange(DOWN, aligned_edge=RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.6).scale(0.95).next_to(fx, DOWN, aligned_edge=LEFT).shift(LEFT*0.5+UP*0.3)
    scene.play(Create(graphDicts[0][0]))
    scene.play(Create(graphDicts[0][1]))
    scene.play(Create(graphDicts[0][2]))
    #3
    scene.play(Write(graphDicts[0][0].buildDotOnAxLabel(0).set_color(PURE_GREEN)),
               Write(graphDicts[0][0].buildDotOnAxLabel(1).set_color(PURE_GREEN)))
    scene.play(Write(graphDicts[0][1].buildDotOnAxLabel(0).set_color(PURE_GREEN)),
               Write(graphDicts[0][1].buildDotOnAxLabel(2, "1").set_color(PURE_GREEN)))
    scene.play(Write(graphDicts[0][2].buildDotOnAxLabel(1, "0").set_color(PURE_GREEN)),
               Write(graphDicts[0][2].buildDotOnAxLabel(2, "1").set_color(PURE_GREEN)))
    scene.play(Write(graphDicts[0][0].buildDotOnAxLabel(2, "$a$")),
               Write(graphDicts[0][1].buildDotOnAxLabel(1, "$a$")),
               Write(graphDicts[0][2].buildDotOnAxLabel(0, "$a$")))
    #4
    scene.play(Create(graphDicts[1][1]))
    scene.play(Write(graphDicts[1][1].buildDotOnAxLabel(0.423, "0").set_color(PURE_GREEN)),
               Write(graphDicts[1][1].buildDotOnAxLabel(2.155, "1").set_color(PURE_GREEN)))
    #5
    scene.play(Create(graphDicts[1][2]))
    scene.play(Write(graphDicts[1][2].buildDotOnAxLabel(-0.155, "0").set_color(PURE_GREEN)),
               Write(graphDicts[1][2].buildDotOnAxLabel(1.577, "1").set_color(PURE_GREEN)))
    #6
    scene.play(graphDicts[0][0].animate.set_color(GREY))
    scene.play(graphDicts[0][1].animate.set_color(GREY))
    scene.play(graphDicts[1][1].animate.set_color(GREY))
    scene.play(graphDicts[1][2].animate.set_color(GREY))
    #7
    graphDict = graphDicts[0][2]
    scene.play(FadeOut(graphDicts),
               graphDict.animate.scale(2, about_point=graphDicts[0][2].get_edge_center(UR)).shift(LEFT*0.3))
    #8
    scene.add(graphDict)
    scene.play(Transform(graphDict["labelOn0"], Tex("-1", color=MINT).scale(graphDict.getScaleRatio()*graphDict.texScaleRatio).move_to(graphDict["labelOn0"], aligned_edge=UP)))
    upperArea = always_redraw(lambda : graphDict["ax"].get_area(graphDict["graph"], [0, 1], color=YELLOW, opacity=0.5))
    lowerArea = always_redraw(lambda : graphDict["ax"].get_area(graphDict["graph"], [1, 2], color=PURE_GREEN, opacity=0.5))
    scene.play(FadeIn(upperArea, lowerArea))
    #9
    a = ValueTracker(0)
    scene.add(a)
    graphDict.buildDotOnAxLabel(a, MathTex("a").set_z_index(-1), "labelOnA")
    graphDict["graph"] = always_redraw(lambda: graphDict["ax"].plot(lambda x: (x-a.get_value())*(x-1)*(x-2)))
    graphDict["liineOn0"] = always_redraw(lambda: Line(graphDict["ax"].c2p(0, 0), graphDict["ax"].i2gp(0, graphDict["graph"]), stroke_width=2))
    scene.play(a.animate.set_value(1/2))
    scene.play(a.animate.set_value(-0.2))
    #10
    gx = MathTex(r"g({{t}})=\int_{{t}}^{{ {t+1} }} f(x)dx {{-}} \int_0^1 {{|}}f(x){{|}}dx").scale(0.8).next_to(graphDict, DOWN)
    scene.play(TransformFromCopy(TEXTS[3], gx))
    gMinus1 = MathTex(r"g({{-1}})=\int_{{ {-1} }}^{{ 0 }} f(x)dx {{-}} \int_0^1 {{|}}f(x){{|}}dx").scale(0.8).next_to(graphDict, DOWN)
    scene.play(TransformMatchingTex(gx, gMinus1))
    #11
    gMinus1WithoutAbs = MathTex(r"g({{-1}})=\int_{{ {-1} }}^{{ 0 }} f(x)dx {{+}} \int_0^1 f(x){{dx}}").scale(0.8).next_to(graphDict, DOWN)
    scene.play(TransformMatchingTex(gMinus1, gMinus1WithoutAbs))
    #12
    gMinus1Final = VGroup(MathTex(r"{{g(-1)= \int _{-1} }}").scale(0.8).move_to(gMinus1WithoutAbs, aligned_edge=LEFT).shift(DOWN*0.04),
                          MathTex(r"{{\int}}{{^1 f(x)dx}}").scale(0.8).move_to(gMinus1WithoutAbs, aligned_edge=RIGHT).shift(UP*0.01))
    scene.play(FadeOut(gMinus1WithoutAbs), FadeIn(gMinus1Final[0]),
               gMinus1Final[1][1].animate.shift(LEFT*2.4))