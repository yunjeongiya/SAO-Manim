from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene) :
    scene.add(TEXTS)

def describeProblem(scene:Scene):
    boxes = VGroup( SurroundingRectangle(TEXTS[2]), SurroundingRectangle(TEXTS[3]))
    scene.play(Create(boxes))
    ul = Underline(TEXTS[5][0].get_part_by_tex("$f(x)$는 실수 전체의 집합에서"), color=YELLOW)
    box = SurroundingRectangle(TEXTS[5][0].get_part_by_tex("미분가능"))
    scene.play(FadeOut(boxes),
               Create(VGroup(ul, box)))
    box2 = SurroundingRectangle(TEXTS[5][1].get_part_by_tex("$f(x) \geq g(x)$"))
    scene.play(FadeOut(VGroup(ul, box)),
               Create(box2))
    scene.remove(box2)

def analyzeFx(scene:Scene, fx, conditions):
    rightFxFunc = lambda x: pow(x-1, 2)*(2*x+1)
    fxGroup = basicGraphGroup([XSTART, XEND], [YSTART, YEND], func = rightFxFunc,
                              yLengthRatio=YLENRATIO,
                              y_axis_config={"include_tip": False, "stroke_width": 0}).next_to(fx, DOWN).shift(RIGHT)
    fxGroup.buildGraphLabel("$y=f(x)$", direction=LEFT)
    #cases의 &로 이어진 부분은 모양으로 검색했을 때 찾을 수 x (& 자체가 전체 줄에 따라 움직이는 거라 같은 모양 임시객체를 만들 수 없음)
    # -> 시작점 끝점 구해서 새로 직선 그어 해결
    ul =  Line(Underline(fx[0][searchShapesInTex(fx, MathTex(r"(x-1)"))]).get_left(), 
    Underline(fx[0][searchShapesInTex(fx, MathTex(r"(x>a)"))]).get_right(), color=YELLOW)
    scene.play(Create(ul))
    scene.play(Create(fxGroup["ax"]), Create(fxGroup["xLabel"]))
    box = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"{(x-1)}^2"))])
    dot1 = Dot(fxGroup["ax"].c2p(1, 0), color=YELLOW).scale(0.7)
    scene.play(FadeOut(ul), Create(box), Create(dot1), Create(fxGroup.dotOnAxLabelBuilder(1)))

    box2 = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"(2x+1)"))])
    dot1over2 = Dot(fxGroup["ax"].c2p(-0.5, 0), color=YELLOW).scale(0.7)
    scene.play(FadeOut(Group(box, dot1)), 
               Create(box2), Create(dot1over2), Create(fxGroup.dotOnAxLabelBuilder(-0.5, MathTex(r"-\frac{1}{2}"), buf=0.7)))

    scene.play(FadeOut(Group(box2, dot1over2)),
               Create(fxGroup["graph"]), Create(fxGroup["graphLabel"]))
    
    box = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"(x>a)"))])
    a = ValueTracker(1/4)
    scene.add(a)
    aLine = always_redraw(
        lambda: Line(fxGroup["ax"].c2p(a.get_value(), YSTART-2),
                     fxGroup["ax"].c2p(a.get_value(), YEND),
                     stroke_width = 1)
    )
    fxGroup.dotOnAxLabelBuilder(a, MathTex("a"), labelKey="labelOnA")
    scene.play(Create(box), Create(aLine), Create(fxGroup["labelOnA"]))
    
    oldGraph = fxGroup["graph"]
    fxGroup["graph"] = always_redraw(lambda: fxGroup["ax"].plot(rightFxFunc, [a.get_value(), XEND], color=YELLOW))
    scene.play(FadeOut(oldGraph), FadeIn(fxGroup["graph"]))

    box2 = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"(x \leq a)"))], color=MINT)
    leftFx = always_redraw(lambda: Line(fxGroup["ax"].c2p(XSTART, 0), fxGroup["ax"].c2p(a.get_value(), 0), color=MINT))
    scene.play(Create(box2), Create(leftFx))

    scene.play(a.animate.set_value(XSTART), run_time=2)
    scene.play(a.animate.set_value(XEND), run_time=2)
    scene.play(a.animate.set_value(1/4), run_time=2)

    ul = Line(Underline(conditions[0].get_part_by_tex("실수 전체의 집합에서")).get_left(),
              Underline(conditions[0].get_part_by_tex("미분가능")).get_right(),
              color=YELLOW)
    scene.play(Create(ul))

    scene.play(a.animate.set_value(1))

    rightFx = fxGroup["graph"]
    fxGroup["graph"] = always_redraw(lambda: fxGroup["ax"].plot(lambda x: rightFxFunc(x) if x>1 else 0, color=MINT))
    aSlices = searchShapesInTex(fx, MathTex(r"a"))
    aTex = VGroup(fx[0][aSlices[0]], fx[0][aSlices[1]])
    oneTex = VGroup(
        fxGroup["labelOn1"].copy().move_to(aTex[0].get_center()),
        fxGroup["labelOn1"].copy().move_to(aTex[1].get_center())
    )
    scene.play(FadeOut(Group(box, box2, ul, aLine, rightFx, leftFx, fxGroup["labelOnA"])),
               FadeToColor(fxGroup["graphLabel"], MINT), FadeIn(fxGroup["graph"]),
               AnimationGroup(AnimationGroup(TransformFromCopy(fxGroup["labelOn1"], oneTex[0]), 
                                             TransformFromCopy(fxGroup["labelOn1"], oneTex[1])),
                              FadeOut(aTex), lag_ratio=0.5))
    fxGroup.remove("labelOnA")
    return fxGroup

