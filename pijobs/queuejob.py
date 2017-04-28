import time
from collections import defaultdict

class QueueJob:
    def __init__(self, options):
        self.options = self.parse_options(options)
        self.init()

    def dafault_options(self):
        return {}

    def parse_options(self, options):
        opts = defaultdict(lambda: None, self.default_options())
        opts.update(options)
        return opts

    def init(self):
        pass

    def run(self):
        self.sleep()

    def sleep(self):
        if self.options['sleep'] is not None:
            time.sleep(self.options['sleep'])

    def cleanup(self):
        pass
