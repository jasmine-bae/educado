from manim import *

class Animation(Scene):
    def construct(self):
        # Introduction text explaining squaring a number
        intro_text = Text("How to Square a Number", font_size=48)
        
        # Explanation: 3 squared is 3 rows of 3 squares each
        explanation = Text("3 squared means 3 rows of 3 squares each.", font_size=36).scale(0.8)
        
        # Move the explanation text downwards
        explanation.next_to(intro_text, DOWN, buff=0.5)

        # Add and display introduction and explanation text
        self.play(Write(intro_text))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)

        # Create a 3x3 grid of squares to visually represent 3 squared
        square_grid = VGroup(*[Square().scale(0.5) for _ in range(3*3)])
        square_grid.arrange_in_grid(rows=3, buff=0.1)
        square_grid.shift(DOWN * 0.5)
        
        # Add a label to the grid
        grid_label = MathTex("3 \\times 3 = 9").next_to(square_grid, DOWN, buff=0.3).scale(0.8)

        # Display the 3x3 grid
        self.play(Create(square_grid))
        self.wait(1)

        # Show the multiplication expression
        self.play(Write(grid_label))
        self.wait(1)

        # Fade out all elements to transition to next concept
        self.play(FadeOut(square_grid), FadeOut(grid_label), FadeOut(intro_text), FadeOut(explanation))
        self.wait(1)

        # Display the concept of squares from 0² to 6²
        square_exp_list = [
            MathTex(f"{i}^2 = {i} \\times {i} = {i*i}") for i in range(7)
        ]

        # Arrange these square expressions vertically with equal spacing
        for i, square_exp in enumerate(square_exp_list):
            if i == 0:
                square_exp.shift(UP * 1.5)  # position the first at the top
            else:
                square_exp.next_to(square_exp_list[i-1], DOWN, buff=0.5)
        
        # Create each row of the square expressions
        for square_exp in square_exp_list:
            self.play(Write(square_exp))
            self.wait(0.5)

        # Focus the animation on the equivalence of squaring positive and negative 5
        indicate_expression = MathTex("5 \\times 5 = \\left(-5\\right) \\times \\left(-5\\right)").scale(0.8)
        indicate_expression.shift(DOWN * 1.5)
        
        # Transform squares to explain negative number squaring
        self.play(FadeOut(VGroup(*square_exp_list)))
        self.play(Write(indicate_expression))
        self.wait(2)

        # Emphasize the concept using Indicate animation
        self.play(Indicate(indicate_expression))
        self.wait(1)

        # End the scene with a fade out
        self.play(FadeOut(indicate_expression))
        self.wait(1)