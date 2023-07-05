from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene) :
    scene.add(TEXTS)

def describeProblem(scene:Scene):
    boxes = VGroup( SurroundingRectangle(TEXTS[2]), SurroundingRectangle(TEXTS[3]))
    scene.play(Create(boxes[0]), Create(boxes[1]))
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
    fxGroup.remove("yLabel")
    fxGroup.buildGraphLabel(MathTex("{{y=}}f(x)"), direction=LEFT)
    #cases의 &로 이어진 부분은 모양으로 검색했을 때 찾을 수 x (& 자체가 전체 줄에 따라 움직이는 거라 같은 모양 임시객체를 만들 수 없음)
    # -> 시작점 끝점 구해서 새로 직선 그어 해결
    ul =  Line(Underline(fx[0][searchShapesInTex(fx, MathTex(r"(x-1)"))]).get_left(), 
    Underline(fx[0][searchShapesInTex(fx, MathTex(r"(x>a)"))]).get_right(), color=YELLOW)
    scene.play(Create(ul))
    scene.play(Create(fxGroup["ax"]), Create(fxGroup["xLabel"]))
    box = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"{(x-1)}^2"))])
    dot1 = Dot(fxGroup["ax"].c2p(1, 0), color=YELLOW).scale(0.7)
    scene.play(FadeOut(ul), Create(box), Create(dot1), Create(fxGroup.buildDotOnAxLabel(1)))

    box2 = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"(2x+1)"))])
    dot1over2 = Dot(fxGroup["ax"].c2p(-0.5, 0), color=YELLOW).scale(0.7)
    scene.play(FadeOut(Group(box, dot1)), 
               Create(box2), Create(dot1over2), Create(fxGroup.buildDotOnAxLabel(-0.5, MathTex(r"-\frac{1}{2}").scale(0.8), buff=1)))

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
    fxGroup.buildDotOnAxLabel(a, MathTex("a"), labelKey="labelOnA")
    scene.play(Create(box))
    scene.play(Create(aLine), Create(fxGroup["labelOnA"]))
    
    oldGraph = fxGroup["graph"]
    fxGroup["graph"] = always_redraw(lambda: fxGroup["ax"].plot(rightFxFunc, [a.get_value(), XEND], color=YELLOW))
    scene.play(FadeOut(oldGraph), FadeIn(fxGroup["graph"]))

    box2 = SurroundingRectangle(fx[0][searchShapesInTex(fx, MathTex(r"(x \leq a)"))], color=MINT)
    leftFx = always_redraw(lambda: Line(fxGroup["ax"].c2p(XSTART, 0), fxGroup["ax"].c2p(a.get_value(), 0), color=MINT))
    scene.play(Create(box2))
    scene.play(Create(leftFx))

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
    scene.play(FadeOut(Group(box, box2, ul, aLine, rightFx, leftFx, fxGroup["labelOnA"], fxGroup["labelOn-0.5"])),
               FadeToColor(fxGroup["graphLabel"], MINT), FadeIn(fxGroup["graph"]),
               AnimationGroup(AnimationGroup(TransformFromCopy(fxGroup["labelOn1"], oneTex[0]), 
                                             TransformFromCopy(fxGroup["labelOn1"], oneTex[1])),
                              aTex.animate.become(oneTex), lag_ratio=0.5))
    fxGroup.remove("labelOnA")
    fxGroup.remove("labelOn-0.5")
    scene.remove(oneTex[0], oneTex[1])
    return fxGroup

