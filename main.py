from pyautogui import alert

class fisherModel:
    
    def __init__(self):
        self.screenTopLeft: int = -1
        self.screenBotRight: int = -1

    def catch(self, isPrompted: bool):
        if self.screenTopLeft < 0 and self.screenBotRight < 0:
            alert(text= "Fishing screen not set", title="alert", button="ok")

