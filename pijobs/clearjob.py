import scrollphat

class BrightnessJob:
    def __init__(self, options):
        self.options = options

    def run(self):
        scrollphat.set_brightness(self.options['brightness'])
