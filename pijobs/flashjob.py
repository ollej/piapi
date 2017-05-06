import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class FlashJob(ScrollphatJob):
    def init(self):
        super(FlashJob, self).init()
        scrollphat.clear()

    def loop_iteration(self, step):
        scrollphat.set_pixels(lambda x, y: True, True)
        self.sleep_interval()
        scrollphat.clear()

    def default_options(self):
        return {
                'loop': 5,
                'brightness': 10,
                'interval': 0.2,
                }
