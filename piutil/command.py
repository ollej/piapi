import subprocess

class Command:
    def call(self, cmd):
        subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def run(self, cmd):
        output = subprocess.check_output(cmd, shell=True)
        return self.decode(output)

    def decode(self, output):
        if output is not None:
            output = output.decode("utf-8").rstrip()
        else:
            output = ''
        return output
