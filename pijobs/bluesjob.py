import math
import unicornhat as unicorn
from pijobs.unicorndemo import UnicornDemo

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class BluesJob(UnicornDemo):
    def effect(self, x, y, step):
        x -= (self.rows / 2)
        y -= (self.cols / 2)

        xs = (math.sin((x + step) / 10.0) / 2.0) + 1.0
        ys = (math.cos((y + step) / 10.0) / 2.0) + 1.0

        scale = math.sin(step / 6.0) / 1.5
        r = math.sin((x * scale) / 1.0) + math.cos((y * scale) / 1.0)
        b = math.sin(x * scale / 2.0) + math.cos(y * scale / 2.0)
        g = r - .8
        g = 0 if g < 0 else g

        b -= r
        b /= 1.4

        return (r * 255, (b + g) * 255, g * 255)

