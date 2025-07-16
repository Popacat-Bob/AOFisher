from pynput.mouse import Listener, Button
from mss import mss
import numpy as np
from pyautogui import position

class mouseScreenCaptureModel:
    def capture(self):

        topLeft: tuple[int, int] = None
        botRight: tuple[int, int] = None

        def on_click(x, y, button, pressed):
            nonlocal topLeft, botRight

            if pressed and button == Button.left:
                topLeft = (x, y)
            elif not pressed and button == Button.left:
                botRight = (x, y)
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        return topLeft, botRight

class getColoratMouseModel:
    def capture(self):
        x, y = position()
        color: tuple[int, int, int] | None = None


        def on_click(x, y, button, pressed):
            nonlocal color

            if pressed and button == Button.left:
                with mss() as sct:
                    region = {"top": y, "left": x, "width": 1, "height": 1}
                    img = np.array(sct.grab(region), dtype=np.uint8)
                    img = np.flip(img[:, :, :3], 2)
                    color = tuple(img[0, 0])
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()
            
        print(color)
        return color