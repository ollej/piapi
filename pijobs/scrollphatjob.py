import time
import scrollphat
from pijobs.queuejob import QueueJob

class ScrollphatJob(QueueJob):
    MATRIX_LEDS = 55
    MATRIX_COLS = 11
    MATRIX_ROWS = 5

    def init(self):
        self.set_rotate()
        self.set_brightness()

    def set_brightness(self):
        if self.options['brightness'] is not None:
            scrollphat.set_brightness(int(self.options['brightness']))

    def set_rotate(self):
        if self.options['rotate'] is not None:
            scrollphat.set_rotate(self.options['rotate'])

    def sleep_interval(self):
        if self.options['interval'] is not None:
            time.sleep(float(self.options['interval']))

    def cleanup(self):
        scrollphat.clear()
