from manim import *

class Animation(Scene):
    def construct(self):
        # Set up the coordinate plane
        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-2, 2, 1], axis_config={"include_numbers": True})
        self.play(Create(axes))
        self.wait(1)

        # Define the line y = 2x + 1
        line = axes.plot(lambda x: 2 * x + 1, color=BLUE)

        # Animate the drawing of the line
        self.play(Create(line), run_time=2)
        self.wait(1)

        # Define example points and their labels
        points = [(-1, -1), (0, 1), (1, 3), (2, 5)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=RED) for x, y in points])
        labels = VGroup(*[MathTex(f"({x}, {y})").scale(0.7).next_to(axes.c2p(x, y), UP) for x, y in points])

        # Animate the creation of the points and their labels
        for dot, label in zip(dots, labels):
            self.play(Create(dot), Write(label))
            self.wait(0.5)

        # Show the equation y = 2x + 1 at the top
        equation = MathTex("y = 2x + 1").scale(1.2).to_edge(UP)
        self.play(Write(equation))
        self.wait(1)

        # Highlight components of the equation
        two_x_comp = Rectangle(color=YELLOW, width=2, height=0.5).move_to(equation[2:4].get_center())
        plus_one_comp = Rectangle(color=GREEN, width=0.8, height=0.5).move_to(equation[5:7].get_center())
        
        self.play(Create(two_x_comp), Indicate(equation[2:4], color=YELLOW))
        self.wait(1)
        self.play(Transform(two_x_comp, plus_one_comp), Indicate(equation[5:7], color=GREEN))
        self.wait(1)

        # Clean up highlights
        self.play(FadeOut(two_x_comp))
        self.wait(1)