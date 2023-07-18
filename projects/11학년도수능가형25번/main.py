from manim import *
from sections import *
config.max_files_cached = -1
    
class Test(ThreeDScene):
    def construct(self):
        cubesGroup = CubesGroup(4).scale_to_fit_height((config.frame_height-1)).to_corner(DL)
        while len(cubesGroup.getEvenCols()) > 0:
            cubesGroup.popEvens()
        self.add(cubesGroup)
        self.play(FadeOut(cubesGroup.getEventhCols()))

        self.play(Group(cubesGroup.getOddthCols(), cubesGroup.axes, cubesGroup.cubes[0])
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)),
               FadeOut(cubesGroup.labels))
        cubesGroup.addCols(4)
        self.play(FadeIn(cubesGroup.getOddthCols(5, 8).set_fill_color(YELLOW)))


class main(ThreeDScene):
    def play(self, *args, **kwargs):
        args = list(args)
        args.append(Wait(2)) # append 하는거라 앞 애니메이션들이랑 동시에 진행되므로 1 초과해야 추가로 기다림
        super().play(*args, **kwargs)

    def construct(self):
        self.next_section()
        texts = questionSection(self)
        originalTexts = texts.copy()
        cubesGroup = describeBaseSituation(self, texts)
        describeEvenIterate(self, texts, cubesGroup) #cubesGroup에 다시 할당 필요한지 확인 필요
        eqbox = descreibeEq(self, texts[4], texts[5], cubesGroup)
        fend = iteratingMore(self, texts, cubesGroup, eqbox)
        neglectEventhCols(self, cubesGroup, fend)
        iteratingMoreOnlyWithOddCols(self, cubesGroup, fend)
        #iteratingMoreWithOutFend(self, cubesGroup, fend)
        f2nEq = comparingTriangles(self, cubesGroup, fend)
        pqEq = calculateEq(self, texts[5], f2nEq)
        findFinalAnswer(self, pqEq, originalTexts)