from manim import Scene, Write, MathTex, VGroup, Square, FadeIn, FadeOut, Create, ReplacementTransform, Text

class Animation(Scene):
    def construct(self):
        # Title and Introduction of the Concept
        title = Text("Squaring a Number").scale(0.8).to_edge(UP)
        introduction = Text("To square a number: multiply it by itself").scale(0.7)

        # Initial Display of the Title
        self.play(Write(title))
        self.wait(1)

        # Display the Introduction Text
        self.play(Write(introduction))
        self.wait(2)
        self.play(FadeOut(introduction))
        
        # Explain the squaring of number 3
        number_3_grid = VGroup()  # Group to hold the grid of squares
        for i in range(3):
            for j in range(3):
                square = Square().scale(0.5)  # Creating a single square
                square.shift(LEFT + UP * 0.5)  # Initial position adjustment
                square.shift(i * RIGHT * 0.5)  # Shift for grid alignment
                square.shift(j * DOWN * 0.5)  # Shift for grid alignment
                number_3_grid.add(square)  # Add to the grid group

        # Equation showing the squaring process
        eq_3_squared = MathTex("3^2 = 3 \\times 3 = 9").scale(0.8)
        eq_3_squared.next_to(number_3_grid, RIGHT, buff=0.5)  # Position the equation to the right

        # Animate the drawing of squares to form a grid
        self.play(Create(number_3_grid))
        self.wait(1)

        # Write the equation next to the grid
        self.play(Write(eq_3_squared))
        self.wait(2)

        # Animation of Exponent Notation
        expo_notation = MathTex("3^2").scale(1.0)
        self.play(ReplacementTransform(eq_3_squared[0], expo_notation))
        self.wait(1)

        # Sequential presentation of perfect squares from 0 to 6
        squares_list = VGroup(
            MathTex("0^2 = 0").scale(0.7),
            MathTex("1^2 = 1").scale(0.7),
            MathTex("2^2 = 4").scale(0.7),
            MathTex("3^2 = 9").scale(0.7),
            MathTex("4^2 = 16").scale(0.7),
            MathTex("5^2 = 25").scale(0.7),
            MathTex("6^2 = 36").scale(0.7)
        ).arrange(DOWN, buff=0.3).to_edge(LEFT)

        # Animate appearance of each perfect square equation
        for square in squares_list:
            self.play(FadeIn(square))
            self.wait(0.5)

        # Pause at the end of the sequence
        self.wait(2)