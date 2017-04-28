import time
import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class GraphJob(ScrollphatJob):
    self.MATRIX_WIDTH = 11

    def run(self):
        if isinstance(self.options['graph'], list):
            self.animate(self.options['graph'])
        else:
            self.show_graph(self.options['graph'])

    def animate(self, graphs):
        for graph in graphs:
            self.show_graph(graph)
            self.sleep_interval()

    def show_graph(self, graph_string):
        graph = self.split_graph(graph_string)
        scrollphat.graph(graph)
        if len(graph) > self.MATRIX_WIDTH:
            self.scroll_graph()

    def scroll_graph(self):
        for i in range(len(graph)):
            scrollphat.scroll()
            time.sleep_interval()

    def split_graph(self, graph_string):
        return list(graph_string)

