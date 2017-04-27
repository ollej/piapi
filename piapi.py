from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from piqueue import piqueue

# Setup database: Base.metadata.create_all(engine)

# TODO: Return JSON on failure
# TODO: Refactor brightness/rotate params
# TODO: One resource class that refers parameter parsing, job creation and job handling
# TODO: Ensure job_name is a proper job

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/queue.db'
ma = Marshmallow(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

class JobSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'job_name', 'date_created', 'options')

job_schemas = JobSchema(many=True)

def clean_dict(data):
    return {k: v for k, v in data.items() if v is not None}

class Queue(Resource):
    def post(self, job_name):
        parser = reqparse.RequestParser()
        parser.add_argument('message', help='Scroll message')
        parser.add_argument('matrix', help='Matrix to update all pixels')
        parser.add_argument('graph', help='Graphs to display')
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        parser.add_argument('rotate', type=int, help='Rotate 180 degrees')
        parser.add_argument('sleep', type=float, help='Seconds to sleep after job')
        parser.add_argument('interval', type=float, help='Seconds to sleep between each iteration')
        args = parser.parse_args()

        job = piqueue.Job(job_name, clean_dict(args))
        session.add(job)
        session.commit()

        return '', 200

class QueueList(Resource):
    def get(self):
        queue = session.query(piqueue.Job).order_by(piqueue.Job.id)
        return job_schemas.jsonify(queue)

    def delete(self):
        pass
        # TODO: delete...


api.add_resource(Queue, '/queue/<string:job_name>')
api.add_resource(QueueList, '/queue')

if __name__ == '__main__':
    app.run(debug=True)
