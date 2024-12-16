from manim import *

class SimilarTriangles(Scene):
    def construct(self):
        # Create grid
        grid = NumberPlane()
        self.add(grid)

        # Setup Triangle R
        points_R = [
            2 * LEFT + 1 * UP,   # A
            3 * RIGHT + 1 * UP,  # B
            3 * RIGHT + 2 * DOWN  # C
        ]
        triangle_R = Polygon(*points_R, color=BLUE)
        label_R_A = Tex("A").next_to(points_R[0], LEFT)
        label_R_B = Tex("B").next_to(points_R[1], UP)
        label_R_C = Tex("C").next_to(points_R[2], DOWN)
        side_lengths_R = [
            Tex("6").next_to(midpoint(points_R[0], points_R[1]), DOWN),
            Tex("7").next_to(midpoint(points_R[1], points_R[2]), RIGHT),
            Tex("8").next_to(midpoint(points_R[0], points_R[2]), UP)
        ]

        # Draw Triangle R
        self.play(Create(triangle_R))
        self.play(FadeIn(label_R_A, label_R_B, label_R_C))
        for side_length in side_lengths_R:
            self.play(FadeIn(side_length))

        # Setup Triangle S - initially as a silhouette
        points_S = [
            6 * LEFT + 2 * UP,   # D
            7 * LEFT + 2 * DOWN, # E
            6 * LEFT + 3 * UP   # F
        ]
        triangle_S = Polygon(*points_S, color=ORANGE, fill_opacity=0.2)
        dash_triangle_S = Triangle(fill_opacity=0, color=ORANGE)  # dashed outline

        # Create dashed outline (invisible until needed)
        self.add(dash_triangle_S)
        self.play(ShowCreationByParts(triangle_S, run_time=2))
        
        # Transition to Triangle S's outline
        self.play(ShowCreation(dash_triangle_S), run_time=1.5 - 0.5)

        # Angle markings
        angle_mark_A = Arc(radius=0.3, arc_center=points_R[0], start_angle=PI / 4, angle=PI / 2)
        angle_mark_D = Arc(radius=0.3, arc_center=points_S[0], start_angle=PI / 4, angle=PI / 2)
        angle_mark_B = Arc(radius=0.3, arc_center=points_R[1], start_angle=3 * PI / 4, angle=PI / 2)
        angle_mark_E = Arc(radius=0.3, arc_center=points_S[1], start_angle=3 * PI / 4, angle=PI / 2)
        angle_mark_C = Arc(radius=0.3, arc_center=points_R[2], start_angle=0, angle=PI / 2)
        angle_mark_F = Arc(radius=0.3, arc_center=points_S[2], start_angle=0, angle=PI / 2)

        # Display angle markings
        self.play(GrowArrow(angle_mark_A), GrowArrow(angle_mark_D))
        self.play(GrowArrow(angle_mark_B), GrowArrow(angle_mark_E))
        self.play(GrowArrow(angle_mark_C), GrowArrow(angle_mark_F))

        # Text hint
        hint_surface = Text("Corresponding Angles are Equal").to_edge(UP)
        self.play(Write(hint_surface))
        self.wait(1)
        self.play(FadeOut(hint_surface))

        # Visualizing corresponding sides
        ratio_text = Text("Ratio = \\frac{6.4}{8}").to_edge(DOWN)
        side_line = Line(start=points_S[1], end=points_R[2], color=YELLOW)
        self.play(Create(side_line))
        
        self.play(Write(ratio_text))
        
        # Showing calculation animation
        self.play(Indicate(side_line))
        self.wait(1)  # pause for a moment

        # Show the step-by-step calculation
        anim_ratio = [r"$6.4$", r"$=$", r"$\frac{6.4}{8}$"]
        frac = Fraction(6.4, 8)
        fraction_result = Tex(str(frac)).next_to(ratio_text, RIGHT)
        
        self.play(Write(ratio_text), FadeOut(side_line), run_time=1)        
        self.play(Write(fraction_result), run_time=0.5)
        self.wait(2)
        
        # Now calculate 'a'
        calc_a = Tex("a = \\frac{6.4}{8} \\times 7").to_edge(DOWN)
        self.play(Write(calc_a))
        a_value = Tex("a = 5.6").next_to(calc_a, DOWN)
        self.play(Write(a_value))
        self.wait(1)

        # Next calculate 'b'
        self.play(FadeOut(calc_a), FadeOut(a_value))
        calc_b = Tex("b = \\frac{6.4}{8} \\times 6").to_edge(DOWN)
        self.play(Write(calc_b))
        b_value = Tex("b = 4.8").next_to(calc_b, DOWN)
        self.play(Write(b_value))
        self.wait(2)

        # Final Visualization
        self.play(FadeOut(calc_b), FadeOut(b_value))
        final_triangle_S = Polygon(*points_S, color=ORANGE, fill_opacity=1)
        self.play(Transform(triangle_S, final_triangle_S))
        
        final_text = Text("Triangles R and S are Similar!").to_edge(UP)
        final_ratio = Text("Corresponding Sides are in Proportion.").next_to(final_text, DOWN)
        self.play(FadeIn(final_text), FadeIn(final_ratio))
        self.wait(3)

        # Fade out both triangles
        self.play(FadeOut(triangle_R), FadeOut(triangle_S), FadeOut(final_text), FadeOut(final_ratio))
        self.wait(1)