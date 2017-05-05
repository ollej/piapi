import time
from random import randint

import unicornhat as unicorn
from pijobs.unicornhatjob import UnicornhatJob

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class CrossJob(UnicornhatJob):
    def default_options(self):
        opts = {
            'brightness': 64,
            'interval': 0.03,
        }
        return opts

    def run(self):
        self.points = []
        for loop in range(int(self.options['loop'])):
            if len(self.points) < 10 and randint(0, 5) > 1:
                self.points.append(LightPoint(self.cols, self.rows))
            self.plot_points()
            self.update_positions()
            self.sleep_interval()

    def update_positions(self):
        for point in self.points:
            if point.direction == 1:
                point.y += 1
                if point.y > self.rows - 1:
                    self.points.remove(point)
            elif point.direction == 2:
                point.x += 1
                if point.x > self.cols - 1:
                    self.points.remove(point)
            elif point.direction == 3:
                point.y -= 1
                if point.y < 0:
                    self.points.remove(point)
            else:
                point.x -= 1
                if point.x < 0:
                    self.points.remove(point)

    def plot_points(self):
        unicorn.clear()
        for point in self.points:
            unicorn.set_pixel(point.x, point.y, point.colour[0], point.colour[1], point.colour[2])
        unicorn.show()

class LightPoint:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.direction = randint(1, 4)
        if self.direction == 1:
            self.x = randint(0, self.cols - 1)
            self.y = 0
        elif self.direction == 2:
            self.x = 0
            self.y = randint(0, self.rows - 1)
        elif self.direction == 3:
            self.x = randint(0, self.cols - 1)
            self.y = self.rows - 1
        else:
            self.x = self.cols - 1
            self.y = randint(0, self.rows - 1)

        self.colour = []

        for i in range(0, 3):
            self.colour.append(randint(100, 255))
