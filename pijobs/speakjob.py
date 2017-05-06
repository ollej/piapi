from piutil.fortune import Fortune
from piutil.command import Command
from pijobs.queuejob import QueueJob

class SpeakJob(QueueJob):
    def run(self):
        Command().call(['/usr/bin/espeak', self.message()])

    def message(self):
        return self.options['message']

