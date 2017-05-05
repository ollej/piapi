import math
import unicornhat as unicorn
from pijobs.unicorndemo import UnicornDemo

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class SpotlightsJob(UnicornDemo):
    def effect(self, x, y, step):
        xs = math.sin((step) / 100.0) * 20.0
        ys = math.cos((step) / 100.0) * 20.0

        scale = ((math.sin(step / 60.0) + 1.0) / 5.0) + 0.2
        r = math.sin((x + xs) * scale) + math.cos((y + xs) * scale)
        g = math.sin((x + xs) * scale) + math.cos((y + ys) * scale)
        b = math.sin((x + ys) * scale) + math.cos((y + ys) * scale)

        return (r * 255, g * 255, b * 255)
