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

