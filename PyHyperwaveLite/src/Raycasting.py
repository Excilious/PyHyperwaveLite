from src.Configure import *

class Raycasting:
    def __init__(self,Game):
        self.Game = Game
        self.Results = []
        self.RenderJob = []
        self.TextureAssets = self.Game.ObjectRender.WallTextures

    def GetRenderJob(self):
        self.RenderJob = []
        for Ray,Value in enumerate(self.Results):
            Depth,ProjectedHeight,Textures,Offset = Value
            if (ProjectedHeight < HEIGHT):
                WallColumn = self.TextureAssets[Textures].subsurface(
                    Offset * (TEXTURESIZE - SCREENSCALE), 0, SCREENSCALE,TEXTURESIZE
                )
                WallColumn = pygame.transform.scale(WallColumn, (SCREENSCALE, ProjectedHeight))
                WallPosition = (Ray * SCREENSCALE, (HEIGHT/2) - ProjectedHeight//2)
            else:
                TextureHeight = TEXTURESIZE * HEIGHT / ProjectedHeight
                WallColumn = self.TextureAssets[Textures].subsurface(
                    Offset * (TEXTURESIZE - SCREENSCALE), TEXTURESIZE/2 - TextureHeight //2,
                    SCREENSCALE, TextureHeight
                )
                WallColumn = pygame.transform.scale(WallColumn,(SCREENSCALE,HEIGHT))
                WallPosition = (Ray * SCREENSCALE ,0)
            self.RenderJob.append((Depth,WallColumn,WallPosition))

    @jit
    def Raycast(self):
        self.Results = []
        
        ObjectX, ObjectY = self.Game.Player.Position
        XMap, YMap = self.Game.Player.MapPosition
        RaycastAngleZ = self.Game.Player.ZAngle - (FIELDOFVIEW/2) + 0.0001
        TextureVertical,TextureHorizontal = 1,1

        for Ray in range(NUMBEROFRAYS):
            SinA = math.sin(RaycastAngleZ)
            CosA = math.cos(RaycastAngleZ)
            YHorizontal,DeltaY = (YMap + 1,1) if (SinA > 0) else (YMap - 1e-6,-1)
            DepthHorizontal = (YHorizontal - ObjectY) / SinA

            XHorizontal = ObjectX + DepthHorizontal * CosA
            DeltaDepth = DeltaY / SinA
            DeltaX = DeltaDepth * CosA

            for x in range(MAXDEPTH):
                TileHorizontal = int(XHorizontal), int(YHorizontal)
                if (TileHorizontal in self.Game.Map.WorldMap):
                    TextureHorizontal = self.Game.Map.WorldMap[TileHorizontal]
                    break
                XHorizontal += DeltaX
                YHorizontal += DeltaY
                DepthHorizontal += DeltaDepth

            XVerticle, DeltaX = (XMap + 1,1) if (CosA > 0) else (XMap - 1e-6, -1)
            DepthVerticle = (XVerticle - ObjectX) / CosA

            YVerticle = ObjectY + DepthVerticle * SinA
            DeltaDepth = DeltaX / CosA
            DeltaY = DeltaDepth * SinA

            for y in range(MAXDEPTH):
                TileVerticle = int(XVerticle), int(YVerticle)
                if (TileVerticle in self.Game.Map.WorldMap):
                    TextureVertical = self.Game.Map.WorldMap[TileVerticle]
                    break
                XVerticle += DeltaX
                YVerticle += DeltaY
                DepthVerticle += DeltaDepth
            
            if (DepthVerticle < DepthHorizontal):
                Depth,Texture = DepthVerticle, TextureVertical
                YVerticle %= 1
                Offset = YVerticle if (CosA > 0) else (1 - YVerticle)
            else:
                Depth,Texture = DepthHorizontal, TextureHorizontal
                XHorizontal %= 1
                Offset = (1 - XHorizontal) if (SinA > 0) else XHorizontal

            Depth *= math.cos(self.Game.Player.ZAngle - RaycastAngleZ)
            self.ProjectedHeight = DISTANCE3D / (Depth + 0.0001)
            self.Results.append((Depth,self.ProjectedHeight - self.Game.Player.ZAngle, Texture,Offset))

            RaycastAngleZ += DELTAANGLE
    
    def Update(self):
        self.Raycast()
        self.GetRenderJob()
