from manim import *

class SimilarTriangles(Scene):
    def construct(self):
        # Define triangles R and S
        triangle_R = Polygon(
            np.array([0, 0, 0]),
            np.array([3, 0, 0]),
            np.array([2.5, 2, 0]),
            color=BLUE
        )
        triangle_S = Polygon(
            np.array([0, 0, 0]),
            np.array([2.4, 0, 0]),
            np.array([2, 1.6, 0]),
            color=GREEN
        ).shift(RIGHT * 4)

        # Add similarity symbol
        similarity_symbol = MathTex(r"\sim").shift(RIGHT * 3)

        # Annotating angles
        arcs_R = [
            ArcBetweenPoints(triangle_R.get_vertices()[1], triangle_R.get_vertices()[0], angle=-PI/8).set_color(RED),
            ArcBetweenPoints(triangle_R.get_vertices()[0], triangle_R.get_vertices()[2], angle=PI/8).set_color(YELLOW),
            ArcBetweenPoints(triangle_R.get_vertices()[2], triangle_R.get_vertices()[1], angle=PI/12).set_color(ORANGE),
        ]
        arcs_S = [
            ArcBetweenPoints(triangle_S.get_vertices()[1], triangle_S.get_vertices()[0], angle=-PI/8).set_color(RED),
            ArcBetweenPoints(triangle_S.get_vertices()[0], triangle_S.get_vertices()[2], angle=PI/8).set_color(YELLOW),
            ArcBetweenPoints(triangle_S.get_vertices()[2], triangle_S.get_vertices()[1], angle=PI/12).set_color(ORANGE),
        ]

        # Displaying corresponding sides
        side_labels_R = [
            MathTex("6").move_to(triangle_R.get_center() + [0.5, -0.3, 0]),
            MathTex("7").move_to(triangle_R.get_center() + [1.5, 0.1, 0]),
            MathTex("8").move_to(triangle_R.get_center() + [1.0, 1.2, 0]),
        ]
        side_labels_S = [
            MathTex("b").move_to(triangle_S.get_center() + [0.4, -0.25, 0]),
            MathTex("a").move_to(triangle_S.get_center() + [1.0, 0.05, 0]),
            MathTex("6.4").move_to(triangle_S.get_center() + [0.8, 0.9, 0]),
        ]

        # Animating the similarities and calculations
        self.play(Create(triangle_R), Create(triangle_S), Write(similarity_symbol))
        self.play(*[Create(arc) for arc in arcs_R], *[Create(arc) for arc in arcs_S])
        self.play(*[Write(label) for label in side_labels_R], *[Write(label) for label in side_labels_S])

        # Explanation for side ratios
        explanation_text = MathTex(
            r"\text{Ratio of sides: } \frac{6.4}{8}",
            r"a = \frac{6.4}{8} \times 7 = 5.6",
            r"b = \frac{6.4}{8} \times 6 = 4.8"
        ).arrange(DOWN).to_edge(LEFT)

        for i, text in enumerate(explanation_text):
            self.play(Write(text))
            self.wait(1)