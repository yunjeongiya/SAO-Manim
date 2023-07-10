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