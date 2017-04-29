import subprocess
from pijobs.scrolljob import ScrollJob

class FortuneJob(ScrollJob):
    def message(self):
        return self.run_cmd('fortune')

    def run_cmd(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.communicate()[0]
        return output
