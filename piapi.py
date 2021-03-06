from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_marshmallow import Marshmallow

from piqueue import piqueue

# TODO: Return JSON on failure
# TODO: Ensure job_name is a proper job

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)
session = piqueue.Session()

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
        parser.add_argument('matrix', help='Matrix to update all pixels', action='append')
        parser.add_argument('graph', help='Graphs to display', action='append')
        parser.add_argument('brightness', type=int, help='Set brightness level (0-255)')
        parser.add_argument('rotate', type=int, help='Rotate 180 degrees')
        parser.add_argument('sleep', type=float, help='Seconds to sleep after job')
        parser.add_argument('interval', type=float, help='Seconds to sleep between each loop iteration')
        parser.add_argument('keep', type=bool, help='Add job to end of queue after run.')
        parser.add_argument('loop', type=int, help='Loop this many iterations in the job.')
        parser.add_argument('upper', type=bool, help='Make all letters in message upper case.')
        args = parser.parse_args()

        job = piqueue.Job(job_name, clean_dict(args))
        session.add(job)
        session.commit()

        return '', 200

class QueueList(Resource):
    def get(self):
        queue = session.query(piqueue.Job).order_by(piqueue.Job.date_created)
        return job_schemas.jsonify(queue)

class Job(Resource):
    def delete(self, job_id):
        job = session.query(piqueue.Job).filter(piqueue.Job.id == job_id).first()
        if job is not None:
            session.delete(job)
            session.commit()
            return '', 200
        else:
            return '', 404


api.add_resource(Queue, '/queue/<string:job_name>')
api.add_resource(QueueList, '/queue')
api.add_resource(Job, '/job/<int:job_id>')

if __name__ == '__main__':
    app.run(debug=True)
