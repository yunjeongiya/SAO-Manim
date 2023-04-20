from SAOlib import *
fontSize = 30
smallFont = fontSize*0.6

class DotOnXY():
    def __init__(self, axes, tracker, tex):
        self.onX = Dot(axes.coords_to_point(tracker.get_value(),0), color=RED).add_updater(lambda m: m.move_to(axes.coords_to_point(tracker.get_value(),0)))
        self.onXLabel = tex.next_to(axes.coords_to_point(tracker.get_value(),0), DOWN, buff=0.1).add_updater(lambda m : m.next_to(axes.coords_to_point(tracker.get_value(),0), DOWN, buff=0.1))
        self.onY = Dot(axes.coords_to_point(0,tracker.get_value()), color=RED).add_updater(lambda m: m.move_to(axes.coords_to_point(0,tracker.get_value())))
        self.onYLabel = tex.copy().next_to(axes.coords_to_point(0,tracker.get_value()), LEFT, buff=0.1).add_updater(lambda m: m.next_to(axes.coords_to_point(0,tracker.get_value()), LEFT, buff=0.1))
        #여기서 copy 안해서 계속 문제 생겼었음. tex를 그냥 이동시킨 셈이었으니까...
        #onX, onY를 화면에서 지우면 Label들은 onX가 안움직여서 안움직임

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

class HighlightAnimationTest(Scene):
    def construct(self):
        return super().construct()

class EqTest(Scene):
    def construct(self):
        direction = "-"
        eq = MathTex(r"\lim\limits_{h\to", r"0", r""+direction+"}", r"\mathit{{f(t+h)-f(t)}", r"\over", "{h}}", font_size=fontSize)
        eq.get_part_by_tex("over").set_color(RED)
        self.add(eq)

class createIndicateTest(Scene):
    def construct(self):
        tex = Tex("안녕", font_size=fontSize)
        self.add(tex)
        self.play(Indicate(tex))

class testZindex(Scene):
    def construct(self):
        circle = Circle(color=RED, fill_opacity=1)
        square = Square(color=BLUE, fill_opacity=1).set_z_index(circle.get_z_index()-1)
        self.add(circle, square)
        self.add(Tex(circle.get_z_index()).next_to(circle, LEFT), Tex(square.get_z_index()).next_to(square, RIGHT))

class FontSizeTest(Scene):
    text = Text("default", font_size=DEFAULT_FONT_SIZE).move_to(UP)
    for i in range(1, 10):
        text = Text("default*" + str(i), font_size=i * DEFAULT_FONT_SIZE).next_to(text, DOWN)
        self.add(text)

class newLineTest(Scene):
    def construct(self):
        tex = Tex(r"Hello\\World", font_size=fontSize)
        self.add(tex)

