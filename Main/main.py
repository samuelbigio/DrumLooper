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

"""

Moving forward i want to create a dynamic grid for each instrument
each instrument should have a picture and then eight buttons
the grid should be dynamic with how many instruments/buttons

i want the instruments buttons to be pressable and then add bits for the state
if the bits are on i want that to play in tempo
if the bits are off nothing happens

i wantt a marker to follow the bpm (this is optional)

if i have enough time i want a drop down to pick instruments (this wont matter in hardware so it might be waste of time)



"""