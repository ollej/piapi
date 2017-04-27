import scrollphat

class ClearJob:
    def __init__(self, options):
        self.options = options

    def run(self):
        scrollphat.clear()
