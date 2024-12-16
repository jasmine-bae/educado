# filename: similar_triangles.py
from manim import *

class SimilarTriangles(Scene):
    def construct(self):
        # Create triangles R and S
        triangle_R = Polygon([-3, 0, 0], [-4, 2, 0], [-1, 1, 0], color=BLUE)
        triangle_S = Polygon([1, 0, 0], [1.5, 1.2, 0], [3, 1, 0], color=GREEN)
        
        # Labels for triangle R
        label_R = MathTex("R: (6, 7, 8)").next_to(triangle_R, DOWN)
        side_R_6 = MathTex("6").move_to(triangle_R.get_center() + LEFT * 1.5)
        side_R_7 = MathTex("7").move_to(triangle_R.get_center() + UP * 1.2)
        side_R_8 = MathTex("8").move_to(triangle_R.get_center() + RIGHT * 0.6)

        # Labels for triangle S with known sides
        label_S = MathTex("S: (b, a, 6.4)").next_to(triangle_S, DOWN)
        side_S_6_4 = MathTex("6.4").move_to(triangle_S.get_center() + RIGHT * 2)

        # Add triangles and their labels to the scene
        self.play(Create(triangle_R), Create(triangle_S))
        self.play(Write(label_R), Write(label_S))
        self.play(Write(side_R_6), Write(side_R_7), Write(side_R_8), Write(side_S_6_4))

        # Calculation of the ratio
        ratio_text = MathTex(r"Ratio = \\frac{6.4}{8} = 0.8").to_edge(UP)
        self.play(Write(ratio_text))

        # Calculating side a and b
        calc_a = MathTex(r"a = 0.8 \\times 7 = 5.6").to_edge(LEFT)
        calc_b = MathTex(r"b = 0.8 \\times 6 = 4.8").next_to(calc_a, DOWN)

        # Update triangle S with calculated side
        side_S_a = MathTex("5.6").move_to(triangle_S.get_center() + UP)
        side_S_b = MathTex("4.8").move_to(triangle_S.get_center() + LEFT)

        self.play(Write(calc_a), Transform(side_S_6_4, side_S_a))
        self.play(Write(calc_b), Transform(side_S_a, side_S_b))

        # Recap the solution
        recap = Text("Triangle sides calculated using similarity ratio.", font_size=24).next_to(triangle_S, RIGHT)
        self.play(Write(recap))
        self.wait(3)