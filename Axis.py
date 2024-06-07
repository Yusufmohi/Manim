from manim import *

class axis(Scene):
    def construct(Self):
        ax=Axes(x_range=(-10,10),y_range=(-10,10))
        tri=Triangle().scale(0.4)
        tri.move_to(ax.coords_to_point(-5,5))
        Self.play(Write(ax))
        Self.play(Write(tri))
        dot=Dot(color=GREEN)
        Self.play(Write(dot))
        Self.wait()
        Self.play(dot.animate.move_to(ax.coords_to_point(3,-5)))
        Self.wait()