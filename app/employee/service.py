from app import db
from .model import Employee


class EmployeeService:
    @staticmethod
    def get_all():
        return Employee.query.all()

    @staticmethod
    def get_by_id(employee_id: int):
        return Employee.query.get(employee_id)

    @staticmethod
    def update(employee: Employee, data):
        if not employee:
            return None
        employee.update(data)
        db.session.commit()
        return employee

    @staticmethod
    def delete_by_id(employee_id: int):
        employee = Employee.query.filter(Employee.id == employee_id).first()
        if not employee:
            return None
        db.session.delete(employee)
        db.session.commit()
        return employee_id

    @staticmethod
    def employee_exists(name, exclude=None):
        return Employee.query.filter(Employee.name == name, ~Employee.id.in_(exclude or [])).first() is not None

    @staticmethod
    def create(new_attrs):
        new_employee = Employee(name=new_attrs["name"], department_id=new_attrs["department_id"])
        db.session.add(new_employee)
        db.session.commit()

        return new_employee
