import self as self
from manim import *

# default font size = 48

fontSize = 20
smallFont = fontSize * 0.6
class coordinateSystemTest(Scene):
    def construct(self):
        numberplane = NumberPlane().add_coordinates()
        self.add(numberplane)

class CameraTest(MovingCameraScene):
    def construct(self):
        self.add(Text("default camera, font size : 48"))
        self.wait(1)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.5).shift(2 * UP))
        self.add(Text("camera zoom in scale : 0.5, font size : 48*0.5", font_size=DEFAULT_FONT_SIZE*0.5)
                 .move_to(self.camera.frame.get_center()))
        self.wait(1)
        self.play(Restore(self.camera.frame))
        self.wait(1)

class StrokeWidthTest(Scene):
    def construct(self):
        #self.add(NumberPlane())
        for i in range(1,10,1):
            line = Line(np.array([-2, 4.5-i, 0]), np.array([2, 4.5-i, 0]), stroke_width=i)
            text = Text(str(i), font_size=fontSize).next_to(line, RIGHT)
            if i == 4:
                self.add(Text("default stroke width -> ", font_size=fontSize).next_to(line, LEFT))
            self.add(line, text)

class FontSizeTest(Scene):
    def construct(self):
        self.add(Text("default font size\n \t\t\t48").move_to(np.array([-4, 0, 0])))
        text = Text("font size").move_to(np.array([0, 4, 0]))
        for i in range(0, 1000, 5):
            text = Text(str(fontSize + i), font_size=fontSize + i).next_to(text, DOWN)
            self.add(text)


def highlightText(self, text, *words, color=YELLOW):  # Animation class 상속받는 걸로 바꿔서 동시에 진행 가능하도록 만들기
    word_mob = VGroup()
    for word in words:
        word_mob.add(*text.get_parts_by_tex(word))
    highlight = BackgroundRectangle(word_mob, fill_opacity=0.3, buff=0.05, color=color).set_z_index(-1)
    self.play(FadeIn(highlight, shift=RIGHT))
    return highlight


def highlightTextWithPicture(self, mob, text, *words, color=YELLOW):
    highlight = highlightText(self, text, *words, color)
    self.play(Flash(mob))
    self.wait(1)
    self.play(FadeOut(highlight))


def diffEqBuilder(direction, fontSize):
    eq = MathTex(r"\lim\limits_{h\to", r"0", r"" + direction + "}", r"\mathit{\frac{f(t+h)-f(t)}", "{h}}",
                 font_size=fontSize)
    return eq


class DotOnXY():
    def __init__(self, axes, tracker, tex):
        self.onX = Dot(axes.coords_to_point(tracker.get_value(), 0), color=RED).add_updater(
            lambda m: m.move_to(axes.coords_to_point(tracker.get_value(), 0)))
        self.onXLabel = tex.next_to(axes.coords_to_point(tracker.get_value(), 0), DOWN, buff=0.1).add_updater(
            lambda m: m.next_to(axes.coords_to_point(tracker.get_value(), 0), DOWN, buff=0.1))
        self.onY = Dot(axes.coords_to_point(0, tracker.get_value()), color=RED).add_updater(
            lambda m: m.move_to(axes.coords_to_point(0, tracker.get_value())))
        self.onYLabel = tex.copy().next_to(axes.coords_to_point(0, tracker.get_value()), LEFT, buff=0.1).add_updater(
            lambda m: m.next_to(axes.coords_to_point(0, tracker.get_value()), LEFT, buff=0.1))
        # 여기서 copy 안해서 계속 문제 생겼었음. tex를 그냥 이동시킨 셈이었으니까...
        # onX, onY를 화면에서 지우면 Label들은 onX가 안움직여서 안움직임


def get_rectangle_corners(bottom_left, top_right):
    return [
        (top_right[0], top_right[1]),
        (bottom_left[0], top_right[1]),
        (bottom_left[0], bottom_left[1]),
        (top_right[0], bottom_left[1]),
    ]


def get_rectangle(axes, recWidth, recColor=WHITE, recStrokeWidth=4):
    polygon = Polygon(
        *[
            axes.c2p(*i)
            for i in get_rectangle_corners(
                (0, 0), (recWidth.get_value(), recWidth.get_value())
            )
        ]
    )
    polygon.set_stroke(color=recColor, width=recStrokeWidth)
    return polygon


def pointerBuilder(tex, point):
    tex.next_to(point, DOWN)
    arrow = Arrow(point.get_center(), tex.get_center(), buff=0.1)
    return VGroup(tex, arrow).set_color(YELLOW)


class TplusHDiff():
    def __init__(self, axes, t, h, area, i, squareLabel, color=WHITE):
        t_plus_h = ValueTracker(t.get_value() + h.get_value())
        self.add(t_plus_h)
        t_plus_h.add_updater(lambda x: x.set_value(t.get_value() + h.get_value()))
        square = always_redraw(lambda: get_rectangle(axes, t_plus_h, color, 2))
        squareLabel = MathTex(squareLabel, font_size=smallFont).set_color(color).next_to(square, UP, buff=0.05)
        squareLabel.add_updater(lambda x: x.next_to(square, UP, buff=0.05))
        dotTplusHs = DotOnXY(axes, t_plus_h, MathTex("t+", "h", font_size=smallFont).set_color_by_tex("h", color))
        # plusBrace = BraceLabel(Line(dotTs.onX, dotTplusHs.onX), "h", font_size=smallFont)
        newI = always_redraw(lambda: Intersection(area, square, stroke_width=0))
        upperIDiffI = always_redraw(
            lambda: Difference(newI, i, stroke_width=0, fill_opacity=1, color=color).set_z_index(-2))
        fXPlusHTex = MathTex("f(x+", "h", ")", font_size=smallFont).set_color_by_tex("h", color).move_to(newI)
