from manim import *

class TransformFromCopyFadeOutTarget(AnimationGroup):
    def __init__(self, origin:Mobject, copy:Mobject, target:Mobject, lag_ratio=0.5, **kwargs):
        super().__init__(TransformFromCopy(origin, copy), FadeOut(target), lag_ratio=lag_ratio, **kwargs)