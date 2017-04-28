import scrollphatjob

class FlashJob(ScrollphatJob):
    def run(self):
        scrollphat.clear()
        for i in range(int(self.options['loop'])):
            scrollphat.set_pixels(lambda x, y: True, True)
            self.sleep_interval()
            scrollphat.clear()
            self.sleep_interval()
        self.sleep()

