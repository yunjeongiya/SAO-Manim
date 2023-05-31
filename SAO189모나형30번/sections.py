from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    ax = Axes(
        x_range=[-1/2, 5/2, 1],
        y_range=[-1/4, 5/4, 1],
        x_length=6/2*3,
        y_length=6/4*3,
        axis_config={
            "include_tip": True,
            "tip_width": 0.1,
            "tip_height": 0.15,
            "include_ticks": False,
            "include_numbers": False,
        },
    )
    axLabel = VGroup(ax.get_x_axis_label("x").shift(LEFT*0.3+DOWN*0.7),
                     ax.get_y_axis_label("y").shift(LEFT*0.7+DOWN*0.3),
                     MathTex(r"\mathrm{O}").next_to(ax.c2p(0, 0), DL*0.4))
    fxFunc = lambda x: 0 if x <= 0 else x
    fx = ax.plot(fxFunc, x_range=[-1/2, 5/4], stroke_width=2)
    fxLabel = MathTex("y=f(x)").next_to(fx, LEFT).shift(RIGHT*4+UP)
    a = ValueTracker(1/2)
    aLabel = MathTex("a").next_to(ax.c2p(a.get_value(), 0), DOWN).add_updater(lambda m: m.next_to(ax.c2p(a.get_value(), 0), DOWN))
    fxMinusA = ax.plot(lambda x: fxFunc(x-a.get_value()), x_range=[-1/2, 7/4], stroke_width=2)
    dashedFxMinusA = DashedVMobject(fxMinusA, num_dashes=40)
    fxMinusALabel = MathTex("y=f(x-a)").next_to(fxMinusA, RIGHT).shift(LEFT*2+DOWN*0.5)
    graphGroup = VGroup(fxMinusA.set_color(BLACK), ax, axLabel, aLabel, dashedFxMinusA, fxMinusALabel, fx, fxLabel)
    
    ax2 = ax.copy()
    axLabel2 = axLabel.copy()
    gxFunc = lambda x: x*(2-x) if abs(x-1) <= 1 else 0
    gx = ax2.plot(gxFunc, x_range=[-1/2, 5/2], stroke_width=2)
    gxLabel = MathTex("y=g(x)").next_to(gx, RIGHT).shift(LEFT*3+UP)
    gxVertex = VGroup(
        ax.get_lines_to_point(ax.c2p(1,1)),
        MathTex("1").next_to(ax.c2p(1,0), DOWN),
        MathTex("1").next_to(ax.c2p(0,1), LEFT)
    )
    graphGroup2 = VGroup(ax2, axLabel2, gx, gxLabel, gxVertex, MathTex("2").next_to(ax.c2p(2,0), DOWN))

    scene.add(TEXTS, VGroup(graphGroup, graphGroup2).arrange(RIGHT).scale(0.5).next_to(TEXTS, DOWN, aligned_edge=LEFT))
    
    return a, graphGroup, graphGroup2