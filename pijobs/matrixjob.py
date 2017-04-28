import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

# TODO: Create super class
# TODO: Have default values for sleep/interval/brightness
# TODO: Reshape array/matrix if necessary

class MatrixJob(ScrollphatJob):
    # matrix is a string with 55 1 or 0, or an array of those strings to animate.
    def run(self):
        if isinstance(self.options['matrix'], list):
            self.animate(self.options['matrix'])
        else:
            self.update_matrix(self.options['matrix'])
        self.sleep()

    def animate(self, matrices):
        # TODO: set interval for each "frame"
        # TODO: set brightness for each frame
        for matrix in matrices:
            self.update_matrix(matrix)
            self.sleep_interval()

    def update_matrix(self, matrix):
        # TODO: Convert matrix
        scrollphat.set_pixels(lambda x, y: matrix[y][x], True)

