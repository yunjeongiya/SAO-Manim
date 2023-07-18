from manim import *

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
    
    def getEventhCols(self, start=1, end=None):
        if(end == None):
            end = self.cubes_num
        eventhCol = VGroup()
        for i in range(start, end+1):
            if(i % 2 == 0):
                eventhCol.add(self.cubes[i])
        return eventhCol
    
    def getOddthCols(self, start=1, end=None):
        if(end == None):
            end = self.cubes_num
        oddthCol = VGroup()
        for i in range(start, end+1):
            if(i % 2 == 1):
                oddthCol.add(self.cubes[i])
        return oddthCol
    
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

def twoPotentialTexBuilder(exponent):
    potentialTex = MathTex(r"2^",r"{}".format(exponent))
    potentialTex[1].set_color(YELLOW)
    return potentialTex

class TriangleSpanningCubes(Polygon) :
    def __init__(self, cubesGroup, col, color=PURE_RED, stroke_width=6, **kwargs):
        super().__init__(cubesGroup.axes.c2p(0,0,0.5), cubesGroup.axes.c2p(col, 0, 0.5), cubesGroup.axes.c2p(col, col, 0.5), color=color, stroke_width=stroke_width, **kwargs)
