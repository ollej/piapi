from pijobs.scrolljob import ScrollJob
from piutil.fortune import Fortune

class FortuneJob(ScrollJob):
    def message(self):
        return Fortune().short()
