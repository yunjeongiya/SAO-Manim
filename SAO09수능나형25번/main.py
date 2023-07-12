from manim import *
from sections import *

config.max_files_cached = -1
class main(Scene):
    def construct(self):
        showProblem(self)
        toFadeOut = showExample(self)
        toFadeOut = describeShortestDistanceConcept(self, toFadeOut)
        toFadeOut, diaTrails, trailsExpandScale = findPath(self, toFadeOut)
        trailParts, trailsExpandScale = generalizePath(self, toFadeOut, diaTrails, trailsExpandScale)
        toFadeOut = calculatePathCountsOfParts(self, trailParts, diaTrails, trailsExpandScale)
        findFinalAnswer(self, toFadeOut, trailParts, diaTrails)