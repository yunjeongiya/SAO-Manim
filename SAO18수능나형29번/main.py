from manim import *
from sections import *

class main(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        showProblem(self)
        describeProblem(self)