import time
import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

# TODO: Create super class
# TODO: Have default values for sleep/interval/brightness
# TODO: Reshape array/matrix if necessary

class GraphJob(ScrollphatJob):
    def run(self):
        if isinstance(self.options['graph'], list):
            self.animate(self.options['graph'])
        else:
            scrollphat.graph(self.options['graph'])
        self.sleep()

    def animate(self, graphs):
        for graph in graphs:
            scrollphat.graph(graph)
            self.sleep_interval()

