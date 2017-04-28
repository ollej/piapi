import scrollphat

class ScrollphatJob(QueueJob):
    def init(self):
        self.set_brightness()

    def set_brightness(self):
        if self.options['brightness'] is not None:
            scrollphat.set_brightness(int(self.options['brightness']))

    def sleep_interval(self):
        if self.options['interval'] is not None:
            time.sleep(float(self.options['interval']))

    def cleanup(self):
        scrollphat.clear()
