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

from src.Configure import *

_ = False

Minimap = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,_,_,_,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Map:
    def __init__(self,Game):
        self.Game = Game
        self.MiniMap = Minimap
        self.WorldMap = {}
        self.GetMap()

    def GetMap(self):
        for X,Row in enumerate(self.MiniMap):
            for Y,Value in enumerate(Row):
                if (Value):
                    self.WorldMap[(X,Y)] = Value

    def Render(self):
        [pygame.draw.rect(self.Game.Screen, 'darkgray',(Pos[0] * 100, Pos[1] * 100,100,100),2) for Pos in self.WorldMap]
