from sqlalchemy import Integer, Column, String

from app import db


class Department(db.Model):
    """A department"""

    __tablename__ = "departments"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Department(name={self.name!r})>".format(self=self)

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
