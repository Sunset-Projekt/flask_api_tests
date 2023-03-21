from app import db
from datetime import datetime


class Task(db.Model):
      __tablename__ = "tasks"

      id = db.Column(db.Integer(), primary_key=True)
      title = db.Column(db.String(255), nullable=False, unique=False)
      description = db.Column(db.String(512), nullable=False, unique=False)
      created_on = db.Column(db.DateTime(), default=datetime.utcnow)
      done = db.Column(db.Boolean(), default=False)

      def serialize(self):
            return { 
                  "id": self.id,
                  "title": self.title,
                  "description": self.description,
                  "created_on": self.created_on, 
                  "done": self.done    
            }

      def __repr__(self):
            return "<{}:{}>".format(self.id, self.title)