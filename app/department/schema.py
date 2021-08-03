from marshmallow import fields, validate, ValidationError

from app import ma
from .model import Department


def validate_name(value):
    if Department.query.filter(Department.name == value).first() is not None:
        raise ValidationError(f"Department with name '{value}' already exists.")


class SimpleDepartmentSchema(ma.SQLAlchemySchema):
    class Meta:
       model = Department

    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(max=255))


class DepartmentSchema(SimpleDepartmentSchema):
    name = fields.String(required=True, validate=[validate.Length(max=255), validate_name])
