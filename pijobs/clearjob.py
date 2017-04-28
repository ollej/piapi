import scrollphatjob

class ClearJob(ScrollphatJob):
    def run(self):
        scrollphat.clear()
        self.sleep()
