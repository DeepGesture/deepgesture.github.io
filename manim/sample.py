from manim import *

class DrawCircle(Scene):
    def construct(self):
        # Create a circle object
        circle = Circle(radius=2, color=BLUE)

        # Animate the drawing of the circle
        self.play(Create(circle))

        # Keep the circle on screen for a while
        self.wait(2)

        # Add a transformation of the circle (scaling it)
        self.play(circle.animate.scale(0.5))

        # Fade out the circle
        self.play(FadeOut(circle))
