from pyautogui import alert, click
from time import sleep

class fisherModel:

    def __init__(self):
        self.screenTopLeft: int = -1
        self.screenBotRight: int = -1

    def catch(self, isPrompted: bool):

        if self.screenTopLeft < 0 and self.screenBotRight < 0:
            raise ValueError("Screen Coordinates not set")

        if isPrompted:

            for i in range(5):
                click()
                sleep(0.5)


