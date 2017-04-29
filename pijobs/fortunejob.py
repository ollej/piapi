import subprocess
from pijobs.scrolljob import ScrollJob

class FortuneJob(ScrollJob):
    def message(self):
        return self.run_cmd(['fortune', '-s'])

    def run_cmd(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = self.decode_output(p.communicate()[0])
        return output

    def decode_output(self, output):
        if output is not None:
            output = output.decode("utf-8").rstrip()
        else:
            output = ''
        return output
