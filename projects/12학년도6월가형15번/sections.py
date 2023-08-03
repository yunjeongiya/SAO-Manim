from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene):
    #1
    scene.add(TEXTS)

def describeProblem(scene:Scene):
    #2
    ul = Underline(TEXTS[1].get_part_by_tex("서로 접하고 크기가 같은 원 3개"), color=YELLOW)
    scene.play(Create(ul), FadeIn(CIRCLES.set_color(YELLOW)))
    #3
    ul2 = VGroup(
        Underline(TEXTS[1].get_part_by_tex("세 원의")),
        Underline(TEXTS[2].get_part_by_tex("중심을 꼭짓점으로 하는 정삼각형"))
    ).set_color(MINT)
    scene.play(Create(ul2), FadeIn(TRIANGLE.set_color(MINT)))
    #4
    ul3 = Underline(TEXTS[3].get_part_by_tex("정삼각형의 내부에 만들어지는 7개의 영역"), color=YELLOW)
    numbers = VGroup(*[Tex(str(i+1), color=YELLOW).scale(0.5).move_to(PARTS[i+1]) for i in range(7)])
    scene.play(FadeOut(CIRCLES, TRIANGLE, ul, ul2),
               Create(ul3))
    numbers[0].shift(UP*0.1)
    numbers[4].shift(UP*0.2)
    numbers[5].shift(DL*0.2)
    numbers[6].shift(DR*0.2)
    scene.play(Create(numbers), run_time=4)

    scene.remove(ul3)
    return numbers

def describeCircularPermutation(scene:Scene):
    texts = VGroup(
        Text("원순열", font=GOTHIC),
        Text("① 원순열 아니라고 생각하고 배열", font=GOTHIC),
        Text("② 한 바퀴 일치하는 횟수로 나누기", font=GOTHIC)
    ).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).scale(TEX_SCALE).next_to(TEXTS)
    arrow = Arrow(stroke_width=4, tip_length=0.15).scale(0.3).next_to(texts[0])
    equation = MathTex("(n-1)!").scale(0.8).next_to(arrow)
    #5
    scene.play(Write(texts[0]))
    #6
    scene.play(GrowArrow(arrow), Write(equation))
    #7
    scene.play(FadeOut(arrow, equation), Write(texts[1]))
    scene.play(Write(texts[2]))

    return texts

