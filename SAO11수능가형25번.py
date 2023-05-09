from SAOlib import *
config.max_files_cached = -1
config.disable_caching = True
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

#Square 소스코드 아이디어 참고 -> VGroup 상속받아 VGroup처럼 통째로 사용 가능하게 만들기
    
class CubesGroup(VGroup):
    def __init__(self, cubes_num, cube_fill_color=GREY, cube_stroke_color=WHITE, cube_stroke_width=2):
        super().__init__()
        self.cubes_num = cubes_num
        self.axes = ThreeDAxes(
            x_range=[0, self.cubes_num, 1],
            y_range=[0, self.cubes_num, 1],
            z_range=[0, 1, 1],
            x_length=self.cubes_num,
            y_length=self.cubes_num,
            z_length=1,
        ).set_opacity(0)
        self.cubes = VGroup()
        self.initial_cube = Cube(side_length=1, fill_color=cube_fill_color, stroke_color=cube_stroke_color, stroke_width=cube_stroke_width).set_opacity(1)
        cube_tracker = self.initial_cube.copy().set_opacity(0)
        self.cubes += cube_tracker #index 0 번은 cube_tracker
        self.labels = VGroup(VMobject()) #index 0 번은 사용 x
        for i in range(1, self.cubes_num+1):
            self.labels.add(Tex(str(i),"열")
                            .move_to(self.axes.c2p(i-0.5,-0.5,0.5)))
            self.cubes += VGroup(VMobject()) #index 0 번은 사용 x
            for j in range(1, i+1):
                cube = self.initial_cube.copy().move_to(self.axes.c2p(i-0.5,j-0.5,0.5))
                self.cubes[i] += VGroup(cube)
        self.cdots = Tex(r"$\cdots$").next_to(self.cubes, RIGHT*2.5).scale(2)
        self.add(self.axes, self.cubes, self.labels, self.cdots)

    #override
    def rotate(self, angle: float, axis, about_point = None, **kwargs):
        rotateGroup = Group(self.axes, self.cubes, self.cdots, self.initial_cube)
        rotateGroup.rotate(angle, axis, about_point, **kwargs)
        for i in range(1, self.cubes_num+1):
            self.labels[i].move_to(self.axes.c2p(i-0.5,-0.5,0.5))
        return self

    def addCols(self, num):
        scale_factor = self.cubes[0].width/self.initial_cube.width
        #print("scale factor: ", scale_factor)
        for i in range(self.cubes_num+1, self.cubes_num+num+1):
            self.labels.add(Tex(str(i),"열")
                            .move_to(self.axes.c2p(i-0.5,-0.5,0.5))
                            .scale(scale_factor)
                            )
            self.cubes += VGroup(VMobject()) #index 0 번은 사용 x
            for j in range(1, i+1):
                cube = self.cubes[0].copy().set_opacity(1).move_to(self.axes.c2p(i-0.5,j-0.5,0.5))
                self.cubes[i] += VGroup(cube)
        self.cdots.next_to(self.cubes, RIGHT*2.5*scale_factor).scale(scale_factor)
        self.cubes_num += num
        
    def popEvens(self):
        evenGroup = VGroup()   
        for i in range(1, self.cubes_num+1):
            if((len(self.cubes[i]) - 1) % 2 == 0):
                    for j in range(len(self.cubes[i]) - 1, (len(self.cubes[i]) - 1)//2, -1):
                        evenGroup.add(self.cubes[i][j])
                        self.cubes[i].remove(self.cubes[i][j])
        return evenGroup
    
    def getEvenCols(self):
        evenCols = VGroup()
        for i in range(1, self.cubes_num+1):
            if((len(self.cubes[i]) - 1) % 2 == 0):
                evenCols.add(self.cubes[i])
        return evenCols
    
    def getOddCols(self):
        oddCols = VGroup()
        for i in range(1, self.cubes_num+1):
            if((len(self.cubes[i]) - 1) % 2 == 1):
                oddCols.add(self.cubes[i])
        return oddCols
    
    def getEventhCols(self):
        eventhCol = VGroup()
        for i in range(1, self.cubes_num+1):
            if(i % 2 == 0):
                eventhCol.add(self.cubes[i])
        return eventhCol
    
    def getOddthCols(self):
        oddthCol = VGroup()
        for i in range(1, self.cubes_num+1):
            if(i % 2 == 1):
                oddthCol.add(self.cubes[i])
        return oddthCol
    
class Test(ThreeDScene):
    def construct(self):
        cubesGroup = CubesGroup(64).scale_to_fit_height((config.frame_height-1)).to_corner(DL)
        while len(cubesGroup.getEvenCols()) > 0:
            cubesGroup.popEvens()

        self.add(cubesGroup)
        triangle = TriangleSpanningCubes(cubesGroup, 32)
        self.play(cubesGroup.cubes[:33].animate.set_fill_color(YELLOW),
               Create(triangle))
        self.play(cubesGroup.cubes[33:65].animate.set_fill_color(YELLOW),
               Transform(triangle, TriangleSpanningCubes(cubesGroup, 65)))

        self.play(cubesGroup.getOddthCols().animate.set_fill_color(YELLOW),
        cubesGroup.getEventhCols().animate.set_fill_color(PURE_GREEN))
    
        self.play(FadeOut(cubesGroup.getEventhCols()))

class Stack1ColCubes(AnimationGroup):
    def __init__(self, cubesGroup, col, shift=None, lag_ratio=0.3, **kwargs):
        #print("col: ", col, "len: ", len(cubesGroup.cubes[col])) #debug
        # col:  1 len:  2 / col:  2 len:  3 / col:  3 len:  4 -> 0번인덱스를 사용 안할 뿐 채워져는 있어서 len은 col+1
        super().__init__(
            FadeIn(cubesGroup.labels[col]),
            AnimationGroup(
                    *[
                        FadeIn(cubesGroup.cubes[col][j], shift=shift)
                        for j in range(1, len(cubesGroup.cubes[col]))
                    ],
                    lag_ratio=lag_ratio
                )
            ,
            **kwargs
        )
    
class StackCubes(AnimationGroup):
    def __init__(self, cubesGroup, start_col, end_col, shift=None, col_lag_ratio=0.3, lag_ratio=0.3, **kwargs):
        super().__init__(
            *[
                Stack1ColCubes(cubesGroup, col, shift, col_lag_ratio, **kwargs)
                for col in range(start_col, end_col+1)
            ],
            lag_ratio=lag_ratio,
            **kwargs
        )

'''
class FadeOutAllEvens(Succession):
    def __init__(self, cubesGroup, shift=UP, **kwargs):
        animations = []
        while len(cubesGroup.getEvenCols()) > 0:
           animations += [AnimationGroup(cubesGroup.getEvenCols().animate.set_fill_color(YELLOW), cubesGroup.getOddCols().animate.set_fill_color(GREY))]
           animations += [FadeOut(cubesGroup.popEvens(), shift=shift)] #popEvens()로 cubesGroup에 변화가 생김 -> FadeOutAllEvens객체 생성 후 play()될 때 문제 발생
        super().__init__(
            *animations, **kwargs
        )
'''

def fadeOutAllEvens(cubesGroup, scene, shift=UP):
    while len(cubesGroup.getEvenCols()) > 0:
        scene.play(AnimationGroup(cubesGroup.getEvenCols().animate.set_fill_color(YELLOW), cubesGroup.getOddCols().animate.set_fill_color(GREY)))
        scene.play(FadeOut(cubesGroup.popEvens(), shift=shift))

class TriangleSpanningCubes(Polygon) :
    def __init__(self, cubesGroup, col, color=PURE_RED, stroke_width=6, **kwargs):
        super().__init__(cubesGroup.axes.c2p(0,0,0.5), cubesGroup.axes.c2p(col, 0, 0.5), cubesGroup.axes.c2p(col, col, 0.5), color=color, stroke_width=stroke_width, **kwargs)

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
        
    cubesGroup = CubesGroup(6).scale_to_fit_width(config.frame_width/3).next_to(texts, RIGHT).shift(DOWN*0.5)

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
    cubesGroup = CubesGroup(3).scale_to_fit_width(config.frame_width/3).next_to(texts, RIGHT).shift(DOWN*0.5).rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP)
    for i in range(1, 4):
        cubesGroup.cubes[i].set_fill_color(YELLOW)
        scene.play(Stack1ColCubes(cubesGroup, i, DOWN),
                   Circumscribe(texts[1].get_part_by_tex(str(i)+"열에 "+str(i)+"개"), fade_out=True))
        cubesGroup.cubes[i].set_fill_color(GREY)
    scene.play(Group(cubesGroup.cubes[:4], cubesGroup.labels[:4], cubesGroup.axes).animate.scale(1/4, about_point=cubesGroup.axes.c2p(0, 0, 0)))
    cubesGroup.addCols(13)
    scene.play(AnimationGroup(StackCubes(cubesGroup, 4, 16, run_time=2), FadeIn(cubesGroup.cdots), lag_ratio=0.8))
    return cubesGroup

