"""pidaemon.py

Usage:
  pidaemon.py [--brightness=<b>] [--sleep=<s>] [--interval=<s>] [--wait=<s>]
  pidaemon.py (-h | --help)
  pidaemon.py --version

Options:
  -h --help         Show this screen.
  --version         Show version
  --brightness=<b>  Default brightness level 1-255 [default: 2]
  --interval=<s>    Default interval in seconds between each frame in jobs [default: 0.1]
  --sleep=<s>       Default number of seconds to pause after each job [default: 0]
  --wait=<s>        Time between each iteration when polling for job on an empty queue. [default: 5]

"""

import sys
import signal
import time
from docopt import docopt
from collections import defaultdict

import settings
from piqueue import piqueue

class PiDaemon():
    def __init__(self, opts):
        self.running = None
        self.options = self.parse_options(opts)
        self.session = piqueue.Session()
        self.setup_signal_handlers()

    def parse_options(self, opts):
        options = defaultdict(lambda: None, {
            'brightness': int(opts['--brightness']),
            'sleep': float(opts['--sleep']),
            'interval': float(opts['--interval']),
            'wait': float(opts['--wait']),
        })
        return options

    def run(self):
        while True:
            job = self.next_job()
            if job is not None:
                self.run_job(job)
                if job.options['keep'] == True:
                    self.add_job(job)
                self.delete_job(job)
            else:
                time.sleep(self.options['wait'])

    def run_job(self, job):
        self.running = job.job_instance(self.options.copy())
        self.running.run()
        self.running.sleep()
        self.running.cleanup()
        self.running = None

    def queue(self):
        return self.session.query(piqueue.Job).order_by(piqueue.Job.date_created)

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
        if self.running is not None:
            self.running.cleanup()
        sys.exit(-1)


if __name__ == '__main__':
    opts = docopt(__doc__, version='PiDaemon v1.0')
    PiDaemon(opts).run()
