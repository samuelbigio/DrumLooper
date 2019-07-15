from Main.DrumPage.Buttons.ToggleButtons import toggleBtn


#self.game.mainmenu.synthMain.displaynotes
class DisplayScale():
    def __init__(self,game):
        self.game= game
        self.scales = ["Major","Minor","Blues","Penatonic"]

        self.scaleButton = [0] * len(self.scales)
        for i in range(len(self.scales)):
            self.scaleButton[i] = toggleBtn(self.game)

        self.activeScale = -1










    def __call__(self, *args, **kwargs):


        #self.game.buttonSize *5.25
        for i in range(len(self.scales)):
            self.scaleButton[i].button(self.scales[i],
                                        self.game.displayW * .015,
                                        self.game.displayH * .1 + i *self.game.buttonSize *5.25,
                                        self.game.buttonSize *3,
                                        self.game.buttonSize,
                                        self.game.lightpurple,
                                        self.game.bright_gray,
                                        onStr = self.scales[i],
                                        hoverStr = self.scales[i],
                                        whenClicked = (lambda: self.noteclicked(i)) #pass a function with argument as a
                                        #function call back
                                       )



    def noteclicked(self,num):
        for i in range(len(self.scaleButton)):
            if i != num:
                self.scaleButton[i].toggleState=0

        if self.scaleButton[num].toggleState is 0:
            self.activeScale = -1

        else:
            self.activeScale = self.scales[num]