def describeEvenIterate(scene, texts, cubesGroup):
    underline = VGroup(Underline(texts[1].get_part_by_tex("블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음\\")),
                       Underline(texts[1].get_part_by_tex("시행을 반복한다."))).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(FadeOut(underline))

    while len(cubesGroup.getEvenCols()) > 0:
        box = SurroundingRectangle(texts[2].get_part_by_tex("블록의 개수가 짝수인 각 열")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(box))
        scene.play(cubesGroup.getEvenCols().animate.set_fill_color(YELLOW), cubesGroup.getOddCols().animate.set_fill_color(GREY))
        scene.play(FadeOut(box))
        underline2 = Underline(texts[2].get_part_by_tex("만큼의 블록을 그 열에서 들어낸다.")).set_color(YELLOW).set_stroke(width=4)
        scene.play(Create(underline2))
        evens = cubesGroup.popEvens()
        scene.play(evens.animate.shift(UP*0.3)) #or 콘티에 나온 대로 두번 깜빡이고 삭제 (Fadeout)
        scene.play(FadeOut(evens, shift=UP))
        scene.play(FadeOut(underline2))

    return cubesGroup

def descreibeEq(scene, text, eq, cubesGroup):
    scene.play(cubesGroup.cubes[:17].animate.set_fill_color(GREY))
    underline = VGroup(Underline(text.get_part_by_tex(r"1열부터 $m$열까지\\")),
                       Underline(text.get_part_by_tex(r"남아 있는 블록의 개수의 합을 $f(m)$"))).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(underline))
    scene.play(cubesGroup.cubes[:17].animate.set_fill_color(YELLOW))
    circle = Circle(color=YELLOW).scale(0.2).move_to(cubesGroup.labels[-1][0])
    scene.play(Create(circle))
    fend = MathTex("f(","16",")").next_to(cubesGroup, DOWN)
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], fend[1]))
    scene.play(Write(fend[0]), Write(fend[2]))
    scene.play(FadeOut(underline), FadeOut(circle), FadeOut(fend), cubesGroup.cubes[:17].animate.set_fill_color(GREY))
    eqbox = SurroundingRectangle(eq).set_color(YELLOW).set_stroke(width=4)
    scene.play(Create(eqbox))
    scene.play(Indicate(eq.get_part_by_tex(r"^{n+1}")),
               Indicate(eq.get_part_by_tex(r"^{n}")),
               Indicate(eq.get_part_by_tex(r"^{n+2}")))
    return eqbox

