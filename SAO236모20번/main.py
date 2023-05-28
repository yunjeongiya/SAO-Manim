from manim import *
from sections import *

config.max_files_cached = -1

class main(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        texts = showProblem(self)
        describeProblem(self, texts)
        minimumDescription = describeMinimum(self, texts)
        gxDescription = describeIntegral(self, texts, minimumDescription)
        texts = graphAnalysis(self, gxDescription, minimumDescription, texts)
        ft, gx = calculateGxIntegral(self, texts)
        targetSituation = specifyMinimum(self, texts, gx, minimumDescription)
        graphGroup, minLine, verticalLines, vals = findMinimum(self, texts, targetSituation)
        fx, f1f2eq = findFx(self, texts, ft, graphGroup, minLine, verticalLines, vals)
        fx, kval = calculateK(self, fx, f1f2eq)
        finalAnswer(self, texts, fx, kval)