def countCasesByColoring(scene:Scene, toFadeOut:VMobject):
    #8
    partsGroup = VGroup(
        *[VGroup(*[PARTS.copy() for _ in range(3)]).arrange(RIGHT) for _ in range(2)]
    ).arrange(DOWN)
    scene.play(FadeOut(toFadeOut),
               TransformFromCopy(PARTS, partsGroup[0][0]))
    #9
    partsGroupCopy = partsGroup.copy()
    scene.play(ColorPartsBySequence(partsGroup[0][0][1:], (YELLOW, MINT, PURE_RED, VIOLET, ORANGE, PURE_GREEN, PURE_BLUE)))
    #10
    scene.play(TransformFromCopy(partsGroupCopy[0][0], partsGroup[0][1]))
    scene.play(ColorPartsBySequence(partsGroup[0][1][1:], (ORANGE, VIOLET, YELLOW, PURE_GREEN, PURE_BLUE, PURE_RED, MINT), lag_ratio=0, run_time=1))
    scene.play(TransformFromCopy(partsGroupCopy[0][1], partsGroup[0][2]))
    scene.play(ColorPartsBySequence(partsGroup[0][2][1:], (PURE_GREEN, ORANGE, PURE_RED, YELLOW, MINT, PURE_BLUE, VIOLET), lag_ratio=0, run_time=1))
    scene.play(TransformFromCopy(partsGroupCopy[0][2], partsGroup[1][2]))
    scene.play(ColorPartsBySequence(partsGroup[1][2][1:], (YELLOW, VIOLET, MINT, PURE_RED, PURE_BLUE, ORANGE, PURE_GREEN), lag_ratio=0, run_time=1))
    scene.play(TransformFromCopy(partsGroupCopy[1][2], partsGroup[1][1]))
    scene.play(ColorPartsBySequence(partsGroup[1][1][1:], (YELLOW, PURE_RED, VIOLET, MINT, PURE_GREEN, PURE_BLUE, ORANGE), lag_ratio=0, run_time=1))
    scene.play(TransformFromCopy(partsGroupCopy[1][1], partsGroup[1][0]))
    scene.play(ColorPartsBySequence(partsGroup[1][0][1:], (PURE_BLUE, PURE_RED, VIOLET, ORANGE, YELLOW, MINT, PURE_GREEN), lag_ratio=0, run_time=1))
    #11
    scene.play(FadeOut(partsGroup[0][1:], partsGroup[1][0]))
    #12
    scene.play(Rotate(partsGroup[1][1], angle=2*PI/3, about_point=partsGroup[1][1][0].get_center()),
               Rotate(partsGroup[1][2], angle=4*PI/3, about_point=partsGroup[1][2][0].get_center()))
    #13
    selectedPartsGroup = VGroup(partsGroup[0][0], partsGroup[1][1], partsGroup[1][2])
    scene.play(selectedPartsGroup.animate.arrange(RIGHT))
    selectedPartsGroupCopy = VGroup(partsGroupCopy[0][0].move_to(partsGroup[0][0]), 
                                    partsGroupCopy[1][1].move_to(partsGroup[1][1]), 
                                    partsGroupCopy[1][2].move_to(partsGroup[1][2]))
    #14
    scene.play(selectedPartsGroup.animate.set_fill(opacity=0))
    selectedPartsGroup.become(selectedPartsGroupCopy) #회전되어 있는 것 되돌리려고
    #15
    sevenFactorial = MathTex(r"7!{{\over}}{{3}}").next_to(selectedPartsGroup[0], DOWN)
    scene.play(ColorPartsBySequence(selectedPartsGroup[0][1:], (YELLOW, MINT, PURE_RED, VIOLET, ORANGE, PURE_GREEN, PURE_BLUE)))
    scene.play(Write(sevenFactorial[0]))
    #16
    copy = selectedPartsGroup[0].copy().move_to(selectedPartsGroup[1])
    scene.play(TransformFromCopy(selectedPartsGroup[0], copy))
    selectedPartsGroup[1].become(copy)
    scene.remove(copy)
    scene.play(Rotate(selectedPartsGroup[1], angle=-2*PI/3, about_point=selectedPartsGroup[1][0].get_center()))
    #17
    copy = selectedPartsGroup[1].copy().move_to(selectedPartsGroup[2])
    scene.play(TransformFromCopy(selectedPartsGroup[1], copy))
    selectedPartsGroup[2].become(copy)
    scene.remove(copy)
    scene.play(Rotate(selectedPartsGroup[2], angle=-2*PI/3, about_point=selectedPartsGroup[2][0].get_center()))
    #18
    three = MathTex("3")
    arrow = Arrow(stroke_width=4, tip_length=0.15).scale(0.3)
    one = MathTex("1")
    VGroup(three, arrow, one).arrange(RIGHT).next_to(selectedPartsGroup, DOWN)
    scene.play(Write(three))
    scene.play(GrowArrow(arrow), Write(one), 
               Rotate(selectedPartsGroup[1], angle=2*PI/3, about_point=selectedPartsGroup[1][0].get_center()),
               Rotate(selectedPartsGroup[2], angle=-2*PI/3, about_point=selectedPartsGroup[2][0].get_center()))
    #19
    scene.play(ReplacementTransform(VGroup(three, arrow, one), sevenFactorial[1:]),
               selectedPartsGroup[1].animate.move_to(selectedPartsGroup[0]),
               selectedPartsGroup[2].animate.move_to(selectedPartsGroup[0]))
    #20
    scene.play(selectedPartsGroup.animate.move_to(PARTS).set_fill(opacity=0),
               sevenFactorial.animate.next_to(PARTS).shift(RIGHT*2),
               FadeIn(TEXTS))
    scene.remove(selectedPartsGroup)
    #21
    calculatedSevenFactorial = MathTex(r"5040{{\over}}{{3}}").move_to(sevenFactorial)
    scene.play(TransformMatchingTex(sevenFactorial, calculatedSevenFactorial))
    #22
    scene.play(Transform(calculatedSevenFactorial, MathTex("1680").move_to(calculatedSevenFactorial)))
    scene.play(FadeToColor(OPTIONS[1], YELLOW))