from manim import *
from sections import *

config.max_files_cached = -1

class main(Scene):
    count = 0
    def play(self, *args, **kwargs):
        args = list(args)
        args.append(Wait(2)) # append 하는거라 앞 애니메이션들이랑 동시에 진행되므로 1 초과해야 추가로 기다림
        super().play(*args, **kwargs)
        self.next_section(str(self.count))
        self.count += 1

    def construct(self):
        self.next_section(skip_animations=False)
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