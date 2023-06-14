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
        graphDict, graphDict2 = showProblem(self)
        originGraphDict = graphDict.copy()
        originGraphDict2 = graphDict2.copy()
        describeProblem(self)
        hxTex, a, b, k = analyzeHx(self, graphDict, graphDict2)
        compareHxGx(self, hxTex, graphDict, graphDict2, VGroup(originGraphDict, originGraphDict2), a, b, k)
        trapezoidTex, toFadeOut = specifyTrapezoid(self, graphDict, graphDict2, a, b)
        findAB(self, trapezoidTex, toFadeOut, graphDict, originGraphDict, originGraphDict2, a, b, k)