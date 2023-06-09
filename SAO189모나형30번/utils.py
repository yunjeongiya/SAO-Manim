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

def dotOnAxLabelBuilder(ax:Axes, val, label: Text| Tex | MathTex, isOnX: bool=True):
    if isOnX:
        return label.move_to(ax.coords_to_point(val, -0.15))
    else:
        return label.move_to(ax.coords_to_point(-0.15, val))
    
def makeGaForCopy(scene:Scene, gx):
    gx.save_state()
    gxPart1 = gx[0][searchShapesInTex(gx, MathTex("x(2-x)"))[0]]
    scene.play(*[
    Transform(gx[0][group], MathTex("a").scale_to_fit_height(gx[0][group].height).move_to(gx[0][group]), path_arc=-PI)
    for group in searchShapesInTex(gx, MathTex("x"))[:3]
    ])
    return MathTex("a(2-a)").scale_to_fit_height(gxPart1.height).move_to(gxPart1)