def analyzeGx(scene:Scene, gx):
    ul = Underline(gx[0][searchShapesInTex(gx, MathTex("12")).start:
                         searchShapesInTex(gx, MathTex("x-k")).stop+1], color=YELLOW)
    k = ValueTracker((XSTART+XEND)/2)
    rightGxFunc = lambda x: 12 * (x-k.get_value())
    gxGroup = basicGraphGroup([XSTART, XEND], [YSTART, YEND], func = lambda x: rightGxFunc(x)/3,
                              yLengthRatio=YLENRATIO,
                              y_axis_config={"include_tip": False, "stroke_width": 0}).next_to(gx, DOWN)
    gxGroup.remove("yLabel")
    scene.play(Create(ul))
    scene.play(Create(gxGroup["ax"]), Create(gxGroup["xLabel"]))

    box = SurroundingRectangle(gx[0][searchShapesInTex(gx, MathTex(r"x-k"))])
    scene.play(FadeOut(ul), Create(box))
    gxGroup["labelOnK"] = gxGroup.buildDotOnAxLabel(k, MathTex("k"), labelKey="labelOnK")
    scene.play(Create(gxGroup["graph"]), Create(gxGroup["labelOnK"]))

    scene.remove(box)
    scene.play(Indicate(gx[0][searchShapesInTex(gx, MathTex(r"12"))]))
    oldGraph = gxGroup["graph"]
    gxGroup["graph"] = always_redraw(lambda: gxGroup["ax"].plot(rightGxFunc, [XSTART+1, YEND/12 + k.get_value()]))
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
    gxGroup.buildGraphLabel(MathTex("{{y=}}g(x)"), color=YELLOW)
    gxGroup["graph"] = VGroup(leftGx, rightGx)
    gxGroup["rightGraph"] = rightGx
    gxGroup["leftGraph"] = leftGx
    scene.play(Write(gxGroup["graphLabel"].add_updater(lambda m: m.next_to(gxGroup["graph"], UR).shift(DOWN*0.4))))
    scene.remove(box)
    return gxGroup, k

def compareGraph(scene:Scene, fx, gx, conditions, fxGroup:basicGraphGroup, gxGroup:basicGraphGroup, k:ValueTracker):
    compareFGTex = conditions[1].get_part_by_tex(r"$f(x) \geq g(x)$")
    box = SurroundingRectangle(compareFGTex)
    scene.play(Create(box))
    compareFGTexCopy = MathTex(r"f(x) {{\geq}} g(x)").scale_to_fit_height(compareFGTex.height).move_to(compareFGTex)
    compareFGTexCopy.set_color_by_tex("f(x)", MINT)
    compareFGTexCopy.set_color_by_tex("g(x)", YELLOW)
    scene.play(k.animate.set_value(XEND-0.2))
    scene.add(compareFGTexCopy)
    scene.play(FadeOut(Group(box, fx, gx, conditions)),
               FadeIn(compareFGTexCopy),
               fxGroup.animate.scale(1.5).move_to(ORIGIN+LEFT*1.5, aligned_edge=LEFT),
               gxGroup.animate.scale(1.5).move_to(ORIGIN+LEFT*1.5, aligned_edge=LEFT))
    contact = Dot(fxGroup["ax"].i2gp(CONTACTX, fxGroup["graph"]), color=RED)
    scene.play(k.animate.set_value(KMIN))
    scene.add(contact)
    scene.play(Flash(contact))
    scene.remove(contact)

    kMinPointer = pointerBuilder(Tex("$k$의 최솟값").scale(0.7), gxGroup["labelOnK"])
    scene.play(Create(kMinPointer))
    
    scene.play(FadeOut(kMinPointer, compareFGTexCopy),
               fxGroup.animate.to_edge(LEFT).shift(LEFT),
               gxGroup.animate.to_edge(LEFT).shift(LEFT))
    
def analyzeGraph(scene:Scene):
    conditions = TEXTS[5].copy()
    fx = TEXTS[2].copy()
    gx = TEXTS[3].copy()
    scene.play(conditions.animate.to_edge(UP), 
               fx.animate.shift(DOWN*0.5),
               gx.animate.next_to(TEXTS[2], RIGHT).shift(DOWN*0.5+RIGHT*2),
               FadeOut(TEXTS))
    fxGroup = analyzeFx(scene, fx, conditions)
    gxGroup, k = analyzeGx(scene, gx)
    compareGraph(scene, fx, gx, conditions, fxGroup, gxGroup, k)

    return fxGroup, gxGroup

