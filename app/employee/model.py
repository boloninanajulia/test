from datetime import date

from sqlalchemy import Integer, Column, String, Date, ForeignKey

from app import db
from app.department.model import Department


class Employee(db.Model):
    """A Employee"""

    __tablename__ = "employees"

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey(Department.id), nullable=False)
    department = db.relationship("Department", backref="employees")
    date_joined = Column(Date, nullable=False, default=date.today())

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id

    def __repr__(self):
        return "<Employee(name={self.name!r})>".format(self=self)

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
