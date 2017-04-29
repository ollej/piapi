import time
import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class GraphJob(ScrollphatJob):
    def run(self):
        for graph in self.options['graph']:
            self.show_graph(list(graph))
            self.sleep_interval()

    def show_graph(self, graph):
        scrollphat.graph(graph)
        if len(graph) > self.MATRIX_COLS:
            self.scroll_graph(len(graph))
        self.sleep()

    def scroll_graph(self, length):
        for i in range(length):
            scrollphat.scroll()
            self.sleep_interval()

