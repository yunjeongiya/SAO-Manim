from manim import *
from consts import *
from utils import *

def showProblem(scene:Scene) :
    scene.add(TEXTS)

def showExample(scene:Scene) :
    ul = Underline(TEXTS[1].get_part_by_tex("직사각형 모양의 잔디밭에 산책로"), color=YELLOW)
    scene.play(Create(ul))

    ul2 = VGroup(Underline(TEXTS[2].get_part_by_tex("반지름의 길이가 같은 원 8개가 서로"), color=YELLOW),
                 Underline(TEXTS[3].get_part_by_tex("외접"), color=YELLOW))
    scene.play(FadeOut(ul), 
               Create(ul2), FadeToColor(TRAILS, YELLOW))
    
    ul = Underline(TEXTS[5].get_part_by_tex("A 지점에서 출발"), color=YELLOW)
    scene.play(FadeOut(ul2), FadeToColor(TRAILS, WHITE),
               Create(ul), FadeToColor(A, YELLOW))
    
    ul2 = VGroup(Underline(VGroup(TEXTS[5].get_part_by_tex("최단 거리"), TEXTS[5].get_part_by_tex("로 B 지점에")), color=MINT),
                 Underline(TEXTS[6].get_part_by_tex("도착"), color=MINT))
    scene.play(Create(ul2), FadeToColor(B, MINT))

    path = VGroup(
        TRAILS[1][0]["UL"].copy(),
        TRAILS[0][0]["DR"].copy(),
        TRAILS[0][1]["DL"].copy(),
        TRAILS[0][1]["DR"].copy(),
        TRAILS[0][2]["UL"].copy(),
        TRAILS[0][2]["UR"].copy(),
        TRAILS[0][3]["DL"].copy(),
        TRAILS[0][3]["DR"].copy()
    ).set_color(VIOLET)
    scene.play(Create(path), run_time=4)

    return VGroup(ul, ul2, path)

def describeShortestDistanceConcept(scene:Scene, toFadeOut:VGroup) :
    box = SurroundingRectangle(TEXTS[5].get_part_by_tex("최단 거리"))
    scene.play(FadeOut(toFadeOut), FadeToColor(VGroup(A, B), WHITE),
               Create(box))
    
    row = 4
    col = 6
    
    grid = VDict({
        "rows" : VGroup(*[VGroup(*[Row(i,j) for i in range(col - 1)]) for j in range(row, 0, -1)]),
        "cols" : VGroup(*[VGroup(*[Col(i,j) for i in range(col)]) for j in range(row, 1, -1)])
    })
    grid["A"] = Tex("A").next_to(grid["rows"][0][0], LEFT)
    grid["B"] = Tex("B").next_to(grid["rows"][-1][-1], RIGHT)
    scene.play(FadeIn(grid.scale(0.8).next_to(TRAILS, RIGHT, buff=1.5)))

    path = VGroup(
        grid["rows"][0][0].copy(),
        grid["cols"][0][1].copy(),
        grid["rows"][1][1].copy(),
        grid["rows"][1][2].copy(),
        grid["cols"][1][3].copy(),
        grid["rows"][2][3].copy(),
        grid["rows"][2][4].copy(),
        grid["cols"][2][5].copy(),
    ).set_color(YELLOW)
    scene.play(Create(path), run_time=2)

    arrowPath = buildArrowPathFromPath(path, 0.5)
    scene.play(Transform(path, arrowPath))

    scene.play(path.animate.arrange(RIGHT, buff=0).next_to(grid, UP))
    
    path2 = VGroup(
        grid["cols"][0][0].copy(),
        grid["rows"][1][0].copy(),
        grid["cols"][1][1].copy(),
        grid["rows"][2][1].copy(),
        grid["rows"][2][2].copy(),
        grid["rows"][2][3].copy(),
        grid["cols"][2][4].copy(),
        grid["rows"][3][4].copy(),
    )
    arrowPath2 = buildArrowPathFromPath(path2, 0.5)
    alignedArrowPath2 = arrowPath2.copy().arrange(RIGHT, buff=0).next_to(grid, UP)
    scene.play(ChangeOrder(path, alignedArrowPath2, (1,0,3,4,2,5,7,6)))
    
    path.become(alignedArrowPath2)
    scene.play(Transform(path, arrowPath2))

    return VGroup(path, grid, box)

