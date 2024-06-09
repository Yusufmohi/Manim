from manim import *

class thing2(Scene):
    def construct(self):
        x=Text("Mathematics",color=BLUE)
        y=Text("Physics",color=BLUE)
        g=VGroup(x,y,)
        g.arrange(DOWN,buff=2,center=False)
        self.play(Write(g))
        self.wait(2)







class thing(Scene):
    def construct(self):
        x=Text("Mathematics",color=BLUE)
        y=Text("Physics",color=BLUE)
        self.play(TransformMatchingShapes(x,y),run_time=5)
        self.wait(2)