from pyautogui import pixel, position 
from pynput import mouse

class colorGetter:
    def __init__(self):
        self.color = None 

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left and not pressed:
            self.color = pixel(*position())
            self.listener.stop() 

    def start(self):
        self.listener = mouse.Listener(
                on_click = self.on_click
                )
        
        self.listener.start()

    def stop(self):
        self.listener.stop()

obj_a = colorGetter()
obj_a.start()
while obj_a.color is None:
    ...
print(obj_a.color)
