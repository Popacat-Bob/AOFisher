from pynput.mouse import Listener, Button
import threading

class mouseScreenModel:
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
    