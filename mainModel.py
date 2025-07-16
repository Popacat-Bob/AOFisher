from pyautogui import click
from time import sleep


class fisherModel:

    def __init__(self, delay: float = 0.5, clicks: int = 10):
        self.screenTopLeft: int = -1
        self.screenBotRight: int = -1
        self._delay = delay
        self._clicks = clicks

    @property
    def delay(self):
        return self._delay

    @property
    def clicks(self):
        return self._clicks

    def changeDelay(self, delay: float):
        self._delay = delay

    def changeClicks(self, clicks: int):
        self._clicks = clicks

    def catch(self, isPrompted: bool):

        if self.screenTopLeft < 0 and self.screenBotRight < 0:
            raise ValueError("Screen Coordinates not set")

        if isPrompted:

            for _ in range(self._clicks):
                click()
                sleep(self._delay)

