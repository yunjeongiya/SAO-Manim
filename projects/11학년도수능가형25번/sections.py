from manim import *
from consts import *
from utils import *

def questionSection(scene):
    texts = Group(TITLE.to_edge(UP),
                  TEXT1.next_to(TITLE, DOWN, aligned_edge = LEFT),
                  TEXT2.next_to(TEXT1, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(RIGHT*0.5),
                  SurroundingRectangle(TEXT2, buff=0.2, color = WHITE).set_stroke(width=2),
                  TEXT3.next_to(TEXT2, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(LEFT*0.5),
                  Eq.next_to(TEXT3, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(RIGHT),
                  TEXT4.next_to(Eq, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(LEFT),
                  ).to_edge(LEFT)
    scene.add(texts)
        
    cubesGroup = CubesGroup(6).scale_to_fit_width(config.frame_width/3).next_to(texts, RIGHT).shift(DOWN*0.5)

    cubesGroup.popEvens()
    cubesGroup.popEvens()

    scene.add(cubesGroup.rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP))
        
    # alter : 전체 add 먼저 하고 pop 한 뒤 지우는 방식
    # *안넣으면 안지워짐, *안넣고 FadeOut이나 Shift는 적용됨... 왜지?
    # self.remove(*popEvens(cubes, CUBES_NUM))

    scene.wait()
    scene.remove(cubesGroup)

    return texts

def describeBaseSituation(scene, texts):
    scene.play(Circumscribe(texts[1].get_part_by_tex("크기가 같은 정육면체 모양의 블록"), fade_out=True))
    cubesGroup = CubesGroup(3).scale_to_fit_width(config.frame_width/3).next_to(texts, RIGHT).shift(DOWN*0.5).rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP)
    for i in range(1, 4):
        cubesGroup.cubes[i].set_fill_color(YELLOW)
        scene.play(Stack1ColCubes(cubesGroup, i, DOWN),
                   Circumscribe(texts[1].get_part_by_tex(str(i)+"열에 "+str(i)+"개"), fade_out=True))
        cubesGroup.cubes[i].set_fill_color(GREY)
    scene.play(Group(cubesGroup.cubes[:4], cubesGroup.labels[:4], cubesGroup.axes).animate.scale(1/4, about_point=cubesGroup.axes.c2p(0, 0, 0)))
    cubesGroup.addCols(13)
    scene.play(AnimationGroup(StackCubes(cubesGroup, 4, 16, run_time=2), FadeIn(cubesGroup.cdots), lag_ratio=0.8))
    return cubesGroup

def describeEvenIterate(scene, texts, cubesGroup):
    underline = VGroup(Underline(texts[1].get_part_by_tex("블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음\\")),
                       Underline(texts[1].get_part_by_tex("시행을 반복한다."))).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(FadeOut(underline))

    while len(cubesGroup.getEvenCols()) > 0:
        box = SurroundingRectangle(texts[2].get_part_by_tex("블록의 개수가 짝수인 각 열")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(box))
        scene.play(cubesGroup.getEvenCols().animate.set_fill_color(YELLOW), cubesGroup.getOddCols().animate.set_fill_color(GREY))
        scene.play(FadeOut(box))
        underline2 = Underline(texts[2].get_part_by_tex("만큼의 블록을 그 열에서 들어낸다.")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(underline2))
        evens = cubesGroup.popEvens()
        scene.play(evens.animate.shift(UP*0.3)) #or 콘티에 나온 대로 두번 깜빡이고 삭제 (Fadeout)
        scene.play(FadeOut(evens, shift=UP))
        scene.play(FadeOut(underline2))

    return cubesGroup

def descreibeEq(scene, text, eq, cubesGroup):
    scene.play(cubesGroup.cubes[:17].animate.set_fill_color(GREY))
    underline = VGroup(Underline(text.get_part_by_tex(r"1열부터 $m$열까지\\")),
                       Underline(text.get_part_by_tex(r"남아 있는 블록의 개수의 합을 $f(m)$"))).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(cubesGroup.cubes[:17].animate.set_fill_color(YELLOW))
    circle = Circle(color=YELLOW).scale(0.2).move_to(cubesGroup.labels[-1][0])
    scene.play(Create(circle))
    fend = MathTex("f(","16",")").next_to(cubesGroup, DOWN)
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], fend[1]))
    scene.play(Write(fend[0]), Write(fend[2]))
    scene.play(FadeOut(underline), FadeOut(circle), FadeOut(fend), cubesGroup.cubes[:17].animate.set_fill_color(GREY))
    eqbox = SurroundingRectangle(eq).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(eqbox))
    scene.play(Indicate(eq.get_part_by_tex(r"^{n+1}")),
               Indicate(eq.get_part_by_tex(r"^{n}")),
               Indicate(eq.get_part_by_tex(r"^{n+2}")))
    return eqbox

