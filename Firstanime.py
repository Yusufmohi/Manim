from manim import *

class first(Scene):
    def construct(self):
        t=Text("Hello there")
        self.play(write(t))