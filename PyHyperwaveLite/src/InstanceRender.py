from src.Configure import *

class InstanceRender:
    RenderInstances = []

    def __init__(self,Game):
        self.Game = Game
        self.Screen = Game.Screen
        self.WallTextures = self.ApplyTexture()
        self.SkyOffset = 0

    def Render(self):
        self.DrawBackground()
        self.RenderObjects()

    def DrawBackground(self):
        (self.SkyOffset + 4.5 * self.Game.Player.MouseConfig) % WIDTH
        self.SkyTexture = self.LoadTexture('src/Textures/Skybox.jpg',(WIDTH,HEIGHT/1.5))
        self.Screen.blit(self.SkyTexture, (-self.SkyOffset, 1))
        self.Screen.blit(self.SkyTexture, (-self.SkyOffset + WIDTH, 500))
        NewColour = [255 / (1 + HEIGHT/2 ** 5 * 1.5)] * 3
        pygame.draw.rect(self.Screen, NewColour, (0,(HEIGHT/2), WIDTH, HEIGHT))
        
    def ShadowRendering(self,Image,Depth):
        NewColour = [255 / (1 + Depth ** 5 * 0.0002)] * 3
        Image.fill(NewColour, special_flags=pygame.BLEND_MULT)

    def RenderObjects(self):
        Objects = self.Game.Raycaster.RenderJob
        for Depth, Image, Position in Objects:
            self.ShadowRendering(Image,Depth)
            self.Screen.blit(Image, Position)

    @staticmethod
    def LoadTexture(path,Resolution=(TEXTURESIZE,TEXTURESIZE)):
        NewTexture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(NewTexture, Resolution)
    
    def ApplyTexture(self):
        return {
            1: self.LoadTexture('src/Textures/BoltedMetal.jpg')
        }