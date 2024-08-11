"""
Copyright (C) 2022 Excilious

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame
import sys
import math
from numba import jit

RESOLUTION = WIDTH,HEIGHT = 1000,500
FRAMESPERSECOND = 120

PLAYERPOSITION = 1.5,5
PLAYERANGLE = 0
PLAYERSPEED = 0.009
PLAYERROTATIONSPEED = 0.009
PLAYERMAXSIZE = 60

FIELDOFVIEW = math.pi / 3.5
NUMBEROFRAYS = WIDTH // 2
DELTAANGLE = FIELDOFVIEW / NUMBEROFRAYS
MAXDEPTH = 20

DISTANCE3D = (WIDTH / 2) / math.tan((FIELDOFVIEW/2))
SCREENSCALE = WIDTH // NUMBEROFRAYS
TEXTURESIZE = 256

MOUSESENSITIVITY = 0.0003
MOUSEMAX = 40
MOUSEBORDERLEFT = 100
MOUSEBORDERIGHT = WIDTH - MOUSEBORDERLEFT
