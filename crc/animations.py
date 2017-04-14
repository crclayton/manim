import numpy as np
import topics
import constants
import animation.transform
import crc.constants
import random
from pydub import AudioSegment

import numpy as np
import itertools as it
import inspect
import copy
import warnings
from scene import Scene

from helpers import *

from animation import Animation
from mobject import Mobject, Point, VMobject, Group
from topics.geometry import Dot
from animation.transform import Transform


class Type(Animation):


    def get_movie_file_path(self, name, extension):
        file_path = os.path.join(MOVIE_DIR, name)
        if not file_path.endswith(extension):
            file_path += extension
        directory = os.path.split(file_path)[0]
        if not os.path.exists(directory):
            os.makedirs(directory)
        return file_path

    def __init__(self, mobject, export_track=False, **kwargs):
        if "run_time" in kwargs:
            self.run_time = kwargs.pop("run_time")
        else:
            self.run_time = DEFAULT_ANIMATION_RUN_TIME

        self.fps = int(1 / LOW_QUALITY_FRAME_DURATION)

        mobject.set_fill(opacity=0)

        # determine typing delay times

        num_frames = self.run_time*self.fps+2

        self.box = mobject.submobjects[-1].copy()
        self.chars = len(mobject.submobjects)
        self.delays = self.make_delays(self.chars, num_frames)

        if export_track:
            self.export_track(mobject.get_tex_string())

        self.char_i = 0
        self.frame_i = 0


        Animation.__init__(self, mobject, run_time=self.run_time, **kwargs)

    def sanitize(self, filename):
        return "".join([c for c in filename if c.isalpha() or c.isdigit() or c == ' ']).rstrip()

    def get_key(self):
        sound_dir = "files/sounds/keys"

        # sound = {"folder":"typewriter",         "files":["key-new-01.wav", "key-new-02.wav", "key-new-03.wav", "key-new-04.wav", "key-new-05.wav"]}
        sound = {"folder": "mechanical", "files": ["1.wav", "2.wav", "3.wav", "4.wav", "5.wav"]}
        # sound = {"folder":"Cherry_G80_3494",    "files":["G80-3494.wav", "G80-3494_backspace.wav", "G80-3494_fast1.wav", "G80-3494_slow1.wav", "G80-3494_space.wav"]}

        return sound_dir + "/" + sound.get("folder") + "/" + random.choice(sound.get("files"))

    def make_delays(self, n, total, mean=10, dev=6):
        ds = [np.random.normal(mean, dev) for _ in range(n)]
        return [i / sum(ds) * total for i in ds]

    def export_track(self, title):
        track = AudioSegment.silent(duration=10 * 1000)

        for i, _ in enumerate(self.delays):
            pos = sum(self.delays[0:i]) * 1000 * int(1/self.fps)
            track = track.overlay(AudioSegment.from_wav(self.get_key()), position=pos)

        track = track[0:self.chars * 1000 * int(1/self.fps)]

        file = self.get_movie_file_path(self.sanitize(title), ".wav")
        track.export(file, format="wav")

    def update_mobject(self, alpha):
        if self.frame_i > sum(self.delays[:self.char_i]) and self.char_i < self.chars - 1:

            next_char = self.mobject.submobjects[self.char_i + 1]

            self.mobject.submobjects[self.char_i] \
                .set_fill(opacity=1)

            self.mobject.submobjects[-1]\
                .set_fill(WHITE, opacity=1) \
                .move_to(next_char.get_right()*RIGHT + self.box.get_width()/6*RIGHT
                         + self.box.get_center()[1] * UP)

            self.char_i += 1

        self.frame_i += 1



class Grow(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            self.starting_mobject.shift(target.get_height()/2*DOWN)
            self.starting_mobject.stretch_to_fit_height(0)

class GrowVertical(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            self.starting_mobject.stretch_to_fit_height(0)

class ShrinkVertical(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        target.stretch_to_fit_height(0)
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            #self.starting_mobject.stretch_to_fit_height(self)
            pass

class GrowHorizontal(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            self.starting_mobject.stretch_to_fit_width(0)

class SwipeDown(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            start = self.starting_mobject.copy()
            self.starting_mobject.move_to(ORIGIN)
            self.starting_mobject.shift(start.get_height()/2*UP + TOP + start.get_center()[0]*RIGHT)

class SwipeUp(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            start = self.starting_mobject.copy()
            self.starting_mobject.move_to(ORIGIN)
            self.starting_mobject.shift(start.get_height()/2*DOWN + BOTTOM + start.get_center()[0]*RIGHT)

class SwipeRight(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            start = self.starting_mobject.copy()
            self.starting_mobject.move_to(ORIGIN)
            self.starting_mobject.shift(start.get_height()/2*LEFT + LEFT_SIDE + start.get_center()[0]*DOWN)

class SwipeLeft(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        Transform.__init__(self, mobject, target, **kwargs)
        if isinstance(self.starting_mobject, VMobject):
            start = self.starting_mobject.copy()
            self.starting_mobject.move_to(ORIGIN)
            self.starting_mobject.shift(start.get_height() / 2 * RIGHT + RIGHT_SIDE + start.get_center()[0] * DOWN)