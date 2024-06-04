from manim import *

class first(Scene):
    def construct(self):
        self.add(NumberPlane())
        t=Text("Hello there!",color=BLUE,weight=BOLD,font_size=64).shift(RIGHT*3,UP*2)
        self.play(Write(t))
        self.wait(1)
        self.play(Unwrite(t))
        s=Square(side_length=2,color=BLUE_C).shift(LEFT*3,DOWN*2)
        self.play(Write(s))
        self.wait(1)
