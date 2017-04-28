import json
import datetime
import importlib
import sqlalchemy
from sqlalchemy.types import TypeDecorator
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'sqlite:///database/queue.db'
engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def create_database():
    Base.metadata.create_all(engine)

class TextPickleType(TypeDecorator):
    SIZE = 4096
    impl = Text(SIZE)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Job(Base):
    __tablename__ = 'queue'
    id = Column(Integer, primary_key=True)
    job_name = Column(String(80))
    options = Column(TextPickleType())
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, job_name, options):
        self.job_name = job_name
        self.options = options

    def module_name(self):
        return "pijobs.%sjob" % (job.job_name)

    def class_name(self):
        return "%sJob" % (self.job_name.capitalize())

    def job_instance(self):
        module = importlib.import_module(self.module_name())
        klass = getattr(module, self.class_name())
        return klass(self.options)

    def __repr__(self):
        return "<Job(id='%r', job_name='%r'>" % (self.id, self.job_name)

