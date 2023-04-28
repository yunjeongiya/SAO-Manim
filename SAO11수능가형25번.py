from SAOlib import *
Tex.set_default(font_size=30, tex_environment="flushleft")

# Tex의 내용 중 수식인 건 일단 Latex 로 넘기기 위해 $로 감싸주고, 그 안에서 또 Latex의 기호를 사용하는 경우 \로 알려줘야 한다.
# 즉, 그냥 \cdots 이나 $cdots$ 이렇게 쓰면 인식이 안되고, $\cdots$ 이렇게 써야 인식이 된다. 
TITLE = Tex("11학년도 수능 수리 가형 25번")
TEXT1 = Tex(r'''자연수 $m$에 대하여 크기가 같은 정육면체 모양의 블록이\\
                1열에 1개, 2열에 2개, 3열에 3개, $\cdots$, $m$열에 $m$개가 쌓여\\
                있다. 블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음\\
                시행을 반복한다.''')
TEXT2 = Tex(r'''블록의 개수가 짝수인 각 열에 대하여 그 열에 있는\\
                블록의 개수의 $\cfrac{1}{2}$ 만큼의 블록을 그 열에서 들어낸다.''')
TEXT3 = Tex(r'''블록을 들어내는 시행을 모두 마쳤을 때, 1열부터 $m$열까지\\
                남아 있는 블록의 개수의 합을 $f(m)$이라 하자.\\
                예를 들어, $f(2)=2$, $f(3)=5$, $f(4)=6$이다.\\
                $\lim\limits_{m\to\infty}\cfrac{f(2^{n+1})-f(2^n)}{f(2^{n+2})}=\cfrac{q}{p}$\\
                일 때, $p+q$의 값을 구하시오.\\
                (단, $p$와 $q$는 서로소인 자연수이다.) [4점]''')

CUBES_NUM = 6 #함수 정의할 때 인자로 받는게 나은지, 어차피 상수로 정의했으니 함수 안에서 바로 쓰는게 나은지?

def myViewRotate(mob):
    mob.rotate(5*DEGREES, axis=RIGHT).rotate(-20*DEGREES, axis=UP)

def createCubes(axes, cubes_num):
    myViewRotate(axes)
    cubes = []
    for i in range(cubes_num):
        cubes.append([])
        for j in range(i+1):
            cube = Cube(side_length=1, fill_opacity=1, fill_color=GREY, stroke_color=WHITE, stroke_width=2).move_to(axes.c2p(i+0.5,j+0.5,-0.5))
            myViewRotate(cube)
            cubes[i] += VGroup(cube)
    return cubes

def scaleCubes(axes, cubes, cubes_num, scale):
    axes.scale(scale)
    for i in range(cubes_num):
        for j in range(len(cubes[i])):
            cubes[i][j].scale(scale).move_to(axes.c2p(i+0.5,j+0.5,-0.5))

def popOdds(cubes, cubes_num):
    oddGroup = VGroup()   
    for i in range(cubes_num):
            if(len(cubes[i]) % 2 == 0):
                    for j in range(len(cubes[i])-1, len(cubes[i])//2-1, -1):
                        oddGroup.add(cubes[i].pop(j))
    return oddGroup

class CSAT11_A_25(ThreeDScene) :
    def construct(self) :
        texts = Group(TITLE.to_edge(UP),
                      TEXT1.next_to(TITLE, DOWN, aligned_edge = LEFT),
                      TEXT2.next_to(TEXT1, DOWN, aligned_edge=LEFT),
                      SurroundingRectangle(TEXT2, buff=0.1, color = WHITE).set_stroke(width=2),
                      TEXT3.next_to(TEXT2, DOWN, aligned_edge=LEFT)).to_edge(LEFT)
        self.add(texts)
        axes = ThreeDAxes(
            x_range=[0, CUBES_NUM, 1],
            y_range=[0, CUBES_NUM, 1],
            z_range=[-1, 1, 1],
            x_length=CUBES_NUM,
            y_length=CUBES_NUM,
            z_length=2,
        ).next_to(texts, RIGHT).shift(LEFT)
        cubes = createCubes(axes, CUBES_NUM)
        
        scaleCubes(axes, cubes, CUBES_NUM, 0.7)
        popOdds(cubes, CUBES_NUM)
        popOdds(cubes, CUBES_NUM)

        for i in range(CUBES_NUM):
            for j in range(len(cubes[i])):
                self.add(cubes[i][j])
        
        # alter : 전체 add 먼저 하고 pop 한 뒤 지우는 방식
        # *안넣으면 안지워짐, *안넣고 FadeOut이나 Shift는 적용됨... 왜지?
        # self.remove(*popOdds(cubes, CUBES_NUM))