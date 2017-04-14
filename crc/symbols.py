from helpers import *
from mobject import Mobject, Mobject1D
from mobject.vectorized_mobject import VMobject
from topics.geometry import *
from topics.characters import  *
import numpy
from constants import *

class Client(VMobject):
    def generate_points(self):
        r1 = Rectangle()\
            .stretch_to_fit_width(3)\
            .stretch_to_fit_height(2)\
            .highlight(Blue)\
            .shift(5*LEFT)

        r2 = Rectangle()\
            .stretch_to_fit_width(1)\
            .stretch_to_fit_height(0.2)\
            .highlight(WHITE)\
            .next_to(r1, DOWN*2.5)\

        self.add(r1, r2)
        self.init_colors()

class Router(VMobject):
    def generate_points(self):
        c = Circle()\
            .scale(0.8)

        x = Cross()

        self.add(c, x)
        self.init_colors()

class Network(VMobject):
    def generate_points(self):
        r1 = Router()\
            .scale(0.5)\
            .shift(1*RIGHT)

        r2 = Router()\
            .scale(0.5)\
            .shift(0.9*DOWN, 0.5*RIGHT  + 1*RIGHT)

        r3 = Router()\
            .scale(0.5)\
            .shift(0.9*DOWN, 0.5*LEFT + 1*RIGHT)

        self.add(r1, r2, r3)
        self.init_colors()


class Engineer(VMobject):
    def generate_points(self):
        p1 = Person()
        p1.highlight(RED_C).set_fill(RED_C)

        helmet = SemiCircle() \
            .set_fill(YELLOW).highlight(YELLOW) \
            .scale_to_fit_width(p1.get_width()) \
            .next_to(p1, UP) \
            .shift(0.4 * DOWN)

        self.add(p1, helmet)
        self.init_colors()

class SemiCircle(VMobject):
    def generate_points(self):
        nudge = 0.05
        w_angle =  -1*degrees
        v_angle = 181*degrees

        arc = Arc(
            (1-2*nudge)*(w_angle - v_angle),
            start_angle = interpolate(v_angle, w_angle, nudge),
            radius = 2.5
        )

        line = Line(LEFT, RIGHT)\
            .next_to(arc, DOWN)\
            .stretch_to_fit_width(arc.get_width())

        self.add(arc, line)
        self.init_colors()


class Family(VMobject):
    def generate_points(self):
        c1 = Colors.Manim.random
        c2 = Colors.Manim.random
        c3 = Colors.Manim.random

        l = Person() \
            .set_fill(c2) \
            .highlight(c2) \
            .shift(1 * LEFT)

        m = Person() \
            .set_fill(c1) \
            .highlight(c1) \
            .shift(1 * RIGHT)

        j = Person() \
            .scale(0.5) \
            .set_fill(c3) \
            .highlight(c3) \
            .shift(2 * DOWN)

        self.add(l,m,j)
        self.init_colors()


class Server(VMobject):
    def generate_points(self):
        l1 = Line(RIGHT, UP)\
            .highlight(GREEN)

        l2 = Line(RIGHT, UP) \
            .next_to(l1, DOWN * 10) \
            .highlight(GREEN)

        l3 = Line(UP, DOWN) \
            .next_to(l1, DOWN) \
            .shift(LEFT * 0.5, 1.1 * UP) \
            .stretch_to_fit_height(2) \
            .highlight(GREEN)

        l4 = Line(UP, DOWN) \
            .next_to(l3, RIGHT) \
            .shift(1 * DOWN, RIGHT * 0.9) \
            .stretch_to_fit_height(2) \
            .highlight(GREEN)


        l5 = Line(LEFT, UP) \
            .next_to(l1) \
            .stretch_to_fit_height(2) \
            .stretch_to_fit_width(2) \
            .shift(RIGHT * 0.4, UP * 0.5)

        l6 = Line(LEFT, UP) \
            .next_to(l1) \
            .stretch_to_fit_height(2) \
            .stretch_to_fit_width(2) \
            .shift(RIGHT * 0.4, DOWN * 1.5)

        l7 = Line(UP, DOWN) \
            .next_to(l1, DOWN) \
            .shift(2.5 * RIGHT, 2.1 * UP) \
            .stretch_to_fit_height(2)

        l8 = Line(LEFT, UP) \
            .next_to(l1) \
            .stretch_to_fit_height(2) \
            .stretch_to_fit_width(2) \
            .shift(UP * 1.5, LEFT * 0.6)

        l9 = Line(RIGHT, UP) \
            .next_to(l1) \
            .shift(.9 * RIGHT, 2 * UP)

        self.add(l1, l2, l3, l4, l5, l6, l7, l8, l9)
        self.init_colors()

