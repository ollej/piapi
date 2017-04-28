import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class FlashJob(ScrollphatJob):
    def run(self):
        scrollphat.clear()
        for i in range(int(self.options['loop'])):
            scrollphat.set_pixels(lambda x, y: True, True)
            self.sleep_interval()
            scrollphat.clear()
            self.sleep_interval()
        self.sleep()

    def default_options(self):
        return {
                'loop': 5,
                'brightness': 10,
                'interval': 0.2,
                }