def iteratingMore(scene, texts, cubesGroup, eqbox):
    eq = texts[5]
    scene.play(FadeOut(texts[0:5], texts[6], eqbox), eq.animate.to_edge(UP).scale(1.5),
               Group(cubesGroup.cubes[:17], cubesGroup.labels[:17], cubesGroup.axes)
               .animate.to_corner(DL).shift(DOWN*0.5).rotate(20*DEGREES, axis=UP).scale_to_fit_height((config.frame_height-1)/2))
    fend = MathTex("f(","16",")").next_to(eq, DOWN*2).shift(LEFT)
    scene.play(Write(fend))
    potentialTex = MathTex(r"2^",r"4").move_to(fend[1])
    potentialTex[1].set_color(YELLOW)
    scene.play(Transform(fend[1], potentialTex))

    cubesGroup.addCols(16)
    scene.play(StackCubes(cubesGroup, 17, 32, None, run_time=2))
    potentialTex = MathTex(r"2^",r"5").move_to(fend[1])
    potentialTex[1].set_color(YELLOW)
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], potentialTex))
    scene.play(Transform(fend[1], potentialTex), FadeOut(potentialTex))
    fadeOutAllEvens(cubesGroup, scene)
    scene.play(Group(cubesGroup.cubes[:33], cubesGroup.labels[:33], cubesGroup.axes)
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    
    cubesGroup.addCols(32)
    scene.play(StackCubes(cubesGroup, 33, 64, None, run_time=2))
    potentialTex = MathTex(r"2^",r"6").move_to(fend[1])
    potentialTex[1].set_color(YELLOW)
    scene.play(TransformFromCopy(cubesGroup.labels[-1][0], potentialTex))
    scene.play(Transform(fend[1], potentialTex), FadeOut(potentialTex))
    fadeOutAllEvens(cubesGroup, scene)

    return fend

def neglectEventhCols(scene, cubesGroup, fend):
    potentialTex4 = MathTex(r"2^",r"4").set_color(YELLOW).move_to(fend[1])
    potentialTex5 = MathTex(r"2^",r"5").set_color(YELLOW).move_to(fend[1])
    potentialTex6 = MathTex(r"2^",r"6").set_color(YELLOW).move_to(fend[1])

    scene.play(cubesGroup.cubes[-1].animate.set_fill_color(GREY), 
               Transform(fend[1][1], potentialTex4[1]),
               cubesGroup.cubes[:17].animate.set_fill_color(YELLOW))
    scene.play(Transform(fend[1][1], potentialTex5[1]),
               cubesGroup.cubes[:33].animate.set_fill_color(YELLOW))
    scene.play(Transform(fend[1][1], potentialTex6[1]),
               cubesGroup.cubes[:65].animate.set_fill_color(YELLOW))
    
    triangle = TriangleSpanningCubes(cubesGroup, 16)
    scene.play(Transform(fend[1][1], potentialTex4[1]),
               cubesGroup.cubes[17:65].animate.set_fill_color(GREY),
               Create(triangle))
    scene.play(Transform(fend[1][1], potentialTex5[1]),
               cubesGroup.cubes[17:33].animate.set_fill_color(YELLOW),
               Transform(triangle, TriangleSpanningCubes(cubesGroup, 32)))
    scene.play(Transform(fend[1][1], potentialTex6[1]),
                cubesGroup.cubes[33:65].animate.set_fill_color(YELLOW),
                Transform(triangle, TriangleSpanningCubes(cubesGroup, 64)))
    
    scene.play(FadeOut(triangle), cubesGroup.cubes[:65].animate.set_fill_color(GREY))

    scene.play(cubesGroup.getOddthCols().animate.set_fill_color(YELLOW),
               cubesGroup.getEventhCols().animate.set_fill_color(PURE_GREEN))
    
    scene.play(FadeOut(cubesGroup.getEventhCols()))

def iteratingMoreOnyWithOddCols(scene, cubesGroup, fend):
    potentialTex7 = MathTex(r"2^",r"7").set_color(YELLOW).move_to(fend[1])
    potentialTex8 = MathTex(r"2^",r"8").set_color(YELLOW).move_to(fend[1])

    scene.play(Group(cubesGroup.cubes[:65], cubesGroup.labels[:65], cubesGroup.axes)
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)),
               FadeOut(cubesGroup.labels[:65]))
    cubesGroup.addCols(64)
    scene.play(FadeIn(cubesGroup.getOddthCols()),
               Transform(fend[1][1], potentialTex7[1]))

    scene.play(Group(cubesGroup.cubes[:129], cubesGroup.axes)
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(128)
    scene.play(FadeIn(cubesGroup.getOddthCols()),
               Transform(fend[1][1], potentialTex8[1]))

    scene.play(Group(cubesGroup.cubes[:257], cubesGroup.axes)
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)),
               FadeOut(fend))
    cubesGroup.addCols(256)
    scene.play(FadeIn(cubesGroup.getOddthCols()))

    scene.play(Group(cubesGroup.cubes[:513], cubesGroup.axes)
               .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(512)
    scene.play(FadeIn(cubesGroup.getOddthCols()))

    scene.play(Group(cubesGroup.cubes[:1025], cubesGroup.axes)
                .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(1024)
    scene.play(FadeIn(cubesGroup.getOddthCols()))

    scene.play(Group(cubesGroup.cubes[:2049], cubesGroup.axes)
                .animate.scale(1/2, about_point=cubesGroup.axes.c2p(0,0,0)))
    cubesGroup.addCols(2048)
    scene.play(FadeIn(cubesGroup.getOddthCols()))

class CSAT11_A_25(ThreeDScene):
    def construct(self):
        self.next_section(skip_animations=True)
        texts = questionSection(self)
        cubesGroup = describeBaseSituation(self, texts)
        describeEvenIterate(self, texts, cubesGroup) #cubesGroup에 다시 할당 필요한지 확인 필요
        eqbox = descreibeEq(self, texts[4], texts[5], cubesGroup)
        fend = iteratingMore(self, texts, cubesGroup, eqbox)
        neglectEventhCols(self, cubesGroup, fend)
        iteratingMoreOnyWithOddCols(self, cubesGroup, fend)