from manim import *

class Value(Scene):
    def construct(self):
        t1=ValueTracker(10)
        number=always_redraw(lambda:DecimalNumber(t1.get_value(),num_decimal_places=0))
        self.play(Write(number))
        self.play(t1.animate.set_value(30),run_time=5,rate_func=rate_functions.linear)
        self.wait(2)
