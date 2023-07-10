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