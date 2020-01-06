import pygame

class CenterDesign():
    def __init__(self,game):
        self.game=game


    def __call__(self, *args, **kwargs):

        ###make these turn colors and turn into squares and different shapes to music later

        if args == ():
            pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 10, 1)

            pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 20, 2)

            pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 40, 4)

            pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 60, 6)

            pygame.draw.circle(self.game.gameDisplay, self.game.white, (self.game.displayW / 2, self.game.displayH / 2), 80, 8)


        else:
            ticks = args[0]


            if ticks %100 ==1:
                pygame.draw.circle(self.game.gameDisplay, self.game.blue,
                                   (self.game.displayW / 2, self.game.displayH / 2), 10, 1)

                pygame.draw.circle(self.game.gameDisplay, self.game.green,
                                   (self.game.displayW / 2, self.game.displayH / 2), 20, 2)

                pygame.draw.circle(self.game.gameDisplay, self.game.yellow,
                                   (self.game.displayW / 2, self.game.displayH / 2), 40, 4)

                pygame.draw.circle(self.game.gameDisplay, self.game.orange,
                                   (self.game.displayW / 2, self.game.displayH / 2), 60, 6)

                pygame.draw.circle(self.game.gameDisplay, self.game.red,
                                   (self.game.displayW / 2, self.game.displayH / 2), 80, 8)

            elif ticks %10 == 2:
                for i in range(4):
                    pygame.draw.circle(self.game.gameDisplay, self.game.blue,
                                       (self.game.displayW / 2, self.game.displayH / 2), 35 * (i + 1), 1)

            elif ticks % 10 == 3:
                for i in range(30):
                    pygame.draw.circle(self.game.gameDisplay, self.game.blue,
                                   (self.game.displayW / 2, self.game.displayH / 2), 4 * (i+1), 1)


            elif ticks % 10 == 4:
                for i in range(30):
                    pygame.draw.circle(self.game.gameDisplay, self.game.green,
                                   (self.game.displayW / 2, self.game.displayH / 2), 10 * (i+1), 1)


            elif ticks % 10 == 5:
                for i in range(30):
                    pygame.draw.circle(self.game.gameDisplay, self.game.yellow,
                                   (self.game.displayW / 2, self.game.displayH / 2), 10 * (i+1), 1)


            elif ticks %10 == 6:
                for i in range(100):
                    colors = [self.game.green, self.game.yellow, self.game.red]
                    pygame.draw.circle(self.game.gameDisplay, colors[i%len(colors)],
                                       (self.game.displayW / 2, self.game.displayH / 2), 35 * (i + 1), 1)

            elif ticks % 10 == 7:
                for i in range(8):
                    pygame.draw.circle(self.game.gameDisplay, self.game.white,
                                   (self.game.displayW / 2, self.game.displayH / 2), 45 * (i+1), 8)


            elif ticks % 10 == 8:
                for i in range(100):
                    pygame.draw.circle(self.game.gameDisplay, self.game.white,
                                   (self.game.displayW / 2, self.game.displayH / 2), 1 * (i+1), 1)


            elif ticks % 10 == 9:
                colors = [self.game.green, self.game.yellow, self.game.red]
                for i in range(60):
                    pygame.draw.circle(self.game.gameDisplay, colors[i%len(colors)],
                                   (self.game.displayW / 2, self.game.displayH / 2), 5 * (i+1), 1)


            elif ticks % 10 == 0:
                colors = [self.game.green,self.game.yellow,self.game.red]
                for i in range(30):
                    pygame.draw.circle(self.game.gameDisplay, colors[i%len(colors)],
                                   (self.game.displayW / 2, self.game.displayH / 2), 10 * (i+1), 1)


