from SAOlib import *
Tex.set_default(font_size=30, tex_environment="flushleft")
#Circumscribe.set_default(fade_out=True) #TODO set_default 없음. 감싸서 변형하는 방법 찾아보기

# Tex의 내용 중 수식인 건 일단 Latex 로 넘기기 위해 $로 감싸주고, 그 안에서 또 Latex의 기호를 사용하는 경우 \로 알려줘야 한다.
# 즉, 그냥 \cdots 이나 $cdots$ 이렇게 쓰면 인식이 안되고, $\cdots$ 이렇게 써야 인식이 된다. 
TITLE = Tex("11학년도 수능 수리 가형 25번")
TEXT1 = Tex(r"자연수 $m$에 대하여 ", "크기가 같은 정육면체 모양의 블록", r"이\\"
            r'''1열에 1개, 2열에 2개, 3열에 3개, $\cdots$, $m$열에 $m$개가 쌓여\\
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

#Square 소스코드 아이디어 참고 -> VGroup 상속받아 VGroup처럼 통째로 사용 가능하게 만들기
class CubesGroup(VGroup):
    def __init__(self, cubes_num):
        super().__init__()
        self.cubes_num = cubes_num
        self.axes = ThreeDAxes(
            x_range=[0, self.cubes_num, 1],
            y_range=[0, self.cubes_num, 1],
            z_range=[-1, 1, 1],
            x_length=self.cubes_num,
            y_length=self.cubes_num,
            z_length=2,
        )
        self.cubes = VGroup()
        self.labels = VGroup()
        for i in range(self.cubes_num):
            self.labels.add(Tex(str(i+1)+"열").move_to(self.axes.c2p(i+0.5,0,-0.5)).shift(0.5*DOWN))
            self.cubes += VGroup()
            for j in range(i+1):
                cube = Cube(side_length=1, fill_opacity=1, fill_color=GREY, stroke_color=WHITE, stroke_width=2).move_to(self.axes.c2p(i+0.5,j+0.5,-0.5))
                self.cubes[i] += VGroup(cube)
            #myViewRotate(labels) #없어도 없어보임. 텍스트는 axes아래 붙여서 따로 안돌려도 돌아간 채로 붙나? axes에 평행하게?
        self.cdots = Tex(r"$\cdots$").next_to(self.cubes, RIGHT*2).shift(DOWN).scale(2)
        self.add(self.cubes, self.labels, self.cdots)
        myViewRotate(self)
        
    def popOdds(self):
        oddGroup = VGroup()   
        for i in range(self.cubes_num):
            if(len(self.cubes[i]) % 2 == 0):
                    for j in range(len(self.cubes[i])-1, len(self.cubes[i])//2-1, -1):
                        oddGroup.add(self.cubes[i][j])
                        self.cubes[i].remove(self.cubes[i][j])
        return oddGroup

def questionSection(scene):
    texts = Group(TITLE.to_edge(UP),
                  TEXT1.next_to(TITLE, DOWN, aligned_edge = LEFT),
                  TEXT2.next_to(TEXT1, DOWN, aligned_edge=LEFT),
                  SurroundingRectangle(TEXT2, buff=0.1, color = WHITE).set_stroke(width=2),
                  TEXT3.next_to(TEXT2, DOWN, aligned_edge=LEFT)).to_edge(LEFT)
    scene.add(texts)
        
    cubesGroup = CubesGroup(CUBES_NUM)

    cubesGroup.popOdds()
    cubesGroup.popOdds()

    scene.add(cubesGroup.scale(0.7).next_to(texts, RIGHT).shift(DOWN*0.5))
        
    # alter : 전체 add 먼저 하고 pop 한 뒤 지우는 방식
    # *안넣으면 안지워짐, *안넣고 FadeOut이나 Shift는 적용됨... 왜지?
    # self.remove(*popOdds(cubes, CUBES_NUM))

    return texts, cubesGroup

class CSAT11_A_25(ThreeDScene) :
    def construct(self) :
        texts, cubesGroup = questionSection(self)
        self.wait()
        self.remove(cubesGroup)
        self.play(Circumscribe(texts[1].get_part_by_tex("크기가 같은 정육면체 모양의 블록"), fade_out=True))