from src.Configure import *

class Player:
    def __init__(self,Game):
        self.Game = Game
        self.X, self.Y = PLAYERPOSITION
        self.ZAngle = PLAYERANGLE

    def Movement(self):
        SinA = math.sin(self.ZAngle)
        CosA = math.cos(self.ZAngle)
        DeltaX,DeltaY = 0,0
        Speed = PLAYERSPEED * self.Game.DeltaTime

        SpeedSin = (Speed * SinA)
        SpeedCos = (Speed * CosA)

        BindedKeys = pygame.key.get_pressed()
        if (BindedKeys[pygame.K_w]):
            DeltaX += SpeedCos
            DeltaY += SpeedSin
        if (BindedKeys[pygame.K_s]):
            DeltaX += -SpeedCos
            DeltaY += -SpeedSin
        if (BindedKeys[pygame.K_a]):
            DeltaX += SpeedSin
            DeltaY += -SpeedCos
        if (BindedKeys[pygame.K_d]):
            DeltaX += -SpeedSin
            DeltaY += SpeedCos

        self.CheckCollisions(DeltaX,DeltaY)
        self.ZAngle %= math.tau
        

    def IsAWall(self,X,Y):
        return (X,Y) not in self.Game.Map.WorldMap
    
    def CheckCollisions(self,DeltaX,DeltaY):
        CurrentScale = 60 / self.Game.DeltaTime

        if (self.IsAWall(int(self.X + DeltaX * CurrentScale), int(self.Y))):
            self.X += DeltaX
        if (self.IsAWall(int(self.X), int(self.Y + DeltaY * CurrentScale))):
            self.Y += DeltaY

    def Render(self):
        ...

    def MouseControl(self):
        MouseX, MouseY = pygame.mouse.get_pos()

        if ((MouseX < MOUSEBORDERLEFT) or (MouseX > MOUSEBORDERIGHT)):
            pygame.mouse.set_pos([WIDTH/2,HEIGHT/2])

        if ((MouseY <= 0) or (MouseY > 470)):
            pygame.mouse.set_pos([WIDTH/2,HEIGHT/2])
        self.MouseConfig = pygame.mouse.get_rel()[0]
        self.MouseConfig = max(-MOUSEMAX, min(MOUSEMAX, self.MouseConfig))
        self.ZAngle += self.MouseConfig * MOUSESENSITIVITY * self.Game.DeltaTime

    def Update(self):
        self.Movement()
        self.MouseControl()

    @property
    def Position(self):
        return self.X, self.Y
    
    @property
    def MapPosition(self):
        return int(self.X), int(self.Y)
    
    