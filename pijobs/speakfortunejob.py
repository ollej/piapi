from piutil.fortune import Fortune
from pijobs.speakjob import SpeakJob

class SpeakfortuneJob(SpeakJob):
    def message(self):
        return Fortune().short()