def findPath(scene:Scene, toFadeOut):
    scene.play(FadeOut(toFadeOut),
               FadeToColor(TRAILS, YELLOW))
    diaTrails = VGroup(
    *[VGroup(
        *[VDict({
            "UR": DRline(isLeft=False),
            "UL": URline(isLeft=True),
            "DL": DRline(isLeft=True),
            "DR": URline(isLeft=False),
            "UP" : Dot().move_to(UP),
            "DOWN" : Dot().move_to(DOWN),
            "LEFT" : Dot().move_to(LEFT),
            "RIGHT" : Dot().move_to(RIGHT)
        }) for _ in range(4)]).arrange(RIGHT, buff=-DEFAULT_DOT_RADIUS*2)
    for _ in range(2)]).arrange(DOWN, buff=-DEFAULT_DOT_RADIUS*2).scale(TEXT_SCALE).move_to(TRAILS)
    scene.play(ReplacementTransform(TRAILS, diaTrails.set_color(YELLOW)))

    trailsExpandScale = 1.3
    scene.play(FadeOut(TEXTS[:4], TEXTS[5:]),
               VGroup(diaTrails, A, B).animate.set_color(WHITE).move_to(ORIGIN).scale(trailsExpandScale))
    
    path = VGroup(
        diaTrails[1][0]["UL"].copy(),
        diaTrails[0][0]["DR"].copy(),
        diaTrails[0][1]["DL"].copy(),
        diaTrails[0][1]["DR"].copy(),
        diaTrails[0][2]["DL"].copy(),
        diaTrails[1][2]["UR"].copy(),
        diaTrails[1][3]["UL"].copy(),
        diaTrails[0][3]["DR"].copy()
    ).set_color(YELLOW)
    scene.play(Create(path), run_time=2)

    arrowPath = buildArrowPathFromPath(path, TEXT_SCALE*trailsExpandScale)
    scene.play(Transform(path, arrowPath))

    scene.play(path.animate.arrange(RIGHT, buff=0).next_to(diaTrails, DOWN))

    path2 = VGroup(
        diaTrails[1][0]["DL"].copy(),
        diaTrails[1][0]["DR"].copy(),
        diaTrails[1][1]["UL"].copy(),
        diaTrails[1][1]["UR"].copy(),
        diaTrails[1][2]["UL"].copy(),
        diaTrails[0][2]["DR"].copy(),
        diaTrails[0][3]["UL"].copy(),
        diaTrails[0][3]["UR"].copy()
    )
    arrowPath2 = buildArrowPathFromPath(path2, TEXT_SCALE*trailsExpandScale)
    alignedArrowPath2 = arrowPath2.copy().arrange(RIGHT, buff=0).next_to(diaTrails, DOWN)
    scene.play(ChangeOrder(path, alignedArrowPath2, (1,2,0,4,3,7,5,6)))
    path.become(alignedArrowPath2)

    scene.play(Transform(path, arrowPath2))

    alignedArrowPath3 = buildArrowPathFromPath(
        VGroup(diaTrails[0][0]["DL"].copy(),
               diaTrails[0][0]["UR"].copy(),
               diaTrails[0][1]["DL"].copy(),
               diaTrails[0][1]["DR"].copy(),
               diaTrails[0][2]["UL"].copy(),
               diaTrails[0][2]["DR"].copy(),
               diaTrails[0][3]["UL"].copy(),
               diaTrails[0][3]["DR"].copy()),
        TEXT_SCALE*trailsExpandScale).arrange(RIGHT, buff=0).next_to(diaTrails, DOWN)
    scene.play(Transform(path, alignedArrowPath2))
    scene.play(ChangeOrder(path, alignedArrowPath3, (0,3,4,1,5,6,7,2)))
    path.become(alignedArrowPath3)

    permutationEq = MathTex(r"8!{{\over}}{{3!}}{{5!}}").next_to(path, UR).shift(RIGHT)
    scene.play(Write(permutationEq.get_part_by_tex("8!")))
    scene.play(FadeIn(permutationEq.get_part_by_tex(r"\over")))
    scene.play(TransformFromCopy(path[:3], permutationEq.get_part_by_tex("3!").set_color(VIOLET)))
    scene.play(TransformFromCopy(path[3:], permutationEq.get_part_by_tex("5!").set_color(MINT)))

    arrowPath4 = buildArrowPathFromPath(
        VGroup(diaTrails[1][0]["DL"].copy(),
               diaTrails[1][0]["UR"].copy().shift(DOWN*2*TEXT_SCALE*trailsExpandScale),
               diaTrails[1][1]["UL"].copy().shift(DOWN*2*TEXT_SCALE*trailsExpandScale),
               diaTrails[1][1]["DR"].copy(),
               diaTrails[1][2]["DL"].copy(),
               diaTrails[1][2]["DR"].copy(),
               diaTrails[1][3]["UL"].copy(),
               diaTrails[0][3]["DR"].copy()),
        TEXT_SCALE*trailsExpandScale)
    alignedArrowPath4 = arrowPath4.copy().arrange(RIGHT, buff=0).next_to(diaTrails, DOWN)
    scene.play(FadeOut(permutationEq),
               ChangeOrder(path, alignedArrowPath4, (0,1,4,2,3,5,6,7)))
    path.become(alignedArrowPath4)
    
    scene.play(Transform(path, arrowPath4))

    scene.play(FadeToColor(path[1:3], PURE_RED))

    return path, diaTrails, trailsExpandScale

