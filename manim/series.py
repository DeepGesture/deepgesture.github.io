from manim import *

class Windind(Scene):
    def construct(self):
        value = ValueTracker(0.0)

        def func(f=0.1, step=0.001):
            out = lambda t: 0.5 * (2 + 1 * np.cos(TAU * t * 3) + 1 * np.cos(TAU * t * 2)) * np.exp(-TAU * 1j * t * f)
            dt = step
            ran = np.arange(0, 6, dt)
            Int = sum([out(i) * dt for i in ran])
            return (1 / 6) * np.array([Int.real, Int.imag, 0])

        def complex_to_real(f):
            z = lambda t: 0.5 * (2 + 1 * np.cos(TAU * t * 3) + 1 * np.cos(TAU * t * 2)) * np.exp(-TAU * 1j * t * f)
            return lambda t: np.array([z(t).real, z(t).imag, 0])

        # Create curve and dot
        curve = always_redraw(lambda: ParametricFunction(complex_to_real(value.get_value()), t_range=[0, 6, 0.01], color=YELLOW))
        dot = always_redraw(lambda: Dot(func(f=value.get_value()), color=RED))

        # Create axes and graphs
        axes = Axes(x_range=[0, 5, 1], y_range=[-1, 1, 1], x_length=4, y_length=3).shift(4.5 * LEFT + 2 * UP)
        axes1 = Axes(x_range=[0, 5, 1], y_range=[0, 2, 1], x_length=4, y_length=1.5).shift(4.5 * RIGHT + 3 * UP)
        graph = axes1.plot(lambda t: 1 + np.cos(TAU * t * 3), color=BLUE)
        axes2 = Axes(x_range=[0, 5, 1], y_range=[0, 2, 1], x_length=4, y_length=1.5).next_to(axes1, DOWN, aligned_edge=LEFT, buff=0.5)
        graph2 = axes2.plot(lambda t: 1 + np.cos(TAU * t * 2), color=YELLOW)
        axes3 = Axes(x_range=[0, 5, 1], y_range=[0, 2, 1], x_length=4, y_length=1.5).next_to(axes2, DOWN, aligned_edge=LEFT, buff=2)
        graph3 = axes3.plot(lambda t: 2 + np.cos(TAU * t * 2) + np.cos(TAU * t * 3), color=PINK)

        # Add labels
        tex1 = VGroup(
            Tex("2 beat/per second").scale(0.5).next_to(graph, LEFT),
            Tex("3 beat/per second").scale(0.5).next_to(graph2, UP),
            Tex("mix").scale(0.5).next_to(graph3, UP)
        )
        freq = Tex("Frequency").next_to(axes.x_axis, DOWN, aligned_edge=RIGHT)
        yl = Text("x coordinate of center of mass").scale(0.5).next_to(axes.y_axis, RIGHT, aligned_edge=UP)

        # Create dot path tracking
        dot1 = always_redraw(lambda: Dot(axes.c2p(value.get_value(), dot.get_center()[0])))
        path = VMobject(color=RED)
        path.set_points_as_corners([dot1.get_center(), dot1.get_center()])

        def path_update(mob):
            previous_path = mob.copy()
            previous_path.add_points_as_corners([dot1.get_center()])
            mob.become(previous_path)

        path.add_updater(path_update)

        # Create complex plane
        plane = ComplexPlane(x_range=[-2, 2, 1], y_range=[-2, 2, 1])

        # Add all elements to the scene
        self.add(plane, freq, yl, curve, dot, axes, dot1, path, axes1, graph, graph2, axes2, axes3, graph3, tex1)

        # Animate the value changes
        self.play(value.animate.set_value(2), run_time=12, rate_func=linear)
        self.wait()
        self.play(value.animate.set_value(3), run_time=6, rate_func=linear)
        self.wait()
        self.play(value.animate.set_value(5), run_time=12, rate_func=linear)
        self.wait()


class FWindind(Scene):
    def construct(self):

        def four(t):
            if t < -0.5 or t > 0.5:
                return 0
            else:
                return 1

        # Create axes and lines
        axes = Axes(x_range=[-5, 5, 1], y_range=[-2, 2, 1], height=3, width=8).shift(2 * DOWN)
        axes1 = Axes(x_range=[-5, 5, 1], y_range=[-2, 2, 1], height=3, width=8).next_to(axes, UP)
        line1 = Line(axes1.c2p(-0.5, 0), axes1.c2p(-0.5, 1))
        line2 = Line(axes1.c2p(0.5, 0), axes1.c2p(0.5, 1))
        line3 = Line(axes1.c2p(-0.5, 1), axes1.c2p(0.5, 1))

        tex = Tex(r"f(\omega)=\int_{-\infty}^{\infty}g(t)e^{-2\pi i \omega t}dt").shift(4 * LEFT)
        square = VGroup(line1, line2, line3).set_color(YELLOW)
        arr = CurvedArrow(axes1.c2p(0, 0), tex.get_center() + UP * 0.8, color=YELLOW)
        arr1 = CurvedArrow(tex.get_center() + 5.5 * RIGHT * 0.5, axes.get_center() + UP, angle=-TAU / 4, color=BLUE)

        # Define the integral function for plotting
        def integral(f, step=0.001):
            dt = step
            sample = np.arange(-6, 6, dt)
            z = sum([four(t) * np.exp(-TAU * 1j * t * f) * dt for t in sample])
            return z.real + z.imag

        curve = axes.plot(lambda t: integral(t), color=BLUE)

        # Add elements to the scene
        self.play(AnimationGroup(*[
            Create(mob) for mob in [axes1, square, arr, tex, arr1, axes, curve]
        ], lag_ratio=1))
