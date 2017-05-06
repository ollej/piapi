import unicornhat as unicorn
from pijobs.unicornhatjob import UnicornhatJob

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class UnicornDemo(UnicornhatJob):
    def loop_iteration(self, step):
        for y in range(self.rows):
            for x in range(self.cols):
                r, g, b = self.effect(x, y, step)
                r = int(max(0, min(255, r)))
                g = int(max(0, min(255, g)))
                b = int(max(0, min(255, b)))
                unicorn.set_pixel(x, y, r, g, b)

        unicorn.show()

    def effect(self, x, y, step):
        pass
