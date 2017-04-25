from flask import Flask
from flask_restful import Resource, Api, reqparse

import scrollphat

# Web server with REST API
#  * /matrix - 1/0 for each pixel, autoupdate flag, brightness level
#  * /scroll - scroll message (params: rotate, loop=x times/forever)
#  * /clear - clear all
#  * /graph - integers for each bar, rotation
#  * /brightness

# TODO: Return JSON on failure
# TODO: Refactor brightness/rotate params

app = Flask(__name__)
api = Api(app)

class MatrixHandler:
    def __init__(self, matrix_string):
        self.matrix = self.parse_matrix_string(matrix_string)

    def parse_matrix_string(self, matrix_string):
        pass

    def handler(self):
        pass

class Matrix(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matrix', required=True, help='Matrix to update all pixels')
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        parser.add_argument('rotate', type=int, help='Rotate 180 degrees')
        args = parser.parse_args()

        scrollphat.set_pixels(MatrixHandler(args['matrix']).handler, True)

        return '', 200

class Scroll(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', required=True, help='Scroll message')
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        parser.add_argument('rotate', type=int, help='Rotate 180 degrees')
        args = parser.parse_args()

        scrollphat.write_string(args['message'])
        # TODO: Handle scroll

        return '', 200

class Graph(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('graph', required=True, help='Graphs to display')
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        parser.add_argument('rotate', type=int, help='Rotate 180 degrees')
        args = parser.parse_args()

        graph = args['graph']
        return '', 200

class Brightness(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        args = parser.parse_args()

        scrollphat.set_brightness(int(args['brightness']))
        return '', 200

class Clear(Resource):
    def post(self):
        scrollphat.clear()
        return '', 200

api.add_resource(Matrix, '/matrix')
api.add_resource(Scroll, '/scroll')
api.add_resource(Graph, '/graph')
api.add_resource(Brightness, '/brightness')
api.add_resource(Clear, '/clear')

if __name__ == '__main__':
    app.run(debug=True)
