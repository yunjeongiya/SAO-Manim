from SAOlib import *
config.max_files_cached = -1
Tex.set_default(font_size=30, tex_environment="flushleft")
#Circumscribe.set_default(fade_out=True) #TODO set_default 없음. 감싸서 변형하는 방법 찾아보기

# Tex의 내용 중 수식인 건 일단 Latex 로 넘기기 위해 $로 감싸주고, 그 안에서 또 Latex의 기호를 사용하는 경우 \로 알려줘야 한다.
# 즉, 그냥 \cdots 이나 $cdots$ 이렇게 쓰면 인식이 안되고, $\cdots$ 이렇게 써야 인식이 된다. 
TITLE = Tex("11학년도 수능 수리 가형 25번")
TEXT1 = Tex(r"자연수 $m$에 대하여 ", "크기가 같은 정육면체 모양의 블록", r"이\\",
            "1열에 1개", ", ", "2열에 2개", ", ", "3열에 3개", r", $\cdots$, $m$열에 $m$개가 쌓여\\",
            "있다. ", r"블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음\\","시행을 반복한다.")
TEXT2 = Tex("블록의 개수가 짝수인 각 열", r"에 대하여 그 열에 있는\\",
            r"블록의 개수의 $\cfrac{1}{2}$ 만큼의 블록을 그 열에서 들어낸다.")
TEXT3 = Tex("블록을 들어내는 시행을 모두 마쳤을 때, ", 
            r"1열부터 $m$열까지\\",r"남아 있는 블록의 개수의 합을 $f(m)$",
            r"이라 하자.\\예를 들어, $f(2)=2$, $f(3)=5$, $f(4)=6$이다.")
#\cfrac 쓸 때는 \mathit 로 안감싸고 끊으면 LaTex 오류 발생 (이유 모름...)
#\cfrac 이랑 \mathit 조합해서 했는데 get_part_by_tex 했을 때 이상한 부분이 선택됨.... + italic이 숫자에도 적용되니 이상함
#\over 써도 여기서는 큰 크기 차이 없어서 그냥 over로 하기로 함
Eq = MathTex(r"\lim\limits_{m\to\infty}{{f(2",r"^{n+1}",r")-f(2",r"^{n}",r")}",r"\over{f(2",r"^{n+2}",r")}}",r"=\cfrac{q}{p}", font_size=30)
TEXT4 = Tex(r'''일 때, $p+q$의 값을 구하시오.\\
                (단, $p$와 $q$는 서로소인 자연수이다.) [4점]''')

CUBES_NUM = 6 #함수 정의할 때 인자로 받는게 나은지, 어차피 상수로 정의했으니 함수 안에서 바로 쓰는게 나은지?
CUBES_WIDTH = 4

