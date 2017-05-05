import math
import colorsys
import unicornhat as unicorn
from pijobs.unicorndemo import UnicornDemo

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class TunnelJob(UnicornDemo):
    def effect(self, x, y, step):
        x -= (self.cols / 2)
        y -= (self.rows / 2)
        speed = step / 100.0

        xo = math.sin(step / 27.0) * 2
        yo = math.cos(step / 18.0) * 2

        x += xo
        y += yo

        if y == 0:
            if x < 0:
                angle = -(math.pi / 2)
            else:
                angle = (math.pi / 2)
        else:
            angle = math.atan(x / y)

        if y > 0:
            angle += math.pi

        angle /= 2 * math.pi # convert angle to 0...1 range

        shade = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) / 2.1
        shade = 1 if shade > 1 else shade

        angle += speed
        depth = speed + (math.sqrt(math.pow(x, 2) + math.pow(y, 2)) / 10)

        col1 = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, .8)
        col2 = colorsys.hsv_to_rgb((step % 255) / 255.0, 1, .3)

        col = col1 if int(abs(angle * 6.0)) % 2 == 0 else col2

        td = .3 if int(abs(depth * 3.0)) % 2 == 0 else 0

        col = (col[0] + td, col[1] + td, col[2] + td)

        col = (col[0] * shade, col[1] * shade, col[2] * shade)

        return (col[0] * 255, col[1] * 255, col[2] * 255)
