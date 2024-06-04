from manim import *

class first(Scene):
    def construct(self):
        c=Circle(radius=0.6,color=RED_C,stroke_width=4,fill_opacity=0.6)
        r=SurroundingRectangle(c,corner_radius=0.1,color=BLUE_C)
        t=Text("PHYSICS").next_to(r,UP,buff=0.6)
        self.play(Write(c),Write(r),Write(t))
        cr=VGroup(c,r)
        self.play(cr.animate.move_to([4,0,0]),t.animate.move_to([-4,0,0]))
        arrow=Line(buff=0.6,start = cr.get_left(),end = t.get_right()).add_tip(tip_shape=ArrowSquareTip).add_tip(tip_shape=ArrowSquareTip,at_start=True)
        self.play(Write(arrow))
        self.play(Indicate(t,2,color=GREEN_C))
        self.play(Rotate(r,angle=PI/2),ScaleInPlace(c,2))
        self.wait()