def generalizePath(scene:Scene, toFadeOut, diaTrails, trailsExpandScale):
    trailsToFadeOut = VGroup(diaTrails[0][0]["UL"], 
                             diaTrails[0][0]["UR"], 
                             diaTrails[0][0]["DL"], 
                             diaTrails[0][0]["UP"],
                             diaTrails[0][0]["LEFT"],  
                             diaTrails[1][3]["UR"],
                             diaTrails[1][3]["DL"],
                             diaTrails[1][3]["DR"],
                             diaTrails[1][3]["RIGHT"],
                             diaTrails[1][3]["DOWN"])
    scene.play(FadeOut(toFadeOut),
               FadeToColor(trailsToFadeOut, YELLOW))
    
    scene.play(FadeOut(trailsToFadeOut))

    scene.play(Indicate(diaTrails[0][2]["LEFT"],color=MINT,scale_factor=2),
               Indicate(diaTrails[1][2]["LEFT"],color=MINT,scale_factor=2))

    line = Line(diaTrails[1][0]["LEFT"].get_center(), diaTrails[0][3]["RIGHT"].get_center(), color=YELLOW)
    scene.play(Create(line))

    lines = VGroup(
        *[Line(start=UP*3, end=DOWN*3, color=MINT) for _ in range(7)]
    ).arrange(RIGHT, buff=1).scale(TEXT_SCALE*trailsExpandScale)
    scene.play(Create(lines))

    scene.play(Indicate(diaTrails[0][1]["UP"],color=MINT,scale_factor=2),
               Indicate(diaTrails[1][1]["UP"],color=MINT,scale_factor=2),
               Indicate(diaTrails[1][1]["DOWN"],color=MINT,scale_factor=2))

    scene.play(Indicate(diaTrails[0][2]["LEFT"],color=MINT,scale_factor=2),
               Indicate(diaTrails[1][2]["LEFT"],color=MINT,scale_factor=2))

    dot = diaTrails[0][2]["LEFT"].copy().set_color(MINT).scale(2).set_z_index(1)
    scene.play(FadeOut(line, lines), FadeIn(dot))
    
    trailPart1 = VGroup(diaTrails[1][0].copy(),
                        diaTrails[0][0]["DR"].copy(),
                        diaTrails[1][1]["UL"].copy(),
                        diaTrails[0][1].copy()).set_color(YELLOW)
    scene.play(FadeIn(trailPart1))

    trailPart2 = VGroup(diaTrails[0][2].copy(),
                        diaTrails[1][2]["UR"].copy(),
                        diaTrails[1][3]["LEFT"].copy(),
                        diaTrails[1][3]["UL"].copy(),
                        diaTrails[0][3].copy()).set_color(VIOLET)
    scene.play(FadeIn(trailPart2))

    dot2 = diaTrails[1][2]["LEFT"].copy().set_color(MINT).scale(2).set_z_index(1)
    scene.play(FadeOut(trailPart1, trailPart2, dot),
               FadeIn(dot2))
    
    trailPart3 = trailPart2.copy().rotate(PI).shift((LEFT*4+DOWN)*TEXT_SCALE*trailsExpandScale)
    scene.play(FadeIn(trailPart3))
    trailPart4 = trailPart1.copy().shift(RIGHT*4*TEXT_SCALE*trailsExpandScale)
    scene.play(FadeIn(trailPart4))

    scene.play(FadeOut(trailPart3, trailPart4, dot2))
    trailsToFadeOut.set_color(BLACK)
    ACopy = A.copy()
    BCopy = B.copy()
    smallDiaTrails = diaTrails.copy()
    VGroup(ACopy, BCopy, smallDiaTrails,
           trailPart1, trailPart2, trailPart3, trailPart4,
           dot, dot2).scale(2/3).to_corner(UL)
    trailsExpandScale *= 2/3
    scene.play(Transform(VGroup(A, B, diaTrails), VGroup(ACopy, BCopy, smallDiaTrails)))
    scene.play(FadeIn(trailPart1, trailPart2, dot))
    one = Tex("①")
    trailPart1Copy = trailPart1.copy()
    arrow = Arrow(max_tip_length_to_length_ratio=0.1).scale(0.5)
    trailPart2Copy = trailPart2.copy()
    VGroup(one, trailPart1Copy, arrow, trailPart2Copy).arrange(RIGHT).to_corner(UR)
    scene.play(Write(one))
    scene.play(TransformFromCopy(trailPart1, trailPart1Copy))
    scene.play(Create(arrow))
    scene.play(TransformFromCopy(trailPart2, trailPart2Copy))

    scene.play(FadeOut(trailPart1, trailPart2, dot),
               FadeIn(trailPart3, trailPart4, dot2))
    two = Tex("②")
    trailPart3Copy = trailPart3.copy().rotate(PI)
    arrow2 = arrow.copy()
    trailPart4Copy = trailPart4.copy()
    VGroup(two, trailPart3Copy, arrow2, trailPart4Copy).arrange(RIGHT).next_to(one, DOWN, aligned_edge=LEFT).shift(DOWN*2)
    scene.play(Write(two))
    trailPart3Temp = trailPart3.copy()
    scene.play(trailPart3Temp.animate.flip(RIGHT).move_to(trailPart3Copy))
    scene.remove(trailPart3Temp)
    scene.add(trailPart3Copy)
    scene.play(Create(arrow2))
    scene.play(TransformFromCopy(trailPart4, trailPart4Copy))
    
    arrowOntrailPart1 = Arrow(trailPart1Copy[0]["LEFT"], trailPart1Copy[3]["RIGHT"], buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.08)
    arrowOntrailPart4 = Arrow(trailPart4Copy[0]["LEFT"], trailPart4Copy[3]["RIGHT"], buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.08)
    aCountTex = Tex("{{$a$}} 가지").next_to(trailPart1Copy, DOWN)
    aCountTex2 = aCountTex.copy().next_to(trailPart4Copy, DOWN)
    scene.play(FadeOut(trailPart3, trailPart4, dot2),
               Create(arrowOntrailPart1), Create(arrowOntrailPart4))
    scene.play(Write(aCountTex), Write(aCountTex2))

    arrowOntrailPart2 = Arrow(trailPart2Copy[0]["LEFT"], trailPart2Copy[4]["RIGHT"], buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.08)
    arrowOntrailPart3 = Arrow(trailPart3Copy[0]["LEFT"], trailPart3Copy[4]["RIGHT"], buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.08)
    bCountTex = Tex("{{$b$}} 가지").next_to(trailPart2Copy, DOWN)
    bCountTex2 = bCountTex.copy().next_to(trailPart3Copy, DOWN)
    scene.play(Create(arrowOntrailPart2), Create(arrowOntrailPart3))
    scene.play(Write(bCountTex), Write(bCountTex2))
    
    trailParts = VDict({
        "nums" : VGroup(one, two),
        "arrows" : VGroup(arrow, arrow2),
        "left" : VDict({
            "a" : VDict({
                "trail" : trailPart1Copy,
                "arrow" : arrowOntrailPart1,
            }),
            "aCountTex" : aCountTex,
            "b" : VDict({
                "trail" : trailPart3Copy,
                "arrow" : arrowOntrailPart3,
            }),
            "bCountTex" : bCountTex2
        }),
        "right" : VDict({
            "b" : VDict({
                "trail" : trailPart2Copy,
                "arrow" : arrowOntrailPart2,
            }),
            "bCountTex" : bCountTex,
            "a" : VDict({
                "trail" : trailPart4Copy,
                "arrow" : arrowOntrailPart4,
            }),
            "aCountTex" : aCountTex2
        })
    })
    return trailParts, trailsExpandScale

