from manim import *
from consts import *
def fxGraphBuilder(xShift, ax:Axes, *args):
    return VGroup(ax.plot(lambda x : 0, x_range=[XSTART, xShift], *args),
                  ax.plot(lambda x : x-xShift, x_range=[xShift, YEND+xShift], *args))

def searchShapesInTex(text:VMobject, shape:VMobject):
    T = TransformMatchingShapes
    results = []
    l = len(shape.submobjects[0])
    shape_aux = VMobject()
    shape_aux.points = np.concatenate([p.points for p in shape.submobjects[0]])
    for i in range(len(text.submobjects[0])):
        subtext = VMobject()
        subtext.points = np.concatenate([p.points for p in text.submobjects[0][i:i+l]])
        if T.get_mobject_key(subtext) == T.get_mobject_key(shape_aux):
            results.append(slice(i, i+l))
    return results