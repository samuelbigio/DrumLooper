from PygameInit import Game
import pygame
import os





def main():
    game = Game()
    game.game_loop()
    pygame.mixer.quit()
    pygame.quit()
    quit()


if __name__ == "__main__":

    main()

