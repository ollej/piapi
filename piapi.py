from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.types import TypeDecorator
from flask_marshmallow import Marshmallow
import datetime
import json

# TODO: Return JSON on failure
# TODO: Refactor brightness/rotate params
# TODO: One resource class that refers parameter parsing, job creation and job handling
# TODO: Ensure job_name is a proper job

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/queue.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class TextPickleType(TypeDecorator):
    SIZE = 4096
    impl = sqlalchemy.Text(SIZE)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Job(db.Model):
    __tablename__ = 'queue'
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(80))
    options = db.Column(TextPickleType())
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, job_name, options):
        self.job_name = job_name
        self.options = options

    def __repr__(self):
        return '<Job %r>' % self.job_name

class JobSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'job_name', 'date_created', 'options')

job_schema = JobSchema()
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

        job = Job(job_name, clean_dict(args))
        db.session.add(job)
        db.session.commit()

        return '', 200

class QueueList(Resource):
    def get(self):
        queue = Job.query.all()
        return job_schemas.jsonify(queue)

    def delete(self):
        pass
        # TODO: delete...


api.add_resource(Queue, '/queue/<string:job_name>')
api.add_resource(QueueList, '/queue')

if __name__ == '__main__':
    app.run(debug=True)
