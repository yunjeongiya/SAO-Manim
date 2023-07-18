from manim import *

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
Eq = MathTex(r"\lim\limits_{n\to\infty}{{",r"f(2",r"^{n+1}",r")",r"-",r"f(2",r"^{n}",r")}",r"\over",r"{f(2",r"^{n+2}",r")}",r"}=",r"{{q}",r"\over",r"{p}}", font_size=30)
TEXT4 = Tex("일 때, ", r"$p+q$", r'''의 값을 구하시오.\\
                (단, $p$와 $q$는 서로소인 자연수이다.) [4점]''')