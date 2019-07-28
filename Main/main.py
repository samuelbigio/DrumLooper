from PygameInit import Game
import pygame
import sys



def main():
    sys.stdout=open('output.txt', 'w')
    game = Game()
    game.game_loop()
    pygame.mixer.quit()
    pygame.quit()
    quit()



if __name__ == "__main__":

    main()

