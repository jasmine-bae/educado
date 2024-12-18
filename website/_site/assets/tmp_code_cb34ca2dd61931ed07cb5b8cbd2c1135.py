from manim import Scene, MathTex, VGroup, Arc, Line, Create, Write, Transform, FadeOut, Circumscribe

class SimilarTriangles(Scene):
    def construct(self):
        # Create and position triangles R and S
        triangle_R = VGroup(
            Line([-1, 1, 0], [1, 1, 0]), 
            Line([1, 1, 0], [0, -1, 0]), 
            Line([0, -1, 0], [-1, 1, 0])
        ).scale(0.9).shift([-2, 0, 0])

        triangle_S = VGroup(
            Line([-0.8, 0.8, 0], [0.8, 0.8, 0]), 
            Line([0.8, 0.8, 0], [0, -0.8, 0]), 
            Line([0, -0.8, 0], [-0.8, 0.8, 0])
        ).scale(0.9).shift([2, 0, 0])

        # Create arcs for angles in both triangles
        arcs_R = VGroup(
            Arc(radius=0.3, start_angle=0, angle=PI/3).shift([-1, 1, 0]),
            Arc(radius=0.3, start_angle=PI, angle=PI/3).shift([1, 1, 0]),
            Arc(radius=0.3, start_angle=3*PI/2, angle=PI/3).shift([0, -1, 0])
        )

        arcs_S = VGroup(
            Arc(radius=0.24, start_angle=0, angle=PI/3).shift([-0.8, 0.8, 0]),
            Arc(radius=0.24, start_angle=PI, angle=PI/3).shift([0.8, 0.8, 0]),
            Arc(radius=0.24, start_angle=3*PI/2, angle=PI/3).shift([0, -0.8, 0])
        )

        # Corresponding lengths and labels
        labels_R = VGroup(
            MathTex("6").next_to(triangle_R.get_bottom(), LEFT, buff=0.1),
            MathTex("7").next_to(triangle_R.get_top(), UP, buff=0.1),
            MathTex("8").next_to(triangle_R.get_right(), RIGHT, buff=0.1)
        ).scale(0.7)
        
        known_S = MathTex("6.4").next_to(triangle_S.get_right(), RIGHT, buff=0.1).scale(0.7)
        unknown_S = VGroup(
            MathTex("a").next_to(triangle_S.get_top(), UP, buff=0.1),
            MathTex("b").next_to(triangle_S.get_left(), LEFT, buff=0.1)
        ).scale(0.7)

        # Show triangles with arcs and labels
        self.play(Create(triangle_R), Create(triangle_S))
        self.play(Create(arcs_R), Create(arcs_S))
        self.play(Write(labels_R))
        self.play(Write(known_S), Write(unknown_S))
        self.wait(1)

        # Show calculation steps using transformations
        ratio_text = MathTex(r"\text{Ratio} = \frac{6.4}{8}").shift(UP * 1.5).scale(0.7)
        self.play(Write(ratio_text))
        self.wait(1)

        # Calculation for 'a'
        calculation_a = MathTex(r"a = \frac{6.4}{8} \times 7 = 5.6").shift(DOWN * 1.5).scale(0.7)
        self.play(Transform(unknown_S[0], calculation_a))
        self.wait(1)

        # Calculation for 'b'
        calculation_b = MathTex(r"b = \frac{6.4}{8} \times 6 = 4.8").shift(DOWN * 2).scale(0.7)
        self.play(Transform(unknown_S[1], calculation_b))
        self.wait(1)

        # Fade out unnecessary calculations and display final result
        self.play(FadeOut(calculation_a), FadeOut(calculation_b), FadeOut(ratio_text))
        final_labels = VGroup(
            MathTex("a = 5.6").next_to(triangle_S.get_top(), UP, buff=0.1),
            MathTex("b = 4.8").next_to(triangle_S.get_left(), LEFT, buff=0.1)
        ).scale(0.7)
        self.play(Transform(unknown_S, final_labels))
        self.play(Circumscribe(triangle_S))
        self.wait(1)