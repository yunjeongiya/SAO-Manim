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
        showProblem(self)
        toFadeOut = showExample(self)
        toFadeOut = describeShortestDistanceConcept(self, toFadeOut)
        toFadeOut, diaTrails, trailsExpandScale = findPath(self, toFadeOut)
        trailParts, trailsExpandScale = generalizePath(self, toFadeOut, diaTrails, trailsExpandScale)
        toFadeOut = calculatePathCountsOfParts(self, trailParts, diaTrails, trailsExpandScale)
        findFinalAnswer(self, toFadeOut, trailParts, diaTrails)