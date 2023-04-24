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

class newLineTest(Scene):
    def construct(self):
        tex = Tex(r"Hello\\World", font_size=fontSize)
        self.add(tex)

class sectionTest(Scene):
    def play(self, *args, **kwargs):
        args = list(args)
        args.append(Wait(5))
        super().play(*args, **kwargs)
        #첫번째 시도) overrideAnimation : Animation를 상속하는 클래스를 만드는거라, Animation의 먼저 만들어진 다른 자식들에 영향을 줄 수가 없어서 안됨
        #두번째 시도) Scene의 play를 override하는 방법 : 애니메이션은 Scene.play()를 통해서만 실행되므로, play()를 오버라이딩해서 wait()을 추가
        #-> 문제점: self.wait() 은 play(Wait()) 이었기 때문에 무한루프에 걸림! 소스코드를 꼭 확인해보기
        #세번째 시도) Scene의 play를 override하는데, Wait()을 추가
        #-> 문제점: play의 인자 *args는 가변 인자 튜플이라 +Wait()연산이 안됨!
        #-> 해결방법: list로 변환해서 + Wait() 연산을 해줌
        #-> 문제점(not critical): 인터페이스가 아닌 구현체 상속은 지양해야 함! -> Scene의 play를 override하는 것은 좋지 않음
        #-> 이유: 템플릿메서드패턴을 쓰는게 아니면, 확장성에 문제가 생기므로(족보꼬임) 최근 언어는 아예 금지해놓기도 함
        #-> 해결방법: 템플릿메서드패턴을 쓰거나, 합성하기 (추가 공부필요)
        self.next_section()

    def construct(self):
        sectionTestFunc1(self)
        sectionTestFunc2(self)
        sectionTestFunc3(self)
        # section의 사용
        # 1) play() override에서 next_section()을 호출하지 않고, 각 함수(실질적 section)들 사이에 next_section() 추가하는 경우
        # 1-1) 개발 중 디버깅 시 원하는 section만 빼고 skip_animation=True로 실행하는 경우에 유용
        # 1-2) 최종 렌더링 후 필요한 section만 다시 렌더링하는 경우에 유용
        # 2) play() override에서 next_section()을 호출하고, 각 함수(실질적 section)들 사이에 next_section() 추가하지 않는 경우
        # 2-1) 최종 렌더링 시 각 section(사실 모든 animation) 마다 5초씩 대기하고, 순서대로 각자 파일이 나와서 동영상 편집하기에 유용
        # 1, 2 를 동시에...분리해서 사용...할 수 있을지 고민해보기. 일단은 개발중에는 오버라이딩한거 주석처리 해놓고, 
        # 최종 렌더링할 때는 주석 해제하고 렌더링하면 될 듯

def sectionTestFunc1(self):
    self.play(Write(Text("First").move_to(UP)))

def sectionTestFunc2(self):
    self.play(Write(Text("Second")))

def sectionTestFunc3(self):
    self.play(Write(Text("Third").move_to(DOWN)))

class example(Scene):
    def construct(self):
        self.play(Write(Text("First").move_to(UP)))
        self.play(Write(Text("Second")))
        self.play(Write(Text("Third").move_to(DOWN)))