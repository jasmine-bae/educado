from manim import *

class SimilarTriangles(Scene):
    def construct(self):
        # Define similar triangles R and S
        triangle_R = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.5, 0],
            color=BLUE,
            fill_opacity=0.3
        ).shift(LEFT*3)
        
        triangle_S = Polygon(
            [0, 0, 0], [2.4, 0, 0], [1.2, 2, 0],
            color=GREEN,
            fill_opacity=0.3
        ).shift(RIGHT*3)
        
        # Display triangles with labels
        labels_R = VGroup(
            MathTex("6").next_to(triangle_R, DOWN),
            MathTex("7").next_to(triangle_R, LEFT),
            MathTex("8").next_to(triangle_R.get_vertices()[1], UP)
        )
        
        labels_S = VGroup(
            MathTex("b").next_to(triangle_S, DOWN),
            MathTex("a").next_to(triangle_S, RIGHT),
            MathTex("6.4").next_to(triangle_S.get_vertices()[1], UP)
        )

        self.play(Create(triangle_R), Create(triangle_S))
        self.play(Write(labels_R), Write(labels_S))
        
        # Highlight corresponding angles with arcs
        angle_marks_R = VGroup(
            Arc(arc_center=triangle_R.get_vertices()[0], angle=PI/6).set_color(RED),
            Arc(arc_center=triangle_R.get_vertices()[2], angle=PI/4).set_color(YELLOW),
            Arc(arc_center=triangle_R.get_vertices()[1], angle=-PI/3).set_color(ORANGE)
        )
        
        angle_marks_S = VGroup(
            Arc(arc_center=triangle_S.get_vertices()[0], angle=PI/6).set_color(RED),
            Arc(arc_center=triangle_S.get_vertices()[2], angle=PI/4).set_color(YELLOW),
            Arc(arc_center=triangle_S.get_vertices()[1], angle=-PI/3).set_color(ORANGE)
        )
        
        self.play(Create(angle_marks_R), Create(angle_marks_S))
        
        # Calculate the unknown sides 'a' and 'b'
        ratio_equation = MathTex(
            "\\frac{6.4}{8} \\times 7 = 5.6",
        ).to_edge(UP)
        
        b_calculation = MathTex(
            "b = \\frac{6.4}{8} \\times 6 = 4.8",
        ).next_to(ratio_equation, DOWN)
        
        self.play(Write(ratio_equation))
        self.wait()
        
        # Solve for 'a'
        self.play(ReplacementTransform(labels_S[1].copy(), ratio_equation[0]), run_time=2)
        
        self.wait()

        # Solve for 'b'
        self.play(Write(b_calculation))
        self.wait()
        
        # Show the final lengths alongside the triangles
        solution_text = Text("Solved lengths: a = 5.6, b = 4.8").next_to(b_calculation, DOWN)
        self.play(Write(solution_text))
        
        self.wait(2)