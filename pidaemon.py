"""pidaemon.py

Usage:
  pidaemon.py [--brightness=<b>] [--sleep=<s>] [--interval=<s>]
  pidaemon.py (-h | --help)
  pidaemon.py --version

Options:
  -h --help         Show this screen.
  --version         Show version
  --brightness=<b>  Default brightness level 1-255 [default: 2]
  --interval=<s>    Default interval in seconds between each frame in jobs [default: 0.1]
  --sleep=<s>       Default number of seconds to pause after each job [default: 0]

"""

import sys
import signal
from docopt import docopt

from piqueue import piqueue

class PiDaemon():
    def __init__(self):
        self.session = piqueue.Session()
        self.setup_signal_handlers()

    def parse_options(self, opts):
        options = {
            'brightness': int(opts['--brightness']),
            'sleep': float(opts['--sleep']),
            'interval': float(opts['--interval']),
        }
        return options

    def run(self):
        job = self.next_job()
        self.run_job(job)
        if job.options['keep'] == True:
            self.add_job(job)
        else:
            self.delete_job(job)

    def run_job(self, job):
        instance = job.job_instance()
        instance.run()

    def queue(self):
        return session.query(piqueue.Job).order_by(piqueue.Job.date_created)

    def next_job(self):
        return self.queue().first()

    def add_job(self, old_job):
        new_job = piqueue.Job(old_job.job_name, old_job.options)
        self.session.add(new_job)
        self.session.commit()

    def delete_job(self, job):
        self.session.delete(job)
        self.session.commit()

    def setup_signal_handlers(self):
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)

    def cleanup(self, signum, frame):
        sys.exit(-1)


if __name__ == '__main__':
    opts = docopt(__doc__, version='PiDaemon v1.0')
    PiDaemon().run()
