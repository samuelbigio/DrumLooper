import pygame



# ESTABLISH PL AS A LIST FROM THE CENTER [ [(R/2, R), (R/2, -R), (0, R/2 + R)],
#                                        [(-R/2, R), (-R/2, -R), (0, -R/2 - R)]

# if bpm is toggled on check if up and then self.game.BPM +=1 or -=1


# create a display for bpm

class DialBtn:
    def __init__(self,game,up, center,radius, colors):
        self.game = game
        self.up = up
        self.colors = colors

        pl = self.getDialPL(center, radius,up)
        self.pl = pl



        if up:
            self.x =  pl[1][0]
            self.y =  pl[2][1]
            self.w = pl[0][0] - pl[1][0]
            self. h = self.w

        else:
            self.x =  pl[1][0]
            self.w = pl[0][0] - pl[1][0]
            self. h = self.w
            self.y = pl[2][1] - self.h



        self.toggleState = 0



    def getMove(self):
        deafultColor =  self.colors[0]
        otherColor = self.colors[1]

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.polygon(self.game.gameDisplay, deafultColor, self.pl)

        if (( mouse[0] < (self.x + self.w) and mouse[0] > self.x ) and ( mouse[1] < (self.y+self.h) and mouse[1] > self.y )):

            pygame.draw.polygon(self.game.gameDisplay, self.game.green, self.pl)

            if click[0] == 1:
                if self.up:
                    if self.game.bpm<666:
                        self.game.bpm +=1
                else:
                    if self.game.bpm>60:
                        self.game.bpm -=1





        if click[1] == 1:
            print mouse


    def getDialPL(self,center,R,up):
        res = [(0,0),(0,0),(0,0)]

        if up:
            res[0] = (center[0] + R / 2., center[1] - R / 4)
            res[1] = (center[0] - R / 2., center[1] - R / 4)
            res[2] = (center[0], center[1] - R * 5. / 4)

        else:
            res[0]= (center[0] + R/2., R/4 + center[1])
            res[1]= (center[0] - R/2., R/4 + center[1])
            res[2]= (center[0],  R*5/4. + center[1])



        return res