#!/usr/bin/env python

import helpers 

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject

import mobject.vectorized_mobject

from animation.animation import Animation
import animation.transform 
import animation.simple_animations 
import animation.playground 

import mobject.svg_mobject 
import mobject.tex_mobject 

from scene import Scene
from camera import Camera

from constants import *
from crc.constants import *
#import topics
import crc
import topics.geometry
import random
import animation.simple_animations
import mobject.vectorized_mobject

## To watch one of these scenes, run the following:
## python extract_scenes.py -p file_name <SceneName>

def tt(s):
    return "\\texttt{" + s + "}\\blacksquare"
    #return "\\verb|" + s

code_string = """
for i in range(10):
    a = [i**2 for i in range(i)]
    print(a)
    if a == i:
        yield not a

"""

class Code(Scene):
    def construct(self):
        chars = max([len(l) for l in code_string.split("\n")])
        lines = [l for l in code_string.split("\n") if l.strip() != ""]


        print(chars)
        mobs = []
        max_l = 0
        for i, line in enumerate(lines):
            print(line)

            line = line.ljust(chars).replace(" ", "{ }")

            t = topics.characters.TextMobject(tt(line))
            if t.get_width() > max_l:
                max_l = t.get_width()
                largest_line = t.copy()

            mobs.append(t)

        for i, mob in enumerate(mobs):
            mob.scale_to_fit_width(largest_line.get_width())
            #mob.next_to(LEFT_SIDE, RIGHT)

            if i > 0: mob.next_to(mobs[i-1], DOWN)

            self.play(crc.animations.Type(mob, run_time=2))
            self.remove(mob.submobjects[-1])

        self.dither(2)


class Intro(Scene):
    def construct(self):
        name = topics.characters.TextMobject(tt("My name is Charlie"))\
            .scale_to_fit_width(SPACE_WIDTH*2-5)

        catch = topics.characters.TextMobject(tt("I'll try to explain..."))\
            .scale_to_fit_width(SPACE_WIDTH*2-5)

        [i.highlight(Colors.VS.TURQUOISE) for i in name.submobjects[8:8 + 7] + name.submobjects[0:2]]
        [i.highlight(Colors.Manim.Orange.ORANGE) for i in catch.submobjects[4:7]]
        [i.highlight(Colors.Manim.Orange.ORANGE) for i in name.submobjects[6:8]]

        name.shift((name.get_height() + catch.get_height()) / 3 * UP)
        catch.shift((name.get_height() + catch.get_height()) / 3 * DOWN)

        self.play(crc.animations.Type(name, run_time=1.5))
        self.dither(0.5)
        self.remove(name.submobjects[-1])
        self.play(crc.animations.Type(catch, run_time=2))
        self.dither(0.5)

        self.remove(name, catch)

        topic = topics.characters.TextMobject(tt("\"How the Internet Works\"")) \
            .scale_to_fit_width(SPACE_WIDTH*2-3)\
            .highlight(Colors.VS.GREEN)

        self.play(crc.animations.Type(topic, run_time=1.5))
        self.dither(2)


class Crowd(Scene):
    def construct(self):
        for i in range(100):
            x = random.uniform(RIGHT_SIDE[0], LEFT_SIDE[0])
            y = random.uniform(TOP[1], BOTTOM[1])

            person = crc.symbols.RandomPerson()\
                .scale(0.5)\
                .move_to(y*UP + x*RIGHT)

            self.play(crc.animations.Grow(person), run_time=0.1)

        self.dither()

class Blinks(Scene):
    def construct(self):
        eye = crc.symbols.Eyes(crc.Colors.Manim.Blue.A)
        eye2 = eye.copy()
        self.play(crc.animations.GrowVertical(eye), run_time=2)
        self.dither()
        self.play(crc.animations.ShrinkVertical(eye), run_time=0.2)
        self.remove(eye)
        self.play(crc.animations.GrowVertical(eye2), run_time=0.2)
        self.dither()

class Swipes(Scene):
    def construct(self):

        self.play(*(
            crc.animations.SwipeDown(
                crc.symbols.Machine()
                    .scale(0.5)\
                    .shift(2*LEFT + 2*UP)),

            crc.animations.SwipeUp(
                crc.symbols.SpeakerFront()
                    .scale(1.25)\
                    .shift(1*LEFT + 1*UP)),

            crc.animations.SwipeLeft(
                topics.geometry.Dot()
                    .highlight(crc.Colors.Manim.Green.D)\
                    .scale(0.75)\
                    .shift(-1*LEFT + -1*UP)),

            crc.animations.SwipeRight(
                topics.geometry.Cross()
                    .highlight(crc.Colors.Manim.Yellow.D)\
                    .scale(0.25)\
                    .shift(-2*LEFT + -2*UP)),

        ), run_time=4)

        self.dither()

