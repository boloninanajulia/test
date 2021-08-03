from datetime import date

from marshmallow import fields, validate, ValidationError

from app import ma
from app.department.schema import DepartmentSchema, Department
from .model import Employee


def validate_department(value):
    if Department.query.filter(Department.id == value).first() is None:
        raise ValidationError(f"Department with id '{value}' not found.")


def validate_name(value):
    if Employee.query.filter(Employee.name == value).first() is not None:
        raise ValidationError(f"Employee with name '{value}' already exists.")


class SimpleEmployeeSchema(ma.SQLAlchemySchema):

    class Meta:
       model = Employee

    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(max=255,))
    department_id = fields.Integer(load_only=True, validate=validate_department)


class EmployeeSchema(SimpleEmployeeSchema):

    name = fields.String(required=True, validate=[validate.Length(max=255,), validate_name])
    department_id = fields.Integer(required=True, load_only=True, validate=validate_department)
    department = fields.Nested(DepartmentSchema, dump_only=True, attribute='department')
    date_joined = fields.String(dump_only=True)
