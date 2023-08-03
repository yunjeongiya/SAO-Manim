from manim import *
from sections import *

config.max_files_cached = -1
class main(Scene):
    count = 0
    def play(self, *args, **kwargs):
        args = list(args)
        args.append(Wait(2))
        super().play(*args, **kwargs)
        self.next_section(str(self.count))
        self.count += 1

    def construct(self):
        #self.next_section(skip_animations=True)
        showProblem(self)
        rangeOfM = findRangeOfM(self)
        findMaxOfP(self, rangeOfM)