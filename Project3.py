from manim import *

class second(Scene):
    def construct(self):
        c=Circle().scale(0.1)
        c.set_fill(WHITE,opacity=1)
        c.set_stroke(RED,width=7)
        r=SurroundingRectangle(c,color=RED,corner_radius=0.1)
        cr=VGroup(c,r)
        t=Text("Theoretical Physics",font_size=32)
        t[0:11].set_color(RED)
        t[11:].set_color(BLUE)
        g=VGroup(cr,t)
        g.arrange(RIGHT)
        self.play(SpinInFromNothing(cr))
        self.play(Write(t))
        rr=SurroundingRectangle(t[11:],corner_radius=0.001,)
        self.play(Write(rr))
        g1=VGroup(t[11:],rr)
        self.play(cr.animate.next_to(t[0:11],UP,buff=1.5),g1.animate.next_to(t[0:11],DOWN,buff=1.5))
        self.play(rr.animate.scale(4).move_to(ORIGIN),g.animate.move_to(ORIGIN),cr.animate.move_to(ORIGIN).shift(UP*0.5),t[11:].animate.move_to(ORIGIN).shift(DOWN*0.5))
        g4=VGroup(c,r,t,rr)
        dot=Dot(color=WHITE).scale(0.5)
        self.play(Transform(g4,dot))
        self.wait()
        self.play(dot.animate.scale(200),run_time=0.5)
        b=Text("BIG BANG!",color=WHITE,font_size=70,stroke_width=3)
        self.play(TransformMatchingShapes(dot,b),FocusOn(b,run_time=0.5))
        self.play(Indicate(b,color=RED),Flash(b[0:],line_length=0.8,flash_radius=2))

        
        
        self.wait(2)
        
        