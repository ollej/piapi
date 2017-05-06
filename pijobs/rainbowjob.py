import math
import unicornhat as unicorn
from pijobs.unicornhatjob import UnicornhatJob

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class RainbowJob(UnicornhatJob):
    def init(self):
        super(RainbowJob, self).init()
        self.i = 0.0
        self.offset = 30

    def loop_iteration(self, step):
        self.i = self.i + 0.3
        for y in range(self.rows):
            for x in range(self.cols):
                r, g, b = self.calculate_color(x, y, self.i)
                unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()

    def calculate_color(self, x, y, i):
        r = 0
        g = 0
        r = (math.cos((x + i) / 2.0) + math.cos((y + i) / 2.0)) * 64.0 + 128.0
        g = (math.sin((x + i) / 1.5) + math.sin((y + i) / 2.0)) * 64.0 + 128.0
        b = (math.sin((x + i) / 2.0) + math.cos((y + i) / 1.5)) * 64.0 + 128.0
        r = int(max(0, min(255, r + self.offset)))
        g = int(max(0, min(255, g + self.offset)))
        b = int(max(0, min(255, b + self.offset)))
        return [r, g, b]
