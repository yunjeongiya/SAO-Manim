from SAOlib import *
Tex.set_default(font_size=35)

# Tex의 내용 중 수식인 건 일단 Latex 로 넘기기 위해 $로 감싸주고, 그 안에서 또 Latex의 기호를 사용하는 경우 \로 알려줘야 한다.
# 즉, 그냥 \cdots 이나 $cdots$ 이렇게 쓰면 인식이 안되고, $\cdots$ 이렇게 써야 인식이 된다. 
TEXT1 = Tex(r'''자연수 $m$에 대하여 크기가 같은 정육면체 모양의 블록이\\
                1열에 1개, 2열에 2개, 3열에 3개, $\cdots$, $m$열에 $m$개가 쌓여 있다.\\
                블록의 개수가 짝수인 열이 남아 있지 않을 때까지 다음 시행을 반복한다.''')
TEXT2 = Tex(r'''블록의 개수가 짝수인 각 열에 대하여 그 열에 있는\\
                블록의 개수의 $\cfrac{1}{2}$ 만큼의 블록을 그 열에서 들어낸다.''')
TEXT3 = Tex(r'''블록을 들어내는 시행을 모두 마쳤을 때, 1열부터 $m$열까지\\
                남아 있는 블록의 개수의 합을 $f(m)$이라 하자.\\
                예를 들어, $f(2)=2$, $f(3)=5$, $f(4)=6$이다.\\
                $\lim\limits_{m\to\infty}\cfrac{f(2^{n+1})-f(2^n)}{f(2^{n+2})}=\cfrac{q}{p}$\\
                일 때, $p+q$의 값을 구하시오.\\
                (단, $p$와 $q$는 서로소인 자연수이다.) [4점]''')

class CSAT11_A_25(ThreeDScene) :
    def construct(self) :
        self.add(TEXT1.to_edge(UP), TEXT2.next_to(TEXT1, DOWN), TEXT3.next_to(TEXT2, DOWN))