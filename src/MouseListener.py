from pynput import mouse


class MouseListener:
    def __init__(self):
        self.pressed_x = -1
        self.pressed_y = -1
        self.released_x = -1
        self.release_y = -1

    def on_click( self, x, y, button, pressed):
        if pressed:
            self.pressed_x = x
            self.pressed_y = y
        elif pressed == 0:
            self.released_x = x
            self.released_y = y
            return False
        else:
            Print("FEHLER muss ich noch abfangen MouseListener\n")
            return False

    def on_click_output( self, x, y, button, pressed):
        if pressed:
            print(button, ' pressed', x, y)
            self.pressed_x = x
            self.pressed_y = y
        elif pressed == 0:
            print(button, ' released', x, y)
            self.released_x = x
            self.released_y = y
            return False



    def run(self):
        with mouse.Listener( on_move = None,
                             on_click = self.on_click,
                             on_scroll = None) as listener:
            listener.join()

    def run_output(self):
        with mouse.Listener( on_move = None,
                             on_click = self.on_click_output,
                             on_scrol = None) as listener:
            listener.join()

    def getMousePositions(self):
        return (self.pressed_x, self.pressed_y, self.released_x, self.released_y)

    def printMousePositions(self):
        print(self.pressed_x, self.pressed_y, self.released_x, self.released_y)