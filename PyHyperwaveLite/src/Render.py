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
from src.Player import *
from src.Sprite import *
from src.Raycasting import *
from src.InstanceRender import *
from src.Map import *

class Game:
    def __init__(self):
        pygame.init()
        Icon = pygame.image.load('./resources/Logo.png')
        pygame.display.set_icon(Icon)
        pygame.display.set_caption("PyHyperwaveLite")

        self.Screen = pygame.display.set_mode(RESOLUTION)
        self.Clock = pygame.time.Clock()
        self.DeltaTime = 1
        self.Start()

    def Start(self):
        self.Map = Map(self)
        self.Player = Player(self)
        self.ObjectRender = InstanceRender(self)
        self.SpriteManager = SpriteManager(self)
        self.Raycaster = Raycasting(self)

    def Update(self):
        self.Player.Update()
        self.Raycaster.Update()
        self.SpriteManager.Update()
        self.DeltaTime = self.Clock.tick(FRAMESPERSECOND)
        pygame.display.flip()

    def Render(self):
        self.ObjectRender.Render()
        self.Player.Render()

    def Events(self):
        for Event in pygame.event.get():
            if (Event.type == pygame.QUIT or (Event.type == pygame.KEYDOWN and Event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()


        
