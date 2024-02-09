from src.Configure import *

class SpriteManager:
    def __init__(self,Game):
        self.Game = Game
        self.X, self.Y = 0,0
        self.SpriteMap = {}

    def ProjectSprite(self,Sprite):
        Projection = DISTANCE3D / self.NormalDistance
        ProjectWidth, ProjectHeight = Projection * (270 / 463), Projection
        Image = pygame.transform.scale(self.SpriteMap[Sprite],(ProjectWidth,ProjectHeight))

        Position = self.ScreenX - ProjectWidth, HEIGHT/2 - ProjectHeight // 2
        self.Game.Raycaster.RenderJob.append((self.NormalDistance, Image, Position))

    def GenerateSprite(self):
        self.DeltaX = self.X - self.Game.Player.X
        self.DeltaY = self.Y - self.Game.Player.Y
        self.Theta = math.atan2(self.DeltaY, self.DeltaX)

        Delta = self.Theta - self.Game.Player.ZAngle
        if ((self.DeltaX > 0 and self.Game.Player.ZAngle > math.pi) or (self.DeltaX < 0 and self.DeltaY < 0)):
            Delta += math.tau
        
        DeltaRay = Delta / DELTAANGLE
        self.ScreenX = (NUMBEROFRAYS/2 + DeltaRay) * SCREENSCALE
        self.Distance = (self.DeltaX ** 2 + self.DeltaY ** 2) ** 1/2
        self.NormalDistance = self.Distance * math.cos(Delta)
        if (-270/2 < self.ScreenX < (WIDTH + 270/2) and self.NormalDistance > 0.5):
            ...

    def Update(self):
        self.GenerateSprite()


