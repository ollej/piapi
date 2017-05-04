import time
from collections import defaultdict

class QueueJob:
    def __init__(self, options, default_options={}):
        self.options = self.parse_options(options, default_options)
        self.init()

    def default_options(self):
        return {}

    def parse_options(self, options, default_options):
        opts = defaultdict(lambda: None, default_options)
        opts.update(self.default_options())
        opts.update(options)
        return opts

    def init(self):
        pass

    def run(self):
        self.sleep()

    def sleep(self):
        if self.options['sleep'] is not None:
            time.sleep(self.options['sleep'])

    def sleep_interval(self):
        if self.options['interval'] is not None:
            time.sleep(float(self.options['interval']))

    def cleanup(self):
        pass
