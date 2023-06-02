from manim import *
from sections import *

config.max_files_cached = -1

class main(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        graphDict, graphDict2 = showProblem(self)
        describeProblem(self)
        hxTex = analyzeHx(self, graphDict, graphDict2)