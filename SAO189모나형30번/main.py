from manim import *
from sections import *

config.max_files_cached = -1

class main(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        graphDict, graphDict2 = showProblem(self)
        originGraphDict = graphDict.copy()
        originGraphDict2 = graphDict2.copy()
        describeProblem(self)
        hxTex, a, b, k = analyzeHx(self, graphDict, graphDict2)
        compareHxGx(self, hxTex, graphDict, graphDict2, VGroup(originGraphDict, originGraphDict2), a, b, k)
        trapezoidTex, toFadeOut = specifyTrapezoid(self, graphDict, graphDict2, a, b)
        findAB(self, trapezoidTex, toFadeOut, graphDict, originGraphDict, originGraphDict2, a, b, k)