def iteratingMore(scene:Scene, texts, cubesGroup, eqbox):
    eq = texts[5]
    scene.play(FadeOut(texts[0:5], texts[6], eqbox), eq.animate.to_edge(UP).scale(1.5),
               Group(cubesGroup.cubes[:17], cubesGroup.labels[:17], cubesGroup.axes)
               .animate.to_corner(DL).shift(DOWN*0.5).rotate(20*DEGREES, axis=UP).scale_to_fit_height((config.frame_height-1)/2))
    fend = MathTex("f(","16",")").next_to(eq, DOWN*2).shift(LEFT)
    scene.play(Write(fend))
    potentialTex = twoPotentialTexBuilder(4).move_to(fend[1])
    scene.play(Transform(fend[1], potentialTex))

    cubesGroup.addCols(16)
    scene.play(StackCubes(cubesGroup, 17, 32, None, run_time=2))
    potentialTex = twoPotentialTexBuilder(5).move_to(fend[1])

    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], potentialTex))
    scene.play(Transform(fend[1], potentialTex), FadeOut(potentialTex))
    fadeOutAllEvens(cubesGroup, scene)
    scene.play(cubesGroup.cubes[:33].animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)).set_fill_color(GREY),
               Group(cubesGroup.labels[:33], cubesGroup.axes).animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    
    cubesGroup.addCols(32)
    scene.play(StackCubes(cubesGroup, 33, 64, None, run_time=2))
    potentialTex = twoPotentialTexBuilder(6).move_to(fend[1])
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], potentialTex))
    scene.play(Transform(fend[1], potentialTex), FadeOut(potentialTex))
    fadeOutAllEvens(cubesGroup, scene)

    return fend

def neglectEventhCols(scene, cubesGroup, fend):
    potentialTex4 = twoPotentialTexBuilder(4).move_to(fend[1])
    potentialTex5 = twoPotentialTexBuilder(5).move_to(fend[1])
    potentialTex6 = twoPotentialTexBuilder(6).move_to(fend[1])

    scene.play(cubesGroup.cubes[-1].animate.set_fill_color(GREY), 
               Transform(fend[1][1], potentialTex4[1]),
               cubesGroup.cubes[:17].animate.set_fill_color(YELLOW))
    scene.play(Transform(fend[1][1], potentialTex5[1]),
               cubesGroup.cubes[:33].animate.set_fill_color(YELLOW))
    scene.play(Transform(fend[1][1], potentialTex6[1]),
               cubesGroup.cubes[:65].animate.set_fill_color(YELLOW))
    
    triangle = TriangleSpanningCubes(cubesGroup, 16)
    scene.play(Transform(fend[1][1], potentialTex4[1]),
               cubesGroup.cubes[17:65].animate.set_fill_color(GREY),
               Create(triangle))
    scene.play(Transform(fend[1][1], potentialTex5[1]),
               cubesGroup.cubes[17:33].animate.set_fill_color(YELLOW),
               Transform(triangle, TriangleSpanningCubes(cubesGroup, 32)))
    scene.play(Transform(fend[1][1], potentialTex6[1]),
                cubesGroup.cubes[33:65].animate.set_fill_color(YELLOW),
                Transform(triangle, TriangleSpanningCubes(cubesGroup, 64)))
    
    scene.play(FadeOut(triangle), cubesGroup.cubes[:65].animate.set_fill_color(GREY))

    scene.play(cubesGroup.getOddthCols().animate.set_fill_color(YELLOW),
               cubesGroup.getEventhCols().animate.set_fill_color(PURE_GREEN))
    
    scene.play(FadeOut(cubesGroup.getEventhCols()))

