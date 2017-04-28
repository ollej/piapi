import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class ClearJob(ScrollphatJob):
    def run(self):
        scrollphat.clear()
        self.sleep()
