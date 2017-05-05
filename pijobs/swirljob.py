import math
import unicornhat as unicorn
from pijobs.unicorndemo import UnicornDemo

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class SwirlJob(UnicornDemo):
    def effect(self, x, y, step):
        x -= (self.cols / 2)
        y -= (self.rows / 2)

        dist = math.sqrt(pow(x, 2) + pow(y, 2)) / 2.0
        angle = (step / 10.0) + (dist * 1.5)
        s = math.sin(angle);
        c = math.cos(angle);

        xs = x * c - y * s;
        ys = x * s + y * c;

        r = abs(xs + ys)
        r = r * 64.0
        r -= 20

        return (r, r + (s * 130), r + (c * 130))