#Square 소스코드 아이디어 참고 -> VGroup 상속받아 VGroup처럼 통째로 사용 가능하게 만들기
class CubesGroup(VGroup):
    def __init__(self, cubes_num, cube_fill_color=GREY, cube_stroke_color=WHITE, cube_stroke_width=2):
        super().__init__()
        self.cubes_num = cubes_num
        self.axes = ThreeDAxes(
            x_range=[0, self.cubes_num, 1],
            y_range=[0, self.cubes_num, 1],
            z_range=[-1, 1, 1],
            x_length=self.cubes_num,
            y_length=self.cubes_num,
            z_length=2,
        ).set_opacity(0)
        self.initial_cube = Cube(side_length=1, fill_color=cube_fill_color, stroke_color=cube_stroke_color, stroke_width=cube_stroke_width).set_opacity(1)
        self.cube_tracker = self.initial_cube.copy().set_opacity(0)
        self.cubes = VGroup()
        self.labels = VGroup()
        for i in range(self.cubes_num):
            self.labels.add(Tex(str(i+1),"열")
                            .move_to(self.axes.c2p(i+0.5,0,-0.5))
                            .shift(0.5*DOWN))
            self.cubes += VGroup()
            for j in range(i+1):
                cube = self.initial_cube.copy().move_to(self.axes.c2p(i+0.5,j+0.5,-0.5))
                self.cubes[i] += VGroup(cube)
            #myViewRotate(labels) #없어도 없어보임. 텍스트는 axes아래 붙여서 따로 안돌려도 돌아간 채로 붙나? axes에 평행하게?
        self.cdots = Tex(r"$\cdots$").next_to(self.cubes, RIGHT*2.5).scale(2)
        self.add(self.axes, self.cubes, self.labels, self.cdots, self.cube_tracker)

    def addCols(self, num):
        scale_factor = self.cube_tracker.width/self.initial_cube.width
        print(scale_factor)
        for i in range(self.cubes_num, self.cubes_num+num):
            self.labels.add(Tex(str(i+1),"열")
                            .move_to(self.axes.c2p(i+0.5,0,-0.5))
                            .shift(0.5*DOWN*scale_factor)
                            .scale(scale_factor))
            self.cubes += VGroup()
            for j in range(i+1):
                cube = self.cube_tracker.copy().set_opacity(1).move_to(self.axes.c2p(i+0.5,j+0.5,-0.5))
                self.cubes[i] += VGroup(cube)
            #myViewRotate(labels) #없어도 없어보임. 텍스트는 axes아래 붙여서 따로 안돌려도 돌아간 채로 붙나? axes에 평행하게?
        self.cdots.next_to(self.cubes, RIGHT*2.5*scale_factor)
        
    def popEvens(self):
        evenGroup = VGroup()   
        for i in range(self.cubes_num):
            if(len(self.cubes[i]) % 2 == 0):
                    for j in range(len(self.cubes[i])-1, len(self.cubes[i])//2-1, -1):
                        evenGroup.add(self.cubes[i][j])
                        self.cubes[i].remove(self.cubes[i][j])
        return evenGroup
    
    def selectEvenCols(self):
        evenCols = VGroup()
        for i in range(self.cubes_num):
            if(len(self.cubes[i]) % 2 == 0):
                evenCols.add(self.cubes[i])
        return evenCols
    
    def selectOddCols(self):
        oddCols = VGroup()
        for i in range(self.cubes_num):
            if(len(self.cubes[i]) % 2 == 1):
                oddCols.add(self.cubes[i])
        return oddCols
    
class Test(ThreeDScene):
    def construct(self):
        cubes = CubesGroup(16).scale_to_fit_width(4).to_corner(DL)
        self.play(StackCubes(cubes, 0, 16, None), run_time=2)
        cubes.addCols(16)
        self.play(StackCubes(cubes, 16, 32, None), run_time=2)

class Stack1ColCubes(AnimationGroup):
    def __init__(self, cubesGroup, col, shift, lag_ratio=0.3, **kwargs):
        super().__init__(
            FadeIn(cubesGroup.labels[col]),
            AnimationGroup(
                    *[
                        FadeIn(cubesGroup.cubes[col][j], shift=shift) 
                        for j in range(len(cubesGroup.cubes[col]))
                    ],
                    lag_ratio=lag_ratio
                )
            ,
            **kwargs
        )
    
class StackCubes(AnimationGroup):
    def __init__(self, cubesGroup, start_col, end_col, shift, col_lag_ratio=0.3, lag_ratio=0.3, **kwargs):
        super().__init__(
            *[
                Stack1ColCubes(cubesGroup, col, shift, col_lag_ratio, **kwargs)
                for col in range(start_col, end_col)
            ],
            lag_ratio=lag_ratio,
            **kwargs
        )

def questionSection(scene):
    texts = Group(TITLE.to_edge(UP),
                  TEXT1.next_to(TITLE, DOWN, aligned_edge = LEFT),
                  TEXT2.next_to(TEXT1, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(RIGHT*0.5),
                  SurroundingRectangle(TEXT2, buff=0.2, color = WHITE).set_stroke(width=2),
                  TEXT3.next_to(TEXT2, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(LEFT*0.5),
                  Eq.next_to(TEXT3, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(RIGHT),
                  TEXT4.next_to(Eq, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER+0.2, aligned_edge=LEFT).shift(LEFT),
                  ).to_edge(LEFT)
    scene.add(texts)
        
    cubesGroup = CubesGroup(6).scale_to_fit_width(CUBES_WIDTH).next_to(texts, RIGHT).shift(DOWN*0.5)

    cubesGroup.popEvens()
    cubesGroup.popEvens()

    scene.add(cubesGroup.rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP))
        
    # alter : 전체 add 먼저 하고 pop 한 뒤 지우는 방식
    # *안넣으면 안지워짐, *안넣고 FadeOut이나 Shift는 적용됨... 왜지?
    # self.remove(*popEvens(cubes, CUBES_NUM))

    scene.wait()
    scene.remove(cubesGroup)

    return texts

def describeBaseSituation(scene, texts):
    scene.play(Circumscribe(texts[1].get_part_by_tex("크기가 같은 정육면체 모양의 블록"), fade_out=True))

    sampleCubes = CubesGroup(3).scale_to_fit_width(CUBES_WIDTH).next_to(texts, RIGHT).shift(DOWN*0.5).rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP)
    for i in range(3):
        sampleCubes.cubes[i].set_fill_color(YELLOW)
        scene.play(Stack1ColCubes(sampleCubes, i, DOWN),
                   Circumscribe(texts[1].get_part_by_tex(str(i+1)+"열에 "+str(i+1)+"개"), fade_out=True))
        sampleCubes.cubes[i].set_fill_color(GREY)

    cubesGroup = CubesGroup(16).scale_to_fit_width(CUBES_WIDTH).next_to(texts, RIGHT).rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP)
    scene.play(TransformMatchingShapes(VGroup(sampleCubes.cubes, sampleCubes.labels), VGroup(cubesGroup.cubes[0:3], cubesGroup.labels[0:3])))
    scene.play(AnimationGroup(StackCubes(cubesGroup, 3, 16, None, run_time=2), FadeIn(cubesGroup.cdots), lag_ratio=0.8))
    return cubesGroup

def describeEvenIterate(scene, texts, cubesGroup):
    underline = VGroup(Underline(texts[1].get_part_by_tex("블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음\\")),
                       Underline(texts[1].get_part_by_tex("시행을 반복한다."))).set_color(RED).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(FadeOut(underline))

    for i in range(4):
        box = SurroundingRectangle(texts[2].get_part_by_tex("블록의 개수가 짝수인 각 열")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(box))
        scene.play(cubesGroup.selectEvenCols().animate.set_fill_color(YELLOW), cubesGroup.selectOddCols().animate.set_fill_color(GREY))
        scene.play(FadeOut(box))
        underline2 = Underline(texts[2].get_part_by_tex("만큼의 블록을 그 열에서 들어낸다.")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(underline2))
        evens = cubesGroup.popEvens()
        scene.play(evens.animate.shift(UP*0.3)) #or 콘티에 나온 대로 두번 깜빡이고 삭제 (Fadeout)
        scene.play(FadeOut(evens, shift=UP))
        scene.play(FadeOut(underline2))

    return cubesGroup

def descreibeEq(scene, text, eq, cubesGroup):
    scene.play(cubesGroup.cubes.animate.set_fill_color(GREY))
    underline = VGroup(Underline(text.get_part_by_tex(r"1열부터 $m$열까지\\")),
                       Underline(text.get_part_by_tex(r"남아 있는 블록의 개수의 합을 $f(m)$"))).set_color(RED).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(cubesGroup.cubes.animate.set_fill_color(YELLOW))
    circle = Circle(color=YELLOW).scale(0.2).move_to(cubesGroup.labels[-1][0])
    scene.play(Create(circle))
    fend = MathTex("f(","16",")").next_to(cubesGroup, DOWN)
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], fend[1]))
    scene.play(Write(fend[0]), Write(fend[2]))
    scene.play(FadeOut(underline), FadeOut(circle), FadeOut(fend), cubesGroup.cubes.animate.set_fill_color(GREY))
    eqbox = SurroundingRectangle(eq).set_color(RED).set_stroke(width=4)
    scene.play(Create(eqbox))
    scene.play(Indicate(eq.get_part_by_tex(r"^{n+1}")),
               Indicate(eq.get_part_by_tex(r"^{n}")),
               Indicate(eq.get_part_by_tex(r"^{n+2}")))
    return eqbox

class CSAT11_A_25(ThreeDScene):
    def construct(self):
        texts = questionSection(self)
        cubesGroup = describeBaseSituation(self, texts)
        cubesGroup = describeEvenIterate(self, texts, cubesGroup) #cubesGroup에 다시 할당 필요한지 확인 필요
        eqbox = descreibeEq(self, texts[4], texts[5], cubesGroup)