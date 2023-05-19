from manim import *
from consts import *
from utils import *

def showProblem(scene):
    texts = Group(TITLE.to_edge(UP),
                  TEXT.next_to(TITLE, DOWN, aligned_edge = LEFT),
                  ).to_edge(LEFT)
    scene.add(texts)
    return texts