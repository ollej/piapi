from os import getenv
from glob import glob
from random import choice

from piutil.command import Command
from pijobs.queuejob import QueueJob

class MusicJob(QueueJob):
    def default_options(self):
        opts = {
            'interval': 0.1,
            'loop': 1,
        }
        return opts

    def loop_iteration(self, step):
        self.play()

    def play(self):
        Command().call(['/usr/bin/mpg321', self.song()])

    def song(self):
        return choice(self.songs())

    def songs(self):
        return glob("{}/*{}".format(self.path(), self.ext()))

    def path(self):
        return getenv('MUSIC_PATH', '/home/pi/music')

    def ext(self):
        return getenv('MUSIC_EXTENSION', '.mp3')
