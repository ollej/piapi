import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class ScrollJob(ScrollphatJob):
    def default_options(self):
        opts = {
                'brightness': 2,
                'interval': 0.1,
                'sleep': 1.0,
        }
        return opts

    def init(self):
        self.set_brightness()
        self.set_rotate()
        self.write_message()

    def write_message(self):
        message = self.parse_message()
        scrollphat.write_string(message, 11)

    def message(self):
        return self.options['message']

    def parse_message(self):
        message = self.message() + '    '
        if self.options['upper'] == True:
            message = message.upper()
        return message

    def run(self):
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
            self.sleep()

    def scroll(self):
        scrollphat.scroll()
        self.sleep_interval()

