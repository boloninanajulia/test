from app import db
from .model import Department


class DepartmentService:
    @staticmethod
    def get_all():
        return Department.query.all()

    @staticmethod
    def get_by_id(department_id: int):
        return Department.query.get(department_id)

    @staticmethod
    def update(department: Department, data):
        if not department:
            return None
        department.update(data)
        db.session.commit()
        return department

    @staticmethod
    def delete_by_id(department_id: int):
        department = Department.query.filter(Department.id == department_id).first()
        if not department:
            return None
        db.session.delete(department)
        db.session.commit()
        return department_id

    @staticmethod
    def exists(name, exclude=None):
        return Department.query.filter(Department.name == name, ~Department.id.in_(exclude or [])).first() is not None

    @staticmethod
    def create(new_attrs):
        new_department = Department(name=new_attrs["name"])
        db.session.add(new_department)
        db.session.commit()

        return new_department
