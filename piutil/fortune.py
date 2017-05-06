from piutil.command import Command

class Fortune:
    def short(self):
        return Command().run(['/usr/games/fortune', '-s'])