def calculatePathCountsOfParts(scene:Scene, trailParts, diaTrails, trailsExpandScale):
    trailParts["left"].save_state()
    scene.play(FadeOut(trailParts["right"], trailParts["nums"], trailParts["arrows"], A, B, diaTrails),
               trailParts["left"].animate.to_edge(LEFT).set_color(WHITE))

    scene.play(VGroup(trailParts["left"]["a"]).animate.rotate(-PI/4),
               VGroup(trailParts["left"]["b"]).animate.rotate(-PI/4))
    
    pathOnA = buildArrowPathFromPath(VGroup(
        trailParts["left"]["a"]["trail"][0]["UL"].copy(),
        trailParts["left"]["a"]["trail"][0]["UR"].copy(),
        trailParts["left"]["a"]["trail"][2].copy(),
        trailParts["left"]["a"]["trail"][3]["DR"].copy(),
    ), trailsExpandScale*TEXT_SCALE, -PI/4)
    scene.play(Create(pathOnA))

    pathOnA2 = buildArrowPathFromPath(VGroup(
        trailParts["left"]["a"]["trail"][0]["UL"].copy(),
        trailParts["left"]["a"]["trail"][1].copy(),
        trailParts["left"]["a"]["trail"][3]["UL"].copy(),
        trailParts["left"]["a"]["trail"][3]["UR"].copy()
    ), trailsExpandScale*TEXT_SCALE, -PI/4).arrange(RIGHT).next_to(trailParts["left"]["a"], RIGHT).shift(RIGHT*2)
    scene.play(pathOnA.animate.arrange(RIGHT).next_to(trailParts["left"]["a"], RIGHT).shift(RIGHT*2))
    scene.play(ChangeOrder(pathOnA, pathOnA2, (0,3,1,2)))

    permutationEq = MathTex(r"4!{{\over}}3!").next_to(pathOnA, RIGHT).shift(RIGHT*2)
    scene.play(Write(permutationEq[0]))
    scene.play(Write(permutationEq[1]))
    scene.play(TransformFromCopy(pathOnA2[:3], permutationEq[2].set_color(MINT)))

    four = MathTex("4").move_to(permutationEq)
    scene.play(ReplacementTransform(permutationEq, four))

    aCountVal = four.copy().next_to(trailParts["left"]["aCountTex"][1], LEFT)
    scene.play(TransformFromCopyFadeOutTarget(four, aCountVal, trailParts["left"]["aCountTex"][0]))
    trailParts["left"]["aCountTex"][0].become(aCountVal)
    scene.remove(aCountVal)

    virtualTrack = VGroup(
        trailParts["left"]["b"]["trail"][0]["UL"].copy(),
        trailParts["left"]["b"]["trail"][0]["UP"].copy(),
        trailParts["left"]["b"]["trail"][0]["UR"].copy(),
    ).shift(RIGHT*trailsExpandScale*TEXT_SCALE*(2**(1/2))).set_color(YELLOW)
    scene.play(Create(virtualTrack))

    pathOnB = buildArrowPathFromPath(VGroup(
        trailParts["left"]["b"]["trail"][0]["UL"].copy(),
        trailParts["left"]["b"]["trail"][0]["UR"].copy(),
        trailParts["left"]["b"]["trail"][4]["DL"].copy(),
        trailParts["left"]["b"]["trail"][4]["DR"].copy()
    ), trailsExpandScale*TEXT_SCALE, -PI/4)
    scene.play(Create(pathOnB))

    pathOnB2 = buildArrowPathFromPath(VGroup(
        trailParts["left"]["b"]["trail"][0]["UL"].copy(),
        virtualTrack[0].copy(),
        virtualTrack[2].copy(),
        trailParts["left"]["b"]["trail"][4]["UR"].copy()
    ), trailsExpandScale*TEXT_SCALE, -PI/4).arrange(RIGHT).next_to(trailParts["left"]["b"], RIGHT).shift(RIGHT*2)
    scene.play(pathOnB.animate.arrange(RIGHT).next_to(trailParts["left"]["b"], RIGHT).shift(RIGHT*2))
    scene.play(ChangeOrder(pathOnB, pathOnB2, (0,2,3,1)))

    permutationEq = MathTex(r"{ 4!{{\over}}{{2!}}{{2!}} } -{{1}}").next_to(pathOnB, RIGHT).shift(RIGHT*2.9)
    scene.play(Write(permutationEq[0]))
    scene.play(Write(permutationEq[1]))
    scene.play(TransformFromCopy(pathOnB2[:2], permutationEq[2].set_color(MINT)))
    scene.play(TransformFromCopy(pathOnB2[2:], permutationEq[3].set_color(VIOLET)))
    
    virtualPath = VGroup(
        trailParts["left"]["b"]["trail"][0]["UL"].copy(),
        virtualTrack[0].copy(),
        virtualTrack[2].copy(),
        trailParts["left"]["b"]["trail"][4]["UR"].copy()
    ).set_color(YELLOW)
    scene.play(Create(virtualPath))
    scene.play(Write(permutationEq[4]),
               TransformFromCopy(virtualPath, permutationEq[5].set_color(YELLOW)))
    
    five = MathTex("5").move_to(permutationEq, aligned_edge=LEFT)
    scene.play(ReplacementTransform(permutationEq, five))
    bCountVal = five.copy().next_to(trailParts["left"]["bCountTex"][1], LEFT)
    scene.play(TransformFromCopyFadeOutTarget(five, bCountVal, trailParts["left"]["bCountTex"][0]))
    trailParts["left"]["bCountTex"][0].become(bCountVal)
    scene.remove(bCountVal)

    return VGroup(pathOnA, pathOnB, four, five, virtualTrack, virtualPath)

