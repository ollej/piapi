import time
import scrollphat

# TODO: Create super class
# TODO: Have default values for sleep/interval/brightness
# TODO: Reshape array/matrix if necessary

class GraphJob:
    def __init__(self, options):
        self.options = options

    def init(self):
        scrollphat.set_brightness(self.options['brightness'])

    def run(self):
        self.init()
        if isinstance(self.options['graph'], list):
            self.animate(self.options['graph'])
        else:
            scrollphat.graph(self.options['graph'])
        time.sleep(self.options['sleep'])

    def animate(self, graphs):
        for graph in graphs:
            scrollphat.graph(graph)
            time.sleep(self.options['interval'])

    def cleanup(self):
        scrollphat.clear()

