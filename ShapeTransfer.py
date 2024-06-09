from manim import *

class thing(Scene):
    def construct(self):
        x=Text("Mathematics",color=BLUE)
        y=Text("Physics",color=BLUE)
        self.play(TransformMatchingShapes(x,y),run_time=5)
        self.wait(2)