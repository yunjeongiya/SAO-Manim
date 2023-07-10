from manim import *
from consts import *

class Row(Line):
    def __init__(self, i, j):
        super().__init__([i, j, 0], [i+1, j, 0])

class Col(Line):
    def __init__(self, i, j):
        super().__init__([i, j, 0], [i, j-1, 0])

class RightArrow(Arrow):
    def __init__(self):
        super().__init__(max_tip_length_to_length_ratio=0.1, color=MINT)

class DownArrow(Arrow):
    def __init__(self):
        super().__init__(max_tip_length_to_length_ratio=0.1, color=VIOLET)
        self.rotate(-PI/2)

class URline(Line):
    def __init__(self, isLeft:bool):
        if isLeft: super().__init__([-1,0,0],[0,1,0])
        else: super().__init__([0,-1,0],[1,0,0])

class DRline(Line):
    def __init__(self, isLeft:bool):
        if isLeft: super().__init__([-1,0,0],[0,-1,0])
        else: super().__init__([0,1,0],[1,0,0])

class URArrow(Arrow):
    def __init__(self):
        super().__init__(max_tip_length_to_length_ratio=0.1, color=MINT)
        self.rotate(PI/4)

class DRArrow(Arrow):
    def __init__(self):
        super().__init__(max_tip_length_to_length_ratio=0.1, color=VIOLET)
        self.rotate(-PI/4)

def buildArrowPathFromPath(path, scale):
    arrowPath = VGroup()
    for line in path:
        if type(line) is Row:
            arrowPath += RightArrow()
        elif type(line) is Col:
            arrowPath += DownArrow()
        elif type(line) is URline:
            arrowPath += URArrow()
        elif type(line) is DRline:
            arrowPath += DRArrow()
        else: raise TypeError("all line should be one of Row, Col, URline, DRline")
        arrowPath[-1].scale(scale).move_to(line)
    return arrowPath

class ChangeOrder(AnimationGroup):
    def __init__(self, mobject:VMobject, target:VMobject, targetSequence:tuple):
        super().__init__(*[
            Transform(mobject[i], target[targetSequence[i]])
            for i in range(len(targetSequence))
        ])