from manim import *

class Animation(Scene):
    def construct(self):
        # Step 1: Create a 3x3 grid to visualize 3 squared
        squares = VGroup(*[Square() for _ in range(9)]).arrange_in_grid(3, 3, buff=0.1)
        squares.scale(0.5)
        
        # Position the grid at the center
        squares.move_to(ORIGIN)
        
        # Step 2: Label each row and column with the number "3"
        row_label = MathTex("3").scale(0.8).next_to(squares, LEFT, buff=0.3)
        column_label = MathTex("3").scale(0.8).next_to(squares, UP, buff=0.3)
        
        # Step 3: Sequentially highlight each square in the grid
        self.play(Create(squares))
        self.play(Write(row_label), Write(column_label))
        self.wait(1)
        
        for square in squares:
            self.play(Indicate(square, scale_factor=1.2, color=BLUE), run_time=0.5)
        
        # Step 4: Show "3 × 3" turning into "9"
        multiplication_text = MathTex("3 \\times 3 = ").scale(0.8).next_to(squares, DOWN, buff=0.5)
        result_text = MathTex("9").scale(0.8)
        self.play(Write(multiplication_text))
        
        # Position "9" near "3 x 3" but slightly separated for transition
        result_text.next_to(multiplication_text, RIGHT)
        
        self.play(Transform(multiplication_text.copy(), result_text))
        self.wait(1)
        
        # Step 5: Display "3² = 9" and transition it
        squared_text = MathTex("3^2", " = ", "9").scale(0.8)
        squared_text.move_to(squares.get_bottom() + DOWN * 1)
        
        # Transform multiplication into exponent notation
        self.play(Transform(multiplication_text, squared_text))
        self.wait(1)
        
        # Step 6: Emphasize the whole result of 9 squares
        self.play(Circumscribe(squares, color=GREEN, run_time=2))
        self.wait(1)
        
        # Final clarification text
        conclusion_text = MathTex("3 \\text{ Squared } = 9").scale(0.8)
        conclusion_text.move_to(squares.get_bottom() + 2 * DOWN)
        self.play(Write(conclusion_text))
        
        self.wait(2)  # Allow the audience to absorb the conclusion