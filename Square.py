from manim import *

class first(Scene):
    def construct(self):
        s=Square(side_length=2, fill_opacity=0.6,color=RED_C)
        self.play(Write(s))
        self.wait(1)
        r=RoundedRectangle(corner_radius=4,fill_opacity=0.4,color=BLUE_D).shift(LEFT*3)
        self.play(Write(r))
        self.wait(1)