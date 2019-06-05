import MouseListener
import pynput
from PIL import Image
import pyscreenshot as ImageGrab

ml = MouseListener.MouseListener()
ml.run()
(x1,y1, x2, y2) = ml.getMousePositions()
print(x1)
print(y1)
print(x2)
print(y2)
im = ImageGrab.grab(bbox=(min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)))

im.show()

