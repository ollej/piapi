import time
import unicornhat as unicorn
from pijobs.queuejob import QueueJob

class UnicornhatJob(QueueJob):
    MATRIX_LEDS = 32
    MATRIX_COLS = 8
    MATRIX_ROWS = 4

    def init(self):
        unicorn.set_layout(unicorn.AUTO)
        self.set_rotate()
        self.set_brightness()
        self.cols, self.rows = unicorn.get_shape()

    def default_options(self):
        opts = {
            'brightness': 64,
            'interval': 0.01,
        }
        return opts

    def set_brightness(self):
        if self.options['brightness'] is not None and self.options['brightness'] < 128:
            brightness = float(self.options['brightness']) / 128
            unicorn.brightness(brightness)

    def set_rotate(self):
        if self.options['rotate'] is not None and self.options['rotate'] is True:
            unicorn.rotation(180)
        else:
            unicorn.rotation(0)

    def cleanup(self):
        unicorn.off()
        unicorn.show()