def findFinalAnswer(scene:Scene, toFadeOut, trailParts, diaTrails):
    scene.play(FadeOut(toFadeOut),
               trailParts["left"].animate.restore().set_color(WHITE),
               VGroup(trailParts["left"]["aCountTex"], trailParts["left"]["bCountTex"]).animate.to_edge(RIGHT).shift(LEFT*4),
               FadeIn(diaTrails, A, B))
    
    trailParts["right"]["aCountTex"] = trailParts["left"]["aCountTex"].copy().next_to(trailParts["right"]["a"], DOWN)
    trailParts["right"]["bCountTex"] = trailParts["left"]["bCountTex"].copy().next_to(trailParts["right"]["b"], DOWN)
    trailParts["right"].set_color(WHITE)
    scene.play(Write(trailParts["nums"][0]))
    scene.play(FadeIn(trailParts["arrows"][0], trailParts["right"]["b"], trailParts["right"]["bCountTex"]))
    scene.play(Write(trailParts["nums"][1]))
    scene.play(FadeIn(trailParts["arrows"][1], trailParts["right"]["a"], trailParts["right"]["aCountTex"]))

    partOneCnt = MathTex(r"4\times5").next_to(trailParts["arrows"][0], DOWN).shift(DOWN)
    partTwoCnt = MathTex(r"5\times4").next_to(trailParts["arrows"][1], DOWN).shift(DOWN)
    scene.play(ReplacementTransform(VGroup(trailParts["left"]["aCountTex"], trailParts["right"]["bCountTex"]), partOneCnt),
               ReplacementTransform(VGroup(trailParts["left"]["bCountTex"], trailParts["right"]["aCountTex"]), partTwoCnt))
    
    scene.play(Transform(partOneCnt, MathTex("20").move_to(partOneCnt)), Transform(partTwoCnt, MathTex("20").move_to(partTwoCnt)))
    
    ans = MathTex("20{{+}}20").next_to(diaTrails, DOWN).shift(DOWN)
    scene.play(Write(ans[1]), TransformFromCopy(partOneCnt, ans[0]), TransformFromCopy(partTwoCnt, ans[2]))
    scene.play(Transform(ans, MathTex("40").move_to(ans)))