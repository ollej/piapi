import time

class QueueJob:
    def __init__(self, options):
        self.options = options
        self.init()

    def init(self):
        pass

    def run(self):
        self.sleep()

    def sleep(self):
        if self.options['sleep'] is not None:
            time.sleep(self.options['sleep'])

    def cleanup(self):
        pass
