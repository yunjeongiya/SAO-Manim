from manim import *
from consts import *
def fxGraphBuilder(xShift, ax:Axes, *args):
    return VGroup(ax.plot(lambda x : 0, x_range=[XSTART, xShift], *args),
                  ax.plot(lambda x : x-xShift, x_range=[xShift, YEND+xShift], *args))