class Capacitor(VMobject):
    def generate_points(self):
        l1 = Line(RIGHT, LEFT)

        l2 = Line(UP, DOWN)\
            .next_to(l1)\
            .shift(0.1*LEFT)

        l3 = Line(UP, DOWN)\
            .next_to(l2)\
            .shift(0.5*RIGHT)

        l4 = Line(RIGHT, LEFT)\
            .next_to(l3) \
            .shift(0.1*LEFT)

        self.add(l1, l2, l3, l4)
        self.init_colors()



class App(VMobject):
    def generate_points(self):
        s1 = Square()\
            .highlight(WHITE)\
            .shift(0*LEFT)

        s2 = Square()\
            .highlight(YELLOW)\
            .shift(0.3*RIGHT, 0.3*DOWN)

        self.add(s1, s2)
        self.init_colors()



class Wifi(VMobject):
    def generate_points(self):
        nudge = 0.05
        w_angle =   3.14/3
        v_angle = 2*3.14/3
        arc1 = Arc(
            (1-2*nudge)*(w_angle - v_angle),
            start_angle = interpolate(v_angle, w_angle, nudge),
            radius = 2.5
        ).highlight(GREEN)\
         .shift(1*RIGHT)
        arc2 = Arc(
            (1-2*nudge)*(w_angle - v_angle),
            start_angle = interpolate(v_angle, w_angle, nudge),
            radius = 2
        ).shift(1*RIGHT)
        arc3 = Arc(
            (1-2*nudge)*(w_angle - v_angle),
            start_angle = interpolate(v_angle, w_angle, nudge),
            radius = 1.5
        ).shift(1*RIGHT )

        self.add(arc1, arc2, arc3)
        self.init_colors()


class NestedCircle(VMobject):
    def generate_points(self):
        c1 = Circle()
        c2 = Circle()\
            .scale(0.8)

        self.add(c1, c2)
        self.init_colors()


class SpeakerFront(VMobject):
    def generate_points(self):
        speaker = SVGMobject(file_name="speakerfront") \
            .scale(0.005) \
            .highlight(Colors.Manim.Yellow.E) \
            .stretch_to_fit_height(Square().get_height()) \
            .stretch_to_fit_width(Square().get_width())

        self.add(speaker)
        self.init_colors()

class CircleArray(VMobject):
    def generate_points(self):
        circle = []
        for i in range(8):
            circle.append(SpeakerFront())
            circle[i].scale(0.5)

        for i in range(len(circle)):
            circle[i].highlight(Colors.Manim.Yellow.E)
            if i > 0: circle[i].next_to(circle[i-1], 0.1*LEFT)

        for c in circle:
            c.shift(RIGHT*3.6)

        for i in range(len(circle)):
            self.add(circle[i])

        self.init_colors()

class SquareArray(VMobject):
    def generate_points(self):
        circle = []
        for i in range(8):
            circle.append(Square())
            circle[i].scale(0.5)

        for i in range(len(circle)):
            circle[i].highlight(Colors.Manim.Yellow.E)

            if i > 0: circle[i].next_to(circle[i-1], 0.25*LEFT)

        for c in circle:
            c.shift(RIGHT*3.6)

        for i in range(len(circle)):
            self.add(circle[i])


        self.init_colors()


class SpeakerArray(VMobject):
    def generate_points(self):
        circle = []
        for i in range(8):
            c = Square()\
                .scale(0.5)

            speaker = Speaker()
            speaker.rotate(-90*degrees)
            speaker.scale_to_fit_width(c.get_width()*2)

            circle.append(speaker)
            circle[i].scale(0.5)

        for i in range(len(circle)):
            circle[i].highlight(Colors.Manim.Yellow.E)

            if i > 0: circle[i].next_to(circle[i-1], 0.25*LEFT)

        for c in circle:
            c.shift(RIGHT*3.6)

        for i in range(len(circle)):
            self.add(circle[i])


        self.init_colors()


