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
        self.next_section(skip_animations=False)
        showProblem(self)
        numbers = describeProblem(self)
        texts = describeCircularPermutation(self)
        countCasesByColoring(self, VGroup(numbers, texts, TEXTS))
