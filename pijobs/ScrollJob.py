import scrollphatjob

class ScrollJob(ScrollphatJob):
    def init(self):
        self.set_rotate()
        self.set_brightness()
        scrollphat.write_string(self.message(), 11)

    def message(self):
        message = self.options['message'] + '    '
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

    def set_rotate(self):
        if self.options['rotate'] is not None:
            scrollphat.set_rotate(self.options['rotate'])

