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