def analyzeGx(scene:Scene, gx):
    ul = Underline(gx[0][searchShapesInTex(gx, MathTex("12")).start:
                         searchShapesInTex(gx, MathTex("x-k")).stop+1], color=YELLOW)
    k = ValueTracker((XSTART+XEND)/2)
    rightGxFunc = lambda x: 12 * (x-k.get_value())
    gxGroup = basicGraphGroup([XSTART, XEND], [YSTART, YEND], func = lambda x: rightGxFunc(x)/12,
                              yLengthRatio=YLENRATIO,
                              y_axis_config={"include_tip": False, "stroke_width": 0}).next_to(gx, DOWN)
    scene.play(Create(ul))
    scene.play(Create(gxGroup["ax"]), Create(gxGroup["xLabel"]))

    box = SurroundingRectangle(gx[0][searchShapesInTex(gx, MathTex(r"x-k"))])
    scene.play(FadeOut(ul), Create(box))
    gxGroup["labelOnK"] = gxGroup.dotOnAxLabelBuilder(k, MathTex("k"), labelKey="labelOnK")
    scene.play(Create(gxGroup["graph"]), Create(gxGroup["labelOnK"]))

    scene.remove(box)
    scene.play(Indicate(gx[0][searchShapesInTex(gx, MathTex(r"12"))]))
    oldGraph = gxGroup["graph"]
    gxGroup["graph"] = always_redraw(lambda: gxGroup["ax"].plot(rightGxFunc, [YSTART/12 + k.get_value(), YEND/12 + k.get_value()]))
    scene.play(ReplacementTransform(oldGraph, gxGroup["graph"]))

    box = SurroundingRectangle(gx[0][searchShapesInTex(gx, MathTex(r"x > k"))])
    scene.play(Create(box))
    oldGraph = gxGroup["graph"]
    gxGroup["graph"] = always_redraw(lambda: gxGroup["ax"].plot(rightGxFunc, [k.get_value(), YEND/12 + k.get_value()], color=YELLOW))
    scene.play(ReplacementTransform(oldGraph, gxGroup["graph"]))

    box2 = SurroundingRectangle(gx[0][searchShapesInTex(gx, MathTex(r"x \leq k"))])
    scene.play(Transform(box, box2))
    leftGx = always_redraw(lambda: Line(gxGroup["ax"].c2p(XSTART, 0), gxGroup["ax"].c2p(k.get_value(), 0), color=YELLOW))
    scene.play(Create(leftGx))
    rightGx = gxGroup["graph"]
    gxGroup.buildGraphLabel("$y=g(x)$", color=YELLOW)
    gxGroup["graph"] = VGroup(leftGx, rightGx)
    scene.next_section()
    scene.play(Write(gxGroup["graphLabel"].add_updater(lambda m: m.next_to(gxGroup["graph"], UR).shift(DOWN*0.4))))
    return gxGroup
    
def analyzeGraph(scene:Scene):
    TEXTS.save_state()
    conditions = TEXTS[5]
    fx = TEXTS[2]
    gx = TEXTS[3]
    scene.play(conditions.animate.to_edge(UP), 
               fx.animate.shift(DOWN*0.5),
               gx.animate.next_to(TEXTS[2], RIGHT).shift(DOWN*0.5+RIGHT*2),
               FadeOut(Group(TEXTS[0], TEXTS[1], TEXTS[4], TEXTS[6], TEXTS[7])))
    fxGroup = analyzeFx(scene, fx, conditions)
    gxGroup = analyzeGx(scene, gx)