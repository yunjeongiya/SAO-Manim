from manim import *
#from library.utils import *

class ColorPartsBySequence(AnimationGroup):
    def __init__(self, mobjects:VGroup, colorSequence:tuple, run_time=2, lag_ratio=0.5, **kwargs):
        super().__init__(*[
            mobject.animate.set_fill(color, opacity=1) for mobject, color in zip(mobjects, colorSequence)
        ], run_time=run_time, lag_ratio=lag_ratio, **kwargs)