def calculatefPrime(scene: Scene, fx):    
    fPrime = VGroup(MathTex("f{{'}}(x)=")).next_to(fx, DOWN, aligned_edge=LEFT)
    scene.play(TransformFromCopy(fx[0], fPrime[0]))
    scene.play(Indicate(fPrime[0][1]))

    decomposedFxRight = MathTex("(x-1){{(x-1)}}(2x+1)").move_to(fx[2:], aligned_edge=LEFT)
    scene.play(ReplacementTransform(fx[2:], decomposedFxRight))

    fPrime += MathTex(r"{{1}}\cdot{{(x-1)}}(2x+1)").next_to(fPrime[0])
    scene.play(FadeToColor(decomposedFxRight[0], YELLOW))
    scene.play(TransformFromCopy(decomposedFxRight[0], fPrime[1][0].set_color(YELLOW)))
    scene.play(TransformFromCopy(decomposedFxRight[1:], fPrime[1][2:]),
               FadeIn(fPrime[1][1]))

    fPrime += MathTex(r"{{(x-1)}}\cdot{{1}}\cdot{{(2x+1)}}").next_to(fPrime[1], DOWN, aligned_edge=LEFT)
    scene.play(FadeToColor(Group(decomposedFxRight[0], fPrime[1]), WHITE),
               FadeToColor(decomposedFxRight[1], YELLOW))
    scene.play(TransformFromCopy(decomposedFxRight[1], fPrime[2][2].set_color(YELLOW)))
    scene.play(TransformFromCopy(decomposedFxRight[0], fPrime[2][0]),
               FadeIn(fPrime[2][1]),
               FadeIn(fPrime[2][3]),
               TransformFromCopy(decomposedFxRight[2], fPrime[2][4]))
    
    fPrime += MathTex(r"(x-1){{(x-1)}}\cdot{{2}}").next_to(fPrime[2], DOWN, aligned_edge=LEFT)
    scene.play(FadeToColor(Group(decomposedFxRight[1], fPrime[2]), WHITE),
               FadeToColor(decomposedFxRight[2], YELLOW))
    scene.play(TransformFromCopy(decomposedFxRight[2], fPrime[3][3].set_color(YELLOW)))
    scene.play(TransformFromCopy(decomposedFxRight[:2], fPrime[3][:2]),
               FadeIn(fPrime[3][2]))

    plus = VGroup(
        MathTex("+").next_to(fPrime[2], LEFT),
        MathTex("+").next_to(fPrime[3], LEFT)
    ).set_color(YELLOW)
    scene.play(FadeToColor(Group(decomposedFxRight[2], fPrime[3]), WHITE),
               Write(plus))

    oldFPrime = fPrime[1:]
    fPrime.remove(*oldFPrime)
    fPrime += MathTex("{{6}}x(x-1)").next_to(fPrime[0])
    oldFPrime += plus
    scene.play(ReplacementTransform(oldFPrime, fPrime[1]))

    return decomposedFxRight, fPrime

def findContactX(scene:Scene, fxGroup: basicGraphGroup, fPrime):
    scene.play(FadeOut(fPrime[1][0]), Transform(fPrime[-1][-1], MathTex("2").move_to(fPrime[-1][-1], aligned_edge=LEFT)))
    
    scene.play(Transform(fPrime[1][1], MathTex("x^2-x").move_to(fPrime[1][1], aligned_edge=RIGHT)))
    
    minus2 = MathTex("-2").move_to(fPrime[1][1], aligned_edge=RIGHT)
    scene.play(fPrime[1][1].animate.shift(LEFT*0.8),
               Transform(fPrime[-1][-1], MathTex("0").move_to(fPrime[-1][-1])),
               TransformFromCopy(fPrime[-1][-1], minus2))
    
    leftEq = MathTex("(x+1){{(x-2)}}").move_to(minus2, aligned_edge=RIGHT)
    scene.play(ReplacementTransform(VGroup(fPrime[1][1], minus2),leftEq))

    x1 = pointerBuilder(MathTex("x=-1"), leftEq[0], arrow_len=3)
    x2 = pointerBuilder(MathTex("x={{2}}"), leftEq[1], arrow_len=3)
    scene.play(Create(x1))
    scene.play(Create(x2))

    contact = Dot(fxGroup["ax"].i2gp(CONTACTX, fxGroup["graph"]), color=RED)
    scene.play(Create(contact))
    contactLine = fxGroup["ax"].get_vertical_line(fxGroup["ax"].i2gp(CONTACTX, fxGroup["graph"]))
    scene.play(Create(contactLine.rotate(PI)))
    scene.play(Wiggle(fxGroup["labelOn1"]))

    scene.play(FadeOut(Group(leftEq, fPrime[-1], x1, x2["arrow"])))
    scene.play(TransformFromCopy(x2["tex"][-1], fxGroup.buildDotOnAxLabel(2)))

    return x2["tex"], contact, contactLine

