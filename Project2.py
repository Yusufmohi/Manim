from manim import *

class second(Scene):
    def construct(self):
        t=Tex("Hello ","there ","Obi","-","Wan")
        t[2].color=RED
        t[3].color=GREEN
        t[4].color=YELLOW
        self.play(Write(t[2:5]))
        self.play(Write(t[0:2]))
        self.play(t[0].animate.to_edge(UL,buff=1),t[1].animate.to_edge(UR,buff=1))
        self.play(t[2].animate.move_to([0,2,0]),t[3].animate.move_to([0,0,0]),t[4].animate.move_to([0,-2,0]))
        r=Rectangle(height=1,width=1).move_to([0,2,0])
        c=Circle(radius=0.5).move_to([0,0,0])
        p=RegularPolygon(5).move_to([0,-2,0]).scale(0.5)
        self.play(SpinInFromNothing(r),Write(c),SpinInFromNothing(p))
        rcp=VGroup(r,c,p)
        self.play(Rotate(rcp,angle=PI*3))
        tr=VGroup(t[2],p)
        tp=VGroup(t[4],r)
        self.play(Swap(tr,tp))
        self.wait(2)