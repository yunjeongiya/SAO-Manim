from manim import *
from sections import *

config.max_files_cached = -1
class main(Scene):
    def construct(self):
        showProblem(self)