def findContactY(scene:Scene, fxGroup: basicGraphGroup, x2, contact: Dot):
    xToChange = fxGroup["graphLabel"].get_parts_by_tex("x")
    alter2s = VGroup(*[MathTex("2").scale(fxGroup.getScaleRatio()*fxGroup.texScaleRatio).move_to(x).shift(UP*0.05) for x in xToChange])
    scene.play(FadeOut(x2),
               AnimationGroup(TransformFromCopy(fxGroup["labelOn2"], alter2s),
               xToChange.animate.become(alter2s), lag_ratio=0.5))
    scene.remove(alter2s)

    newFxLabel = MathTex("{{y=}}5").scale(fxGroup.getScaleRatio()*fxGroup.texScaleRatio).move_to(fxGroup["graphLabel"], aligned_edge=LEFT)
    newFxLabel[0].set_color(MINT)
    scene.play(ReplacementTransform(fxGroup["graphLabel"], newFxLabel))
    fxGroup.remove("graphLabel")

    contactLabel = MathTex("({{2}}, {{5}})").next_to(contact, RIGHT)
    scene.play(FadeOut(newFxLabel),
               TransformFromCopy(fxGroup["labelOn2"], contactLabel.get_part_by_tex("2")),
               TransformFromCopy(newFxLabel.get_part_by_tex("5"), contactLabel.get_part_by_tex("5")),
               FadeIn(Group(contactLabel[0], contactLabel[2], contactLabel[4])))

    return contactLabel

def calculateForK(scene:Scene, fxGroup:basicGraphGroup, gxGroup:basicGraphGroup):
    newFxLabel = MathTex("{{y=}}({{x}}-1)^2 (2{{x}}+1)", color=MINT).scale(fxGroup.getScaleRatio()*fxGroup.texScaleRatio).move_to(fxGroup["graphLabel"], aligned_edge=RIGHT)
    newGxLabel = MathTex("{{y}}={{12}}({{x}}-k)}}", color=YELLOW).scale(gxGroup.getScaleRatio()*gxGroup.texScaleRatio).move_to(gxGroup["graphLabel"], aligned_edge=LEFT)
    scene.play(Transform(fxGroup["graphLabel"], newFxLabel),
               Transform(gxGroup["graphLabel"], newGxLabel))
    fxGroup["graphLabel"] = newFxLabel
    gxGroup["graphLabel"] = newGxLabel

    clues = VGroup(
        Tex("① {{$y=$}}$(${{$x$}}$-1)^2 (2${{$x$}}$+1)${{ 의 접선}}"),
        Tex("② 기울기 = {{12}}인 직선")
    ).arrange(DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2,aligned_edge=LEFT).to_edge(RIGHT).shift(UP+LEFT*0.5)
    result = pointerBuilder("$x$절편", clues, arrow_len=3)
    scene.play(TransformFromCopy(fxGroup["graphLabel"], clues[0]))
    scene.play(TransformFromCopy(gxGroup["graphLabel"].get_part_by_tex("12"), clues[1]))
    scene.play(Create(result))

    fx = Tex("$f${{$(x)=$}}$(${{$x$}}$-1)^2 (2${{$x$}}$+1)$").move_to(clues[0])
    scene.play(FadeOut(Group(clues[1], result)),
               TransformMatchingTex(clues[0], fx, shift=UP))

    decomposedFxRight, fPrime = calculatefPrime(scene, fx)

    fPrime += MathTex("={{12}}").set_color_by_tex("12", YELLOW).next_to(fPrime[1])
    scene.play(Wiggle(gxGroup["graphLabel"].get_part_by_tex("12")))
    scene.play(TransformFromCopy(gxGroup["graphLabel"].get_part_by_tex("12"), fPrime[2]))

    scene.play(FadeOut(Group(fx, decomposedFxRight, fPrime[0])), FadeToColor(fPrime[-1], WHITE))

    x2, contact, contactLine = findContactX(scene, fxGroup, fPrime)
    contactLabel = findContactY(scene, fxGroup, x2, contact)

    alter2forX = MathTex("2").scale(gxGroup.getScaleRatio()*gxGroup.texScaleRatio).move_to(gxGroup["graphLabel"].get_part_by_tex("x"))
    alter5forY = MathTex("5").scale(gxGroup.getScaleRatio()*gxGroup.texScaleRatio).move_to(gxGroup["graphLabel"].get_part_by_tex("y"))
    scene.play(FadeOut(fxGroup["graph"]),
               AnimationGroup(AnimationGroup(TransformFromCopy(contactLabel.get_part_by_tex("2"), alter2forX),
                                             TransformFromCopy(contactLabel.get_part_by_tex("5"), alter5forY)),
                              AnimationGroup(gxGroup["graphLabel"].get_part_by_tex("x").animate.become(alter2forX),
                                             gxGroup["graphLabel"].get_part_by_tex("y").animate.become(alter5forY)),
                              lag_ratio=0.5))
    scene.remove(alter2forX, alter5forY)
    fxGroup.remove("graph")

    kVal = MathTex(r"k={{ \dfrac{19}{12} }}").scale(gxGroup.getScaleRatio()*gxGroup.texScaleRatio).move_to(gxGroup["graphLabel"])
    scene.play(Transform(gxGroup["graphLabel"], kVal))

    gxGroup.buildDotOnAxLabel(KMIN, label=MathTex(r"\dfrac{19}{12}").scale(0.8), labelKey="newLabelOnK", buff=1)

    scene.play(FadeOut(Group(contact, contactLine, contactLabel, fxGroup["labelOn2"])),
               AnimationGroup(TransformFromCopy(gxGroup["graphLabel"], gxGroup["newLabelOnK"]),
                              gxGroup["labelOnK"].animate.become(gxGroup["newLabelOnK"]),
                              lag_ratio=0.3))
    scene.remove(gxGroup["labelOnK"])
    gxGroup.remove("labelOnK")
    fxGroup.remove("labelOn2")
    kMin = pointerBuilder("$k$의 최솟값", gxGroup["newLabelOnK"], arrow_len=2)
    scene.play(Create(kMin))

    return kMin["tex"], VGroup(fxGroup, gxGroup, kMin["arrow"])

def finalAnswer(scene: Scene, kMin, toFadeOut):
    kMinCopy = kMin.copy().to_corner(UR).shift(LEFT*2+DOWN)
    kVal = MathTex(r"=\dfrac{19}{12}").next_to(kMinCopy)
    scene.play(Transform(kMin, kMinCopy), FadeIn(kVal))
    scene.play(FadeOut(toFadeOut), FadeIn(TEXTS, shift=LEFT))

    ul = Underline(VGroup(TEXTS[6].get_part_by_tex(r"$k$의 최솟값이 "),
                          TEXTS[6].get_part_by_tex(r"$\dfrac{q}{p}$")), color=YELLOW)
    scene.play(Create(ul))

    texPoverQ = MathTex(r"\dfrac{q}{p}").move_to(kMin, aligned_edge=RIGHT)
    scene.play(FadeOut(ul), 
               AnimationGroup(TransformFromCopy(TEXTS[6].get_part_by_tex(r"$\dfrac{q}{p}$"), texPoverQ),
               kMin.animate.become(texPoverQ), lag_ratio=0.5))
    scene.remove(texPoverQ)

    ans = VGroup(
        MathTex("p=19"),
        MathTex("q=12")
    ).arrange(DOWN, aligned_edge=LEFT).move_to(kMin, aligned_edge=LEFT)
    scene.play(ReplacementTransform(VGroup(kMin, kVal), ans))

    scene.play(FadeToColor(TEXTS[6].get_part_by_tex("$a$"), YELLOW),
               FadeToColor(TEXTS[6].get_part_by_tex("$+p+q$"), YELLOW))

    aSlices = searchShapesInTex(TEXTS[2], MathTex(r"a"))
    aTex = VGroup(*[TEXTS[2][0][i] for i in aSlices])
    oneTex = VGroup(*[MathTex("1").scale(0.7).set_color(YELLOW).move_to(a.get_center()) for a in aTex])
    scene.play(FadeToColor(TEXTS[6].get_part_by_tex("$+p+q$"), WHITE),
               FadeToColor(aTex, YELLOW))
    
    ans += MathTex("a=1").set_color(YELLOW).next_to(ans[-1], DOWN)
    scene.remove(ans[-1])
    scene.play(Transform(aTex, oneTex))
    scene.play(Write(ans[-1]))

    finalAns = MathTex(r"\therefore a+p+q = 32").next_to(ans, DOWN*2, aligned_edge=RIGHT)
    scene.play(FadeToColor(Group(TEXTS[6].get_part_by_tex("$a$"), oneTex, ans), WHITE),
               Write(finalAns))