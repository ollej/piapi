import math
import unicornhat as unicorn
from random import randint
from pijobs.unicornhatjob import UnicornhatJob

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class SparklesJob(UnicornhatJob):
    def loop_iterations(self):
        int(self.options['loop']) * self.rows * self.cols

    def loop_iteration(self, step):
        x = randint(0, self.cols - 1)
        y = randint(0, self.rows - 1)
        r, g, b = self.calculate_color(x, y)
        unicorn.set_pixel(x, y, r, g, b)
        unicorn.show()

    def calculate_color(self, x, y):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return [r, g, b]