def iteratingMoreOnlyWithOddCols(scene, cubesGroup, fend):
    potentialTex7 = twoPotentialTexBuilder(7).move_to(fend[1])
    potentialTex8 = twoPotentialTexBuilder(8).move_to(fend[1])

    scene.play(Group(cubesGroup.getOddthCols(), cubesGroup.axes, cubesGroup.cubes[0])
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)),
               FadeOut(cubesGroup.labels[:65]))
    cubesGroup.addCols(64)
    scene.play(FadeIn(cubesGroup.getOddthCols(65, 128).set_fill_color(YELLOW)),
               Transform(fend[1][1], potentialTex7[1]))

    scene.play(Group(cubesGroup.getOddthCols(), cubesGroup.axes, cubesGroup.cubes[0])
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(128)
    scene.play(FadeIn(cubesGroup.getOddthCols(129, 256).set_fill_color(YELLOW)),
               Transform(fend[1][1], potentialTex8[1]))
    

def iteratingMoreWithOutFend(scene, cubesGroup, fend):
    scene.play(Group(cubesGroup.getOddthCols(), cubesGroup.axes, cubesGroup.cubes[0])
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)),
               FadeOut(fend))
    cubesGroup.addCols(256)
    scene.play(FadeIn(cubesGroup.getOddthCols(257, 512).set_fill_color(YELLOW)))
    scene.play(Group(cubesGroup.getOddthCols(), cubesGroup.axes, cubesGroup.cubes[0])
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(512)
    scene.play(FadeIn(cubesGroup.getOddthCols(513, 1024).set_fill_color(YELLOW)))

def comparingTriangles(scene, cubesGroup, fend):
    smallTriangle = TriangleSpanningCubes(cubesGroup, 128)
    bigTriangle = TriangleSpanningCubes(cubesGroup, 256, PURE_BLUE).set_z_index(-1)

    f2n_1 = MathTex("f(", r"2^{n+1}", ")").set_color_by_tex(r"2^{n+1}", BLUE).to_edge(RIGHT).shift(LEFT*0.1)
    f2n = MathTex("f(", r"2^n", ")").set_color_by_tex(r"2^n", RED).next_to(f2n_1, LEFT*4)
    
    f2nLen = MathTex("1",color=RED).next_to(f2n, DOWN)
    f2n_1Len = MathTex("2",color=BLUE).next_to(f2n_1, DOWN)
    f2nArea = MathTex("1",color=RED).next_to(f2nLen, DOWN)
    f2n_1Area = MathTex("4",color=BLUE).next_to(f2n_1Len, DOWN)
    
    lenRatio = Text("길이비", font="NanumBarunGothic").scale_to_fit_height(f2n.height*0.8).next_to(f2nLen, LEFT*2.2)
    areaRatio = Text("넓이비", font="NanumBarunGothic").scale_to_fit_height(f2n.height*0.8).next_to(f2nArea, LEFT*2.2)
    colon = MathTex(":").next_to(lenRatio, RIGHT*6)
    colon2 = MathTex(":").next_to(areaRatio, RIGHT*6)
    equal = MathTex("=").next_to(f2n, RIGHT*0.5)

    scene.play(Create(smallTriangle), FadeOut(fend))
    scene.play(TransformFromCopy(smallTriangle, f2n))
    scene.play(Create(bigTriangle))
    scene.play(TransformFromCopy(bigTriangle, f2n_1))
    scene.play(FadeOut(cubesGroup.getOddthCols()), Write(lenRatio)) #FadeOut(cubesGroup) 하면 화면에 안나타나 있던 것들이 보였다가 사라짐
    scene.play(Write(f2nLen), Write(f2n_1Len), Write(colon))
    scene.play(Write(areaRatio))
    scene.play(TransformFromCopy(f2nLen, f2nArea), TransformFromCopy(f2n_1Len, f2n_1Area), Write(colon2))
    scene.play(FadeOut(Group(lenRatio, areaRatio, colon, colon2, f2nLen, f2n_1Len)),
               f2nArea.animate.next_to(f2n_1, LEFT*0.5), f2n_1Area.animate.next_to(f2n, LEFT*0.5))
    scene.remove(smallTriangle, bigTriangle)
    
    return Group(f2n, f2n_1, f2nArea, f2n_1Area, equal)

def calculateEq(scene, questionEq, f2nEq):
    scene.play(questionEq.animate.move_to(ORIGIN+UP).scale_to_fit_height(f2nEq.height*2),
               f2nEq[0].animate.shift(UP*3).set_color(WHITE),
               f2nEq[3:].animate.shift(UP*3).set_color(WHITE),
               f2nEq[1].animate.shift(LEFT*0.5+UP*3).set_color(WHITE), FadeOut(f2nEq[2])) 
    scene.play(FadeToColor(VGroup(questionEq.get_part_by_tex(r"^{n+1}"), questionEq.get_part_by_tex(r"^{n}"), questionEq.get_part_by_tex(r"^{n+2}")), YELLOW))

    #동일한 수식 여러개 있어서 get_part_by_tex 사용 못하고 인덱스로 참조 -> 텍스트 변경 시 문제 발생 가능(종속적)
    f2n_1Square = SurroundingRectangle(questionEq[1:4], color=PURE_RED)
    f2nSquare = SurroundingRectangle(questionEq[5:8], color=PURE_RED)
    f2n_2Square = SurroundingRectangle(questionEq[9:12], color=PURE_RED)
    starEq = MathTex(r"{4",r"\bigstar",r" - ",r"\bigstar}",r"\over", r"{4\cdot", r"4", r"\bigstar}").set_color_by_tex('igsta', RED).next_to(questionEq, DOWN).shift(DOWN)

    arrow = Arrow(f2nSquare.get_edge_center(DOWN), starEq[3], buff=0, color=PURE_RED, tip_length=0.3)
    arrow2 = Arrow(f2n_1Square.get_edge_center(DOWN), starEq[1], buff=0, color=PURE_RED, tip_length=0.3)
    arrow3 = Arrow(f2n_2Square.get_edge_center(DOWN), starEq[-1], buff=0, color=PURE_RED, tip_length=0.3)

    scene.play(Create(f2nSquare))
    scene.play(Create(arrow))
    scene.play(Write(starEq[3]))
    scene.play(Create(f2n_1Square), FadeOut(Group(f2nSquare, arrow)))
    scene.play(Create(arrow2), TransformFromCopy(starEq[3], starEq[1]))
    scene.play(Write(starEq[0]), Write(starEq[2]))
    scene.play(Create(f2n_2Square), FadeOut(Group(f2n_1Square, arrow2)))
    scene.play(Create(arrow3), TransformFromCopy(starEq[:2], starEq[-2:]))
    scene.play(Write(starEq.get_part_by_tex(r"\over")), Write(starEq.get_part_by_tex(r"4\cdot")))
    scene.play(FadeOut(Group(f2n_2Square, arrow3)))
    scene.play(Transform(starEq[-3:], MathTex("16 ",r"\bigstar").set_color_by_tex('igsta', RED).move_to(starEq[-3:])))
    scene.play(Transform(starEq[:4], MathTex("3 ",r"\bigstar").set_color_by_tex('igsta', RED).move_to(starEq[:4])))
    valOfQoverP = MathTex(r"{3}",r"\over",r"{16}").next_to(questionEq.get_part_by_tex("="), LEFT)
    scene.play(FadeOut(questionEq[:-4]), FadeOut(starEq.get_parts_by_tex("igsta")), FadeOut(f2nEq),
               ReplacementTransform(starEq[-3:], valOfQoverP.get_part_by_tex("16")),
               ReplacementTransform(starEq[:4], valOfQoverP.get_part_by_tex("3")),
               ReplacementTransform(starEq.get_part_by_tex(r"\over"), valOfQoverP.get_part_by_tex(r"\over")))
    pqEq = Tex("$p$", " = ", "16", r"\\", "$q$", " = ", "3", font_size=50).to_edge(RIGHT)
    scene.play(Write(pqEq.get_parts_by_tex("=")), Write(pqEq.get_parts_by_tex("\\")),
               FadeOut(Group(questionEq[-2], questionEq.get_part_by_tex("="), valOfQoverP.get_part_by_tex(r"\over"))),
               ReplacementTransform(questionEq.get_part_by_tex(r"{{q}"), pqEq.get_part_by_tex("p")),
               ReplacementTransform(questionEq.get_part_by_tex(r"{p}}"), pqEq.get_part_by_tex("q")),
               ReplacementTransform(valOfQoverP.get_part_by_tex("3"), pqEq.get_part_by_tex("3")),
               ReplacementTransform(valOfQoverP.get_part_by_tex("16"), pqEq.get_part_by_tex("16")))
    return pqEq

def findFinalAnswer(scene, pqEq, texts):
    scene.play(FadeIn(texts.to_edge(LEFT), shift=RIGHT))

    answer = MathTex("p", "+", "q", "=", "19").next_to(pqEq, DOWN*2, aligned_edge=RIGHT)
    scene.play(Circumscribe(texts[-1][1], fade_out=True))
    scene.play(TransformFromCopy(texts[-1][1], answer[:3]))

    pVal = MathTex("16").move_to(answer.get_part_by_tex("p")).shift(UP*0.1)
    qVal = MathTex("3").move_to(answer.get_part_by_tex("q")).shift(UP*0.1)
    scene.play(TransformFromCopy(pqEq.get_part_by_tex("16"), pVal),
               FadeOut(answer.get_part_by_tex("p")),
               TransformFromCopy(pqEq.get_part_by_tex("3"), qVal),
               FadeOut(answer.get_part_by_tex("q")))
    scene.play(Write(answer.get_part_by_tex("=")), Write(answer.get_part_by_tex("19")))

def temp(scene):
    f2n_1 = MathTex("f(", r"2^{n+1}", ")").set_color_by_tex(r"2^{n+1}", BLUE).to_edge(RIGHT).shift(LEFT*0.1)
    f2n = MathTex("f(", r"2^n", ")").set_color_by_tex(r"2^n", RED).next_to(f2n_1, LEFT*4)
    
    f2nLen = MathTex("1",color=RED).next_to(f2n, DOWN)
    f2n_1Len = MathTex("2",color=BLUE).next_to(f2n_1, DOWN)
    f2nArea = MathTex("1",color=RED).next_to(f2nLen, DOWN)
    f2n_1Area = MathTex("4",color=BLUE).next_to(f2n_1Len, DOWN)
    
    lenRatio = Text("길이비", font="NanumBarunGothic").scale_to_fit_height(f2n.height*0.8).next_to(f2nLen, LEFT*2.2)
    areaRatio = Text("넓이비", font="NanumBarunGothic").scale_to_fit_height(f2n.height*0.8).next_to(f2nArea, LEFT*2.2)
    colon = MathTex(":").next_to(lenRatio, RIGHT*6)
    colon2 = MathTex(":").next_to(areaRatio, RIGHT*6)
    equal = MathTex("=").next_to(f2n, RIGHT*0.5)

    scene.add(f2n, f2n_1, lenRatio, f2nLen, f2n_1Len, colon, areaRatio)
    scene.play(TransformFromCopy(f2nLen, f2nArea), TransformFromCopy(f2n_1Len, f2n_1Area), Write(colon2))
    scene.play(FadeOut(Group(lenRatio, areaRatio, colon, colon2, f2nLen, f2n_1Len)),
               f2nArea.animate.next_to(f2n_1, LEFT*0.5), f2n_1Area.animate.next_to(f2n, LEFT*0.5))
    
    return Group(f2n, f2n_1, f2nArea, f2n_1Area, equal)

class FinalPartTest(ThreeDScene):
    count = 0
    def play(self, *args, **kwargs):
        args = list(args)
        args.append(Wait(2)) # append 하는거라 앞 애니메이션들이랑 동시에 진행되므로 1 초과해야 추가로 기다림
        super().play(*args, **kwargs)
        self.next_section(str(self.count))
        self.count += 1

    def construct(self):
        texts = questionSection(self)
        self.remove(texts)
        originalTexts = texts.copy()

        f2nEq = temp(self)
        
        pqEq = calculateEq(self, texts[5].to_edge(UP).scale(1.5), f2nEq)
        findFinalAnswer(self, pqEq, originalTexts)