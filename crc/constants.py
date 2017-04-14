import numpy as np
import random
import random
import inspect
from constants import *

DEGREES = np.pi/180

class Colors():
    class Manim():
        class Blue():
            DARK   = "#236B8E"
            E      = "#1C758A"
            D      = "#29ABCA"
            C      = "#58C4DD"
            B      = "#9CDCEB"
            A      = "#C7E9F1"

        class Teal():
            E      = "#49A88F"
            D      = "#55C1A7"
            C      = "#5CD0B3"
            B      = "#76DDC0"
            A      = "#ACEAD7"

        class Green():
            E     = "#699C52"
            D     = "#77B05D"
            C     = "#83C167"
            B     = "#A6CF8C"
            A     = "#C9E2AE"

        class Yellow():
            E    = "#E8C11C"
            D    = "#F4D345"
            C    = "#FFFF00"
            B    = "#FFEA94"
            A    = "#FFF1B6"

        class Gold():
            E      = "#C78D46"
            D      = "#E1A158"
            C      = "#F0AC5F"
            B      = "#F9B775"
            A      = "#F7C797"

        class Red():
            E       = "#CF5044"
            D       = "#E65A4C"
            C       = "#FC6255"
            B       = "#FF8080"
            A       = "#F7A1A3"

        class Maroon():
            E    = "#94424F"
            D    = "#A24D61"
            C    = "#C55F73"
            B    = "#EC92AB"
            A    = "#ECABC1"

        class Purple():
            E    = "#644172"
            D    = "#715582"
            C    = "#9A72AC"
            B    = "#B189C6"
            A    = "#CAA3E8"

        class Grey():
            LIGHT  = "#BBBBBB"
            NORMAL = "#888888"
            DARK   = "#444444"

        class Brown():
            @property
            def __init__(self):
                return self.PINK

            DARK  = "#8B4513"
            LIGHT = "#CD853F"
            GREY  = "#736357"

        class Orange():
            @property
            def __init__(self):
                return self.ORANGE

            ORANGE = "#FF862F"

        class Pink():
            def __init__(self):
                return self.PINK

            PINK = "#D147BD"

        White  = "#FFFFFF"
        Black  = "#000000"
        SCREEN = "#00FF00"


    class VS():
        BACKGROUND = "#101010"
        TURQUOISE = "#4EC9B0"
        GRAY = "#9B9B9B"
        RED = "#ff3333"
        PINK = "#B90690"
        VIOLET = "#C586C0"
        WHITE = "#DCDCDC"
        GREEN = "#608B4E"
        LIME = "#B5CEA8"
        BEIGE = "#E3BBAB"
        ORANGE = "#D69D85"
        BLUE = "#569CD6"
        YELLOW = "#DCDCAA"
        YELLOW_LIGHT = "#D7BA7D"
        BLUE_LIGHT = "#9CDCFE"

    @property
    @staticmethod
    def random():

        colors = []
        for a in inspect.getmembers(Colors.Manim):
            if inspect.isclass(a[1]):
                colors += [c[1] for c in inspect.getmembers(a[1])
                          if type(c[1]) is str and c[1].startswith("#")]

        return random.choice(colors)
