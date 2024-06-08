from manim import *
import numpy as np

class axis4(Scene):
    def construct(self):
        axes=Axes(x_range=(-7,7),y_range=(-2,2),x_length=13,y_length=3,tips=False).add_coordinates().set_color(BLUE)
        x=axes.get_x_axis_label("X").set_color(GREEN)
        y=axes.get_y_axis_label("Y").set_color(GREEN)
        self.play(Write(axes),Write(x),Write(y))
        number=ValueTracker(1)
        curve1=always_redraw(lambda: axes.plot(lambda x:number.get_value()*x*x,color=YELLOW))
        self.play(Write(curve1))
        self.play(number.animate.set_value(2),run_time=2)
        self.play(number.animate.set_value(0.2),run_time=4)
        self.play(number.animate.set_value(7),run_time=2)
        self.wait(3)















class axis3(Scene):
    def construct(self):
        axes=Axes(x_range=(-7,7),y_range=(-2,2),x_length=13,y_length=3,tips=False).add_coordinates().set_color(BLUE)
        x=axes.get_x_axis_label("X").set_color(GREEN)
        y=axes.get_y_axis_label("Y").set_color(GREEN)
        self.play(Write(axes),Write(x),Write(y))
        curve1=axes.plot(lambda x: np.cos(x),color=RED)
        curve2=axes.plot(lambda x: x*x,color=YELLOW)
        self.play(Write(curve1),Write(curve2))
        self.wait(3)















class axis2(Scene):
    def construct(self):
        axes=Axes(x_range=(-1,6),y_range=(-1,5),x_length=13,y_length=6,tips=False).add_coordinates().set_color(BLUE)
        x=axes.get_x_axis_label("X").set_color(GREEN)
        y=axes.get_y_axis_label("Y").set_color(GREEN)
        self.play(Write(axes),Write(x),Write(y))
        dot=Dot(color=RED).move_to(axes.c2p(3,2))
        dot_label=always_redraw(lambda: Text("Dot",font_size=24).next_to(dot,UP))
        self.play(Write(dot),Write(dot_label))
        self.play(dot.animate.move_to(axes.c2p(6,5)))
        dot_label.clear_updaters()
        group=VGroup(axes,x,y,dot,dot_label)
        self.play(group.animate.scale(0.3).to_edge(UL))
        self.wait(2)













class axis(Scene):
    def construct(self):
        ax=Axes(x_range=(-10,10),y_range=(-10,10))
        tri=Triangle().scale(0.4)
        tri.move_to(ax.coords_to_point(-5,5))
        self.play(Write(ax))
        self.play(Write(tri))
        dot=Dot(color=GREEN)
        self.play(Write(dot))
        self.wait()
        self.play(dot.animate.move_to(ax.coords_to_point(3,-5)))
        self.wait()