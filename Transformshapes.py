from manim import *

class first(Scene):
    def construct(self):
        r=RoundedRectangle(corner_radius=4,fill_opacity=0.4,color=BLUE_D).shift(UP*3)
        t=Triangle(fill_opacity=0.6,color=RED_C).scale(3)
        self.add(r)
        self.wait(2)
        self.play(Transform(r,t),run_time=3)
        self.wait(2)
        rr=RoundedRectangle(corner_radius=0.7,fill_opacity=0.4,color=BLUE_D).shift(LEFT*3)
        tt=Triangle(fill_opacity=0.6,color=RED_C).scale(3).shift(RIGHT*3)
        self.play(DrawBorderThenFill(tt),Create(rr))
        self.wait(1)
