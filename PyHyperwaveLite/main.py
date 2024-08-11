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

from src.Render import *
import asyncio

async def Render():
    Engine = Game()
    while True:
        Engine.Events()
        Engine.Update()
        Engine.Render()
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(str(Engine.Clock.get_fps()))
        await asyncio.sleep(0)

if (__name__ == "__main__"):
    asyncio.run(Render())

