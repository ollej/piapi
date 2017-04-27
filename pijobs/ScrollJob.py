import time
import scrollphat

class ScrollJob:
    def __init__(self, options):
        self.options = options

    def init(self):
        scrollphat.set_brightness(self.options['brightness'])
        scrollphat.set_rotate(self.options['rotate'])

        message = self.options['message'] + '    '
        if self.options['upper'] == True:
            message = message.upper()
        scrollphat.write_string(message, 11)

    def run(self):
        self.init()
        length = scrollphat.buffer_len()
        if self.options['loop'] == True:
            counter = 0
            while True:
                self.scroll()
                counter += 1
                if counter % length == 0:
                    time.sleep(self.options['sleep'])
        else:
            for i in range(length):
                self.scroll()
            time.sleep(self.options['sleep'])

    def scroll(self):
        scrollphat.scroll()
        time.sleep(self.options['interval'])

    def cleanup(self):
        scrollphat.clear()

