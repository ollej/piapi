import unicornhat as unicorn
from pijobs.unicornhatjob import UnicornhatJob

# Based on Pimoroni example code:
# https://github.com/pimoroni/unicorn-hat

class UnicornDemo(UnicornhatJob):
    def run(self):
        step = 0
        for loop in range(int(self.options['loop'])):
            for y in range(self.rows):
                for x in range(self.cols):
                    r, g, b = self.effect(x, y, step)
                    r = int(max(0, min(255, r)))
                    g = int(max(0, min(255, g)))
                    b = int(max(0, min(255, b)))
                    unicorn.set_pixel(x, y, r, g, b)

            step += 1
            unicorn.show()
            self.sleep_interval()

    def effect(self, x, y, step):
        pass