class SpeakerArraySmall(VMobject):
    def generate_points(self):
        circle = []
        for i in range(8):
            c = Square()\
                .scale(0.5)

            speaker = Speaker()
            speaker.rotate(180*degrees)
            speaker.scale_to_fit_width(c.get_width()*2)

            circle.append(speaker)
            circle[i].scale(0.5)

        for i in range(len(circle)):
            circle[i].highlight(Colors.Manim.Yellow.E)

            if i > 0: circle[i].next_to(circle[i-1], 0.25*LEFT)

        for c in circle:
            c.shift(RIGHT*3.6)
            c.scale(0.5)

        for i in range(len(circle)):
            self.add(circle[i])


        self.init_colors()


class Camera(VMobject):
    def generate_points(self):
        cam = SVGMobject(file_name="camera4.svg")
        cam.scale(0.005)
        self.add(cam)
        self.init_colors()



class Atlus(VMobject):
    def generate_points(self):
        atlus = CircleArray()

        #rect = Rectangle() \
        #    .stretch_to_fit_width(atlus.get_width()+0.5) \
        #    .stretch_to_fit_height(atlus.get_height()+0.5) \
        #    .highlight(VS_COLORS.GRAY)

        self.add(atlus)#, rect)

        self.init_colors()


class Eyes(VMobject):
    def generate_points(self, color=Colors.Manim.Blue.D):
        eye1 = Eye(color).scale(0.5).shift(1.8*LEFT)
        eye2 = Eye(color).scale(0.5).shift(1.8*RIGHT)
        self.add(eye1, eye2)
        self.init_colors()

class Eye(VMobject):
    def generate_points(self, color=Colors.Manim.Blue.D):
        eye = SVGMobject(file_name="eye")
        eye.scale(0.002)
        [i.highlight(color) for i in eye.submobjects[2:10]]
        eye.submobjects[10].highlight(COLORS.WHITE).set_fill(COLORS.WHITE)
        self.add(eye)
        self.init_colors()


class GenericPerson(VMobject):
    def generate_points(self):
        person = SVGMobject(file_name="person")
        person.scale(0.01)
        self.add(person)
        self.init_colors()

class RandomPerson(VMobject):
    def generate_points(self):
        person = SVGMobject(file_name="person")
        person.scale(0.01)
        color = COLORS.RANDOM()
        person.highlight(color)
        person.set_fill(color)
        self.add(person)
        self.init_colors()

class Machine(VMobject):
    def generate_points(self):
        m = SVGMobject(file_name="machine")
        m.scale(0.01)

        [i.highlight(Colors.Manim.GREY.DARK) for i in m.submobjects[0]]
        [i.highlight(Colors.Manim.GREY.NORMAL) for i in m.submobjects[1:2]]
        [i.highlight(Colors.Manim.GREY.LIGHT) for i in m.submobjects[2:5]]
        [i.highlight(Colors.Manim.RED.E) for i in m.submobjects[6]]
        [i.set_fill(Colors.Manim.RED.A) for i in m.submobjects[6]]


        self.add(m)
        self.init_colors()


class LongSine(Mobject1D):
    def generate_points(self):
        self.add_points(
            [(x, numpy.sin(360*degrees*x), 0) for x in np.arange(0, 5, 0.0001)])

        self.init_colors()


class Speaker(VMobject):
    def generate_points(self):
        speaker = SVGMobject(file_name="speaker")\
            .scale(0.005)\
            .highlight(Colors.Manim.Yellow.E)\
            .stretch_to_fit_height(Square().get_height())\
            .stretch_to_fit_width(Square().get_width()/2)

        semi = SemiCircle()\
            .highlight(Colors.Manim.Yellow.E)\
            .rotate(-90*degrees)\
            .scale(0.15)

        semi.shift(speaker.get_left())

        semi.shift(0.035*LEFT)

        self.add(speaker, semi)
        self.init_colors()

class Filter(VMobject):
    def generate_points(self):
        f = Square() \
            .highlight(VS_COLORS.TURQUOISE) \
            .scale(0.5) \
            .rotate(45*degrees)

        l = DashedLine(UP, DOWN)\
            .highlight(WHITE)\
            .stretch_to_fit_height(f.get_height())

        l.scale(0.8)
        l.shift(0.08*DOWN)

        self.add(f, l)
        self.init_colors()