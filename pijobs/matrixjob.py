import scrollphat
from pijobs.scrollphatjob import ScrollphatJob

class MatrixJob(ScrollphatJob):
    # matrix is an array of strings with 55 1 or 0
    def run(self):
        for matrix_string in self.options['matrix']:
            matrix = self.convert_to_matrix(list(matrix_string))
            self.update_matrix(matrix)
            self.sleep_interval()

    def update_matrix(self, matrix):
        scrollphat.set_pixels(lambda x, y: matrix[y][x], True)

    def convert_to_matrix(self, arr):
        """
        Convert a 1 dimensional array into a 2 dimensional array.
        """
        matrix_array = self.limit_array(arr)
        counter = 0
        matrix = []
        for i in range(self.MATRIX_ROWS):
            row = []
            for j in range(self.MATRIX_COLS):
                row.append(int(matrix_array[counter]))
                counter += 1
            matrix.append(row)
        return matrix

    def limit_array(self, arr):
        """
        Ensure arr is exactly self.MATRIX_LEDS elements long.
        Longer array is cut off, shorter is filled with zeroes.
        """
        if len(arr) > self.MATRIX_LEDS:
            return arr[:self.MATRIX_LEDS]
        elif len(arr) < self.MATRIX_LEDS:
            return arr + [0] * (self.MATRIX_LEDS - len(arr))
        else:
            return arr
