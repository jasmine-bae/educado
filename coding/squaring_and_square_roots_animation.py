# filename: squaring_and_square_roots_animation.py
from manim import *

class SquareAndSquareRoots(Scene):
    def construct(self):
        # 1. Introduction to Squaring a Number
        intro_text = Text("How to Square a Number", font_size=48)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Example of squaring 3
        example_text = MathTex("3^2", "=", "3 \\times 3", "= 9")
        grid_title = Text("3 by 3 grid representation:", font_size=36).shift(UP * 2)
        grid = VGroup(*[Square() for _ in range(9)]).arrange_in_grid(3, 3).scale(0.5)
        
        self.play(Write(example_text))
        self.wait(1)
        self.play(example_text.animate.to_edge(UP))
        self.play(Write(grid_title), Create(grid))
        self.wait(2)
        self.play(FadeOut(grid_title), FadeOut(grid))

        # 2. Squared Numbers from 0² to 6²
        squares_text = MathTex(
            "0^2 = 0,\\\\, 1^2 = 1,\\\\, 2^2 = 4,\\\\, 3^2 = 9,\\\\, "
            "4^2 = 16,\\\\, 5^2 = 25,\\\\, 6^2 = 36"
        )
        self.play(FadeOut(example_text), Write(squares_text))
        self.wait(4)
        self.play(FadeOut(squares_text))

        # 3. Squaring Negative Numbers
        negative_text = MathTex("(-5)^2 = (-5) \\times (-5) = 25")
        self.play(Write(negative_text))
        self.wait(2)
        positive_text = MathTex("5^2 = 5 \\times 5 = 25")
        same_result = Text("(Positive result)", font_size=24).next_to(negative_text, DOWN)
        self.play(Write(positive_text), Write(same_result))
        self.wait(2)
        self.play(FadeOut(negative_text), FadeOut(positive_text), FadeOut(same_result))

        # 4. Square Roots
        sqrt_intro = Text("Square Roots", font_size=48)
        sqrt_example = MathTex("\\sqrt{9} = 3", "\\,\\text{because}\\, 3^2 = 9").arrange(DOWN)
        
        self.play(Write(sqrt_intro))
        self.wait(2)
        self.play(sqrt_intro.animate.to_edge(UP))
        self.play(Write(sqrt_example))
        self.wait(3)

        # Conclusion
        conclusion_text = Text("Squaring and Square Roots Explained", font_size=36).next_to(sqrt_example, DOWN)
        self.play(Write(conclusion_text))
        
        self.wait(3)
        self.play(FadeOut(conclusion_text), FadeOut(sqrt_example), FadeOut(sqrt_intro))