class Test(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        axes = Axes(
            x_range=[-0.7, 5, 1],
            y_range=[-0.7, 4, 1],
            x_length=5.7,
            y_length=4.7,
            axis_config={
                "include_numbers": True,
                "font_size": fontSize,
                "tip_width": 0.1,
                "tip_height": 0.15},
            x_axis_config={
                "numbers_to_include": np.arange(1, 4.1, 1),
            },
            tips=True, #tips size 줄이기 -> axis_config에서 tip_width, tip_height 조절
        )

        upperText = Tex("21. 좌표평면 위에 그림과 같이 ","어두운 부분","을 내부로 하는 ",
                    "도형이 있다. 이 도형과 네 점 ",
                    "$(0, 0)$",", ", #index 4
                    "$(t, 0)$",", ", #index 6
                    "$(t, t)$",", ", #index 8
                    "$(0, t)$", #index 10
                    "를 ","꼭짓점으로 하는 정사각형","이 ","겹치는 ", "부분의 넓이를 $f(t)$","라 하자.", 
                    font_size = fontSize, tex_environment="flushleft").next_to(axes, UP, buff=0.5)
        lowerText = Tex("열린 구간 $(0, 4)$", "에서 함수 ", "$f(t)$가 ", "미분가능", "하지 ", "않은", " 모든\n",
                        "$t$의 값", "의 ", "합", "은? [4점]", font_size=fontSize).next_to(axes, DOWN, buff=0.5)
        underilneNot = Underline(lowerText.get_part_by_tex("않은"))
        text = Group(upperText, lowerText, underilneNot)
        self.add(text)
        Group(text, axes).move_to(ORIGIN)

        xLabel = axes.get_x_axis_label(MathTex("x", font_size=fontSize*1.2), direction=DOWN+LEFT*0.05, buff=0.35)
        yLabel = axes.get_y_axis_label(MathTex("y", font_size=fontSize*1.2), direction=LEFT+DOWN*0.25, buff=0.35)
        labels = Group(xLabel, yLabel)
        x_vals = [0, 0, 1, 2, 3, 3, 4, 4]
        y_vals = [0, 1, 1, 2, 2, 3, 3, 0]
        graph = axes.plot_line_graph(x_vals, y_vals, add_vertex_dots=False).set_color("#EEEEE0").set_stroke(width=2).set_z_index(-2)
        points = [axes.c2p(x, y) for x, y in zip(x_vals, y_vals)]
        area = Polygon(*points, color=GREY, fill_opacity=0.5, stroke_width=0).set_z_index(-5)
        #area = axes.get_area(graph, [0, 4], color=GREY, opacity=0.5) #수학적으로 함수가 아니므로 불가능함

        # 반복문으로 하나로 만들기
        line_1 = axes.get_lines_to_point(axes.c2p(1,1))
        line_2 = axes.get_lines_to_point(axes.c2p(2,2))
        line_3 = axes.get_lines_to_point(axes.c2p(3,3))
        line_group = Group(line_1,line_2,line_3).set_z_index(-3)

        dotO = Dot(axes.coords_to_point(0,0), color=RED)
        dotOLabel = Tex("O", font_size=fontSize).next_to(dotO, DL*0.4)

        self.add(area, axes, labels, graph, dotOLabel, line_group)
        self.play(Circumscribe(upperText.get_part_by_tex("어두운 부분")), area.animate.set_color(YELLOW))
        self.play(area.animate.set_color(GREY))  
        self.wait()

        self.play(Indicate(upperText.get_part_by_tex("(0, 0)")), Indicate(upperText.get_part_by_tex("(t, 0)")),
                   Indicate(upperText.get_part_by_tex("(t, t)")), Indicate(upperText.get_part_by_tex("(0, t)")))

        t = ValueTracker(1.5)

        dotTs = DotOnXY(axes, t, Tex("$t$", font_size=fontSize))
        horizontalLine = axes.get_horizontal_line(axes.coords_to_point(t.get_value(),t.get_value()))
        verticalLine = axes.get_vertical_line(axes.coords_to_point(t.get_value(),t.get_value()))
        linett = Group(horizontalLine, verticalLine)

        self.play(Create(dotO.set_z_index(1)), Flash(dotO),
                  Circumscribe(upperText.get_part_by_tex("$(0, 0)$"), fade_out=True))
        self.wait()

        self.add(dotTs.onXLabel)
        self.play(Indicate(dotTs.onXLabel))
        #self.play(Create(dotTs.onXLabel), Indicate(dotTs.onXLabel)) 하면 아예(!) 화면에 추가되지가 않음
        self.wait()

        self.play(Create(dotTs.onX.set_z_index(1)), Flash(dotTs.onX),
                  Circumscribe(upperText.get_part_by_tex("$(t, 0)$"), fade_out=True))
        self.wait()

        dotTT = Dot(axes.coords_to_point(t.get_value(),t.get_value()), color=RED)
        drawLineTT = AnimationGroup(FadeIn(dotTs.onYLabel),
                                    AnimationGroup(Create(horizontalLine), Create(verticalLine)),
                                    AnimationGroup(Create(dotTT.set_z_index(1)), Flash(dotTT)), 
                                    lag_ratio=1, run_time=1)
        self.play(drawLineTT, Circumscribe(upperText.get_part_by_tex("$(t, t)$"), fade_out=True)) #다 동시에 되도록 수정! -> Line을 따로 만들고 AnimationGroup 이용해 해결
        self.wait()

        self.play(Create(dotTs.onY.set_z_index(1)), Flash(dotTs.onY),
                  Circumscribe(upperText.get_part_by_tex("$(0, t)$"), fade_out=True))
        self.wait()

        squareT = always_redraw(lambda: get_rectangle(axes, t).set_stroke(color=RED))
        #lambda로 안감싸고 get_rectangle(RED)로 하면, get_rectangle()에 RED를 넣어서 실행된 결과인 polygon이
        #always_redraw의 인자로 들어가서 오류 발생!
        #always_redraw는 함수를 인자로 받아서, 함수의 결과를 계속해서 업데이트 해줌
        #즉, 함수를 인자로 넣어야 하므로 lambda로 감싸줘야 함
        #always_redraw(get_rectangle)로 하면,
        #get_rectangle()이 아니라 get_rectangle이라는 함수 자체가 인자로 들어가서 정상 작동! lambda로 감싸지 않아도 됨

        dots = Group(dotO, dotTT, dotTs.onX, dotTs.onY, linett) #이름 바꾸기
        self.play(FadeOut(dots), FadeIn(squareT), Circumscribe(upperText.get_part_by_tex("꼭짓점으로 하는 정사각형")))

        self.play(t.animate.set_value(2.5))
        self.play(t.animate.set_value(3.2))
        self.play(t.animate.set_value(0.5))
        self.play(t.animate.set_value(1.5))

        i = always_redraw(lambda: Intersection(area, squareT, color=YELLOW, fill_opacity=0.5, stroke_width=0).set_z_index(-4))

        underline1 = Underline(upperText.get_part_by_tex("겹치는 "), color=YELLOW)
        underline2 = Underline(upperText.get_part_by_tex("부분의 넓이를 $f(t)$"), color=YELLOW)
        self.play(FadeIn(i), 
                  AnimationGroup(Create(underline1, lag_ratio=1), Create(underline2, lag_ratio=1), lag_ratio=1))

        self.play(t.animate.set_value(2.5))
        self.play(t.animate.set_value(3.2))
        self.play(t.animate.set_value(0.5))
        self.play(t.animate.set_value(1.5))

        line = Line(axes.coords_to_point(0,0), axes.coords_to_point(4,0), color="#ADFF2F", stroke_width=8, stroke_opacity=0.8)

        self.play(FadeOut(i), FadeOut(underline1),FadeOut(underline2), Create(line), Circumscribe(lowerText.get_part_by_tex("열린 구간 $(0, 4)$"), fade_out=True, run_time=2))
        self.wait()
        self.play(FadeOut(line))
        nonDiffTex = Group(lowerText.get_part_by_tex("$f(t)$가 "), 
                           lowerText.get_part_by_tex("미분가능"), 
                           lowerText.get_part_by_tex("하지 "), 
                           lowerText.get_part_by_tex("않은"))

        #카메라 이동 한번에 -> 해결
        self.play(self.camera.frame.animate.move_to(nonDiffTex).shift(DOWN).set(width=nonDiffTex.width*2))
        self.remove(squareT, dotTs.onXLabel, dotTs.onYLabel)
        highlight = highlightText(self, lowerText, "미분가능")

        diffDescription = Tex("좌미분계수", "=", "우미분계수", font_size=fontSize).next_to(nonDiffTex, DOWN, buff=0.5)
        diffDescription.next_to(nonDiffTex, DOWN, buff=0.5)
        self.play(Write(diffDescription))
        self.wait()
        framebox = SurroundingRectangle(lowerText.get_part_by_tex("않은"))
        notEqual = Tex("≠", font_size=fontSize, color=RED).move_to(diffDescription.get_part_by_tex("="))
        self.play(Create(framebox), Transform(diffDescription.get_part_by_tex("="),notEqual))
        self.wait()
        self.play(FadeOut(framebox), FadeOut(highlight), FadeToColor(notEqual, color=WHITE))

        #eq = MathTex(r"\lim\limits_{h\to", r"0", r""+direction+"}", r"\mathit{{f(t+h)-f(t)}", r"\over", "{h}}", font_size=fontSize)
        leftDiffEq = diffEqBuilder("-", fontSize).move_to(diffDescription.get_part_by_tex("좌미분계수"), aligned_edge=RIGHT)
        leftDiffEq.get_part_by_tex("-").set_color(RED)
        self.play(Transform(diffDescription.get_part_by_tex("좌미분계수"),leftDiffEq.get_part_by_tex("f(t+h)-f(t)")))
        self.wait()
        self.play(FadeIn(Group(leftDiffEq.get_part_by_tex("{h}}"), leftDiffEq.get_part_by_tex("over"))))
        self.wait()
        self.play(FadeIn(leftDiffEq.get_part_by_tex("lim")))
        self.wait()
        self.play(FadeIn(Group(leftDiffEq.get_part_by_tex("0"), leftDiffEq.get_part_by_tex("-"))))
        self.wait()
        
        rightDiffEq = diffEqBuilder("+", fontSize).move_to(diffDescription.get_part_by_tex("우미분계수"), aligned_edge=LEFT)
        rightDiffEq.get_part_by_tex("+").set_color(BLUE)
        self.play(FadeOut(diffDescription.get_part_by_tex("우미분계수")), 
                  FadeIn(Group(rightDiffEq.get_part_by_tex("f(t+h)-f(t)"), rightDiffEq.get_part_by_tex("{h}}")), 
                        rightDiffEq.get_part_by_tex("over"), rightDiffEq.get_part_by_tex("lim")))
        self.wait()
        self.play(FadeIn(Group(rightDiffEq.get_part_by_tex("0"), rightDiffEq.get_part_by_tex("+"))))
        self.wait()

        leftDiffLabel = Tex("좌미분계수", font_size=fontSize)
        leftDiffEq2 = diffEqBuilder("-", fontSize).next_to(leftDiffLabel, DOWN, buff=0.2, aligned_edge=LEFT)
        rightDiffLabel = Tex("우미분계수", font_size=fontSize).next_to(leftDiffEq2, DOWN, buff=0.5, aligned_edge=LEFT)
        rightDiffEq2 = diffEqBuilder("+", fontSize).next_to(rightDiffLabel, DOWN, buff=0.2, aligned_edge=LEFT)
        diffEqGroup = Group(leftDiffLabel, leftDiffEq2, rightDiffLabel, rightDiffEq2).next_to(axes, RIGHT, buff=0.5)

        self.play(self.camera.frame.animate.move_to(axes).shift(RIGHT*1.8).set(width=axes.width*1.8), FadeIn(diffEqGroup))

        areaDiffTex = Tex("넓이 ", "차", color=RED, font_size=fontSize).next_to(diffEqGroup, UP, buff=0.5, aligned_edge=LEFT)
        areaChangeRateTex = Tex("넓이 ", "순간변화율", color=BLUE, font_size=fontSize).move_to(areaDiffTex, aligned_edge=LEFT)

        frameDiff = Group(SurroundingRectangle(leftDiffEq2.get_part_by_tex("f(t+h)-f(t)")),
                          SurroundingRectangle(rightDiffEq2.get_part_by_tex("f(t+h)-f(t)"))).set_color(RED)
        
        frameLim = Group(Difference(SurroundingRectangle(Group(leftDiffEq2.get_part_by_tex("lim"),leftDiffEq2.get_part_by_tex("{h}}"))), frameDiff[0]),
                        Difference(SurroundingRectangle(Group(rightDiffEq2.get_part_by_tex("lim"), rightDiffEq2.get_part_by_tex("{h}}"))), frameDiff[1])).set_color(BLUE)

        self.play(FadeIn(frameDiff),
                  FadeOut(Group(leftDiffEq, rightDiffEq, diffDescription)))
        self.wait()
        self.play(Write(areaDiffTex))
        self.wait()
        self.play(Transform(frameDiff, frameLim))
        self.wait()
        self.play(Transform(areaDiffTex[1], areaChangeRateTex[1]))
        self.wait()

        dotTs.onXLabel = dotTs.onXLabel.copy().set_font_size(smallFont)
        dotTs.onYLabel = dotTs.onYLabel.copy().set_font_size(smallFont)
        squareT = always_redraw(lambda: get_rectangle(axes, t).set_stroke(width=2).set_color(WHITE)) 
        #recStroke, recColor 인자 없애도 되겠다 -> 완료
        self.play(self.camera.frame.animate.move_to(squareT).shift(RIGHT+DOWN*0.2).set(width=squareT.width*4),
                  FadeIn(dotTs.onXLabel), FadeIn(dotTs.onYLabel), FadeIn(squareT))
        self.wait()
        fxtex = MathTex("f(x",")", font_size=smallFont).move_to(i)
        self.play(FadeIn(i), FadeIn(fxtex),
                  FadeOut(diffEqGroup), FadeOut(areaDiffTex), FadeOut(frameDiff))

        h = ValueTracker(0)

        t_plus_h = ValueTracker(t.get_value()+h.get_value())
        self.add(t_plus_h)
        t_plus_h.add_updater(lambda x: x.set_value(t.get_value()+h.get_value()))
        bigSquare = always_redraw(lambda : get_rectangle(axes, t_plus_h).set_stroke(width=2, color=BLUE).set_z_index(-1))
        bigSquareLabel = MathTex("h>0", font_size=smallFont).set_color(BLUE).next_to(bigSquare, UP, buff=0.05)
        bigSquareLabel.add_updater(lambda x: x.next_to(bigSquare, UP, buff=0.05))
        dotTplusHs = DotOnXY(axes, t_plus_h, MathTex("t+","h", font_size=smallFont).set_color_by_tex("h", BLUE))
        plusBrace = BraceLabel(Line(dotTs.onX, dotTplusHs.onX), "h", font_size=smallFont)
        
        upperI = always_redraw(lambda: Intersection(area, bigSquare, stroke_width=0))
        upperIDiffI = always_redraw(lambda: Difference(upperI, i, stroke_width=0, fill_opacity=1, color=BLUE).set_z_index(-4))
        fXPlusHTex = MathTex("f(x+","h",")", font_size=smallFont).set_color_by_tex("h", BLUE).move_to(upperI)
        
        self.add(bigSquare, upperI, upperIDiffI.set_z_index(-4))
        self.play(h.animate.set_value(0.2),
                  FadeIn(bigSquareLabel), FadeIn(dotTplusHs.onXLabel), FadeIn(dotTplusHs.onYLabel), 
                  TransformMatchingTex(fxtex, fXPlusHTex))
        self.wait()
        self.play(h.animate.set_value(0),
                  FadeOut(bigSquareLabel), FadeOut(dotTplusHs.onXLabel), FadeOut(dotTplusHs.onYLabel),
                  TransformMatchingTex(fXPlusHTex, fxtex))
        self.remove(bigSquare, upperI, upperIDiffI)
        self.wait()

        t_minus_h = ValueTracker(t.get_value()-h.get_value())
        self.add(t_minus_h)
        t_minus_h.add_updater(lambda x: x.set_value(t.get_value()-h.get_value()))
        smallSquare = always_redraw(lambda : get_rectangle(axes, t_minus_h).set_stroke(width=2, color=RED).set_z_index(-1))
        smallSquareLabel = MathTex("h<0", font_size=smallFont).set_color(RED).next_to(smallSquare, UP, buff=0.05)
        smallSquareLabel.add_updater(lambda x: x.next_to(smallSquare, UP, buff=0.05))
        dotTminusHs = DotOnXY(axes, t_minus_h, MathTex("t+","h", font_size=smallFont).set_color_by_tex("h", RED))
        minusBrace = BraceLabel(Line(dotTs.onX, dotTminusHs.onX), "h", font_size=smallFont) #Brace 수정하기
        #+h였어서 사실 위에거랑 다른게 거의 없음. 코드 재사용하는거로 수정하기

        lowerI = always_redraw(lambda: Intersection(area, smallSquare, stroke_width=0))
        IDiffLowerI = always_redraw(lambda: Difference(i, lowerI, stroke_width=0, fill_opacity=1, color=RED).set_z_index(-4))
        fXMinusHTex = MathTex("f(x+","h",")", font_size=smallFont).set_color_by_tex("h", RED).move_to(lowerI)
        
        self.add(smallSquare, lowerI, IDiffLowerI.set_z_index(-4))
        self.play(h.animate.set_value(0.2),
                  FadeIn(smallSquareLabel), FadeIn(dotTminusHs.onXLabel), FadeIn(dotTminusHs.onYLabel), 
                  TransformMatchingTex(fxtex, fXMinusHTex))
        self.wait()
        self.play(h.animate.set_value(0),
                  FadeOut(smallSquareLabel), FadeOut(dotTminusHs.onXLabel), FadeOut(dotTminusHs.onYLabel),
                  TransformMatchingTex(fXMinusHTex, fxtex))
        self.remove(smallSquare, lowerI, IDiffLowerI)
        self.wait()

        #smallThinSquare = always_redraw(lambda : get_rectangle(axes, t_minus_h, RED, recStrokeWidth=2))
        #bigThinSquare = always_redraw(lambda : get_rectangle(axes, t_plus_h, BLUE, recStrokeWidth=2))
        #self.play(Transform(smallSquare, smallThinSquare), Transform(bigSquare, bigThinSquare))
        #Transform 은 한 프레임에서 target으로 다시 draw하는거라서,
        #위에처럼 하면 smallSquare, bigSquare는 다음순간에 always_redraw로 다시 그려지기 때문에
        #smallSquare, bigSquare가 smallThinSquare, bigThinSquare로 바뀌는 것처럼 보이지 않는다.

        self.add(bigSquare, upperI, upperIDiffI.set_z_index(-4), smallSquare, lowerI, IDiffLowerI.set_z_index(-4))
        diffDescription = Tex("좌우 넓이 차", font_size=smallFont).move_to(axes.c2p(3, 1))
        diffEq = diffEqBuilder("", smallFont).move_to(diffDescription, aligned_edge=RIGHT)
        self.play(h.animate.set_value(0.2), Write(diffDescription), FadeOut(fxtex), FadeOut(i))
        self.wait()
        self.play(Transform(diffDescription, diffEq.get_part_by_tex("f(t+h)-f(t)")))
        self.wait()
        self.play(h.animate.set_value(0.05), FadeIn(diffEq))
        self.wait()
        diffable = pointerBuilder(Tex("미분 가능", font_size = smallFont), dotTs.onXLabel)
        self.play(Write(diffable))

        self.play(FadeOut(diffable), FadeOut(diffEq), FadeOut(diffDescription), h.animate.set_value(0),
                  FadeOut(bigSquare), FadeOut(upperI), FadeOut(upperIDiffI), FadeOut(smallSquare), FadeOut(lowerI), FadeOut(IDiffLowerI),
                  FadeIn(i))
        self.wait()
        self.play(t.animate.set_value(1), run_time=2)
        self.wait()

        self.add(smallSquare, lowerI, IDiffLowerI.set_z_index(-4))
        self.play(h.animate.set_value(0.2))
        self.wait()
        self.play(h.animate.set_value(0))
        self.remove(smallSquare, lowerI, IDiffLowerI)
        self.wait()

        self.add(bigSquare, upperI, upperIDiffI.set_z_index(-4))
        self.play(h.animate.set_value(0.2))
        self.wait()
        smallSquare.become(get_rectangle(axes, t_minus_h).set_stroke(width=2, color=RED))
        lowerI.become(Intersection(area, smallSquare, stroke_width=0))
        IDiffLowerI.become(Difference(i, lowerI, stroke_width=0, fill_opacity=1, color=RED)).set_z_index(-4)
        self.play(FadeOut(i), FadeIn(smallSquare), FadeIn(lowerI), FadeIn(IDiffLowerI))
        self.wait()
        self.play(Write(diffDescription))
        i = always_redraw(lambda: Intersection(area, squareT, fill_opacity=0, stroke_width=0).set_z_index(-4))
        self.add(i)

        self.play(FadeIn(diffEq))
        self.wait()
        self.play(h.animate.set_value(0.05))
        self.wait()
        gap = h.get_value()/2
        upperIDiffIStick = Line(axes.c2p(1 + gap, 0), axes.c2p(1 + gap,1), color=BLUE, stroke_width=4.5)
        IDiffLowerIStickHorizontal = Line(axes.c2p(1 - gap,0), axes.c2p(1 - gap,1), color=RED, stroke_width=4.5)
        IDiffLowerIStickVertical = Line(axes.c2p(0,1-gap), axes.c2p(1 - gap,1-gap), color=RED, stroke_width=4.5)
        IDiffLowerISticks = VGroup(IDiffLowerIStickHorizontal, IDiffLowerIStickVertical)
        
        all = Group(area, upperIDiffI.set_z_index(-4), IDiffLowerI.set_z_index(-4), line_group, graph, axes, dotTs.onXLabel, dotTs.onYLabel, dotOLabel, diffEq, diffDescription)
        #saved = self.get_top_level_mobjects()
        self.play(FadeIn(upperIDiffIStick), FadeIn(IDiffLowerISticks), FadeOut(all), FadeOut(bigSquare), FadeOut(smallSquare), FadeOut(squareT))
        self.play(Rotate(IDiffLowerIStickVertical, -PI/2, about_point=axes.c2p(1 - gap, 1 - gap)))

        IDiffLowerStickBrace = BraceLabel(IDiffLowerISticks, "2t", brace_direction=LEFT, font_size=fontSize)
        upperIDiffIStickBrace = BraceLabel(upperIDiffIStick, "t", brace_direction=RIGHT, font_size=fontSize)

        self.play(FadeIn(IDiffLowerStickBrace), FadeIn(upperIDiffIStickBrace))
        self.wait()

        squareT = always_redraw(lambda: get_rectangle(axes, t).set_stroke(width=0))
        bigSquare = always_redraw(lambda : get_rectangle(axes, t_plus_h).set_stroke(width=0).set_z_index(-1))
        smallSquare = always_redraw(lambda : get_rectangle(axes, t_minus_h).set_stroke(width=0).set_z_index(-1))
        self.add(bigSquare, smallSquare, squareT)
        self.play(FadeIn(all), FadeOut(IDiffLowerStickBrace), FadeOut(upperIDiffIStickBrace), FadeOut(upperIDiffIStick), FadeOut(IDiffLowerISticks))

        undiffable1 = pointerBuilder(Tex("미분 불가능", font_size = smallFont), dotTs.onXLabel).shift(DOWN*0.3)
        self.play(Write(undiffable1), self.camera.frame.animate.shift(DOWN*0.05))
        self.wait()
        #0.001 is a hack to make the animation work
        #0+h.get_value() -> IDiffLowerI 의 영역이 0까지 감 -> 화면에서 아예 제거되는지 다시 안그려지고 사라짐...
        self.play(FadeOut(diffEq), FadeOut(diffDescription), t.animate.set_value(0.0001 + h.get_value()))
        #.animate()의 동작, rate_func인자, rate_functions 참고
        self.play(t.animate(rate_func=linear).set_value(1))
        self.play(t.animate(rate_func=linear).set_value(2))
        self.play(self.camera.frame.animate.move_to(axes).shift(RIGHT*0.5+DOWN*0.5).set(width=axes.width*1.5))
        self.play(t.animate(rate_func=linear).set_value(3))
        self.wait()
        undiffable2 = pointerBuilder(Tex("미분 불가능", font_size = smallFont), dotTs.onXLabel).shift(DOWN*0.3)
        self.play(Write(undiffable2))
        self.wait()
        self.play(t.animate(rate_func=linear).set_value(4-h.get_value()))
        self.play(Restore(self.camera.frame), FadeOut(bigSquare), FadeOut(smallSquare), FadeOut(squareT), 
                  FadeOut(dotTs.onXLabel), FadeOut(dotTs.onYLabel),
                  FadeOut(i), FadeOut(IDiffLowerI), FadeOut(upperIDiffI))
        #highlight = highlightText(self, lowerText, )
        #self.wait()
        #self.play(FadeOut(highlight))
        
        word_mob = Group(
            lowerText.get_part_by_tex("$f(t)$가"),
            lowerText.get_part_by_tex("미분가능"),
            lowerText.get_part_by_tex("하지"),
            lowerText.get_part_by_tex("않은"),
            lowerText.get_part_by_tex("모든"),
            lowerText.get_part_by_tex("$t$의 값"),
        )
        highlight = BackgroundRectangle(word_mob, fill_opacity=0.3, buff=0.05, color=YELLOW).set_z_index(-1)
        self.play(FadeIn(highlight, shift = RIGHT), 
                  Create(Circle(radius=axes.x_axis.get_number_mobject(3).get_height(), color=YELLOW).move_to(axes.x_axis.get_number_mobject(1))),
                  Create(Circle(radius=axes.x_axis.get_number_mobject(3).get_height(), color=YELLOW).move_to(axes.x_axis.get_number_mobject(3))))
        
        answerEq = MathTex("1", "+", "3", "=4").next_to(axes, RIGHT)
        self.play(Circumscribe(lowerText.get_part_by_tex("합")),
                  TransformFromCopy(axes.x_axis.get_number_mobject(1), answerEq[0]),
                  TransformFromCopy(axes.x_axis.get_number_mobject(3), answerEq[2]))
        self.play(Write(answerEq[1]), Write(answerEq[3]))
    