from flask import request, jsonify, abort
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .schema import EmployeeSchema, SimpleEmployeeSchema
from .service import EmployeeService

api = Namespace("Employee", description='API for employees (CRUD)')


@api.route("/")
@api.response(500, 'Internal Server Error')
@api.response(400, 'Bad Request')
class EmployeeResource(Resource):
    """Employees"""

    @responds(schema=EmployeeSchema(many=True))
    @api.response(200, 'Success')
    def get(self):
        """Get all employees"""

        return EmployeeService.get_all()

    @accepts(schema=EmployeeSchema, api=api)
    @responds(schema=EmployeeSchema(), status_code=201)
    @api.response(201, 'Success')
    def post(self):
        """Create employee"""

        return EmployeeService.create(request.parsed_obj)


@api.route("/<int:id>")
@api.param("id", "Employee id")
@api.response(200, 'Success')
@api.response(500, 'Internal Server Error')
@api.response(400, 'Bad Request')
@api.response(404, 'Employee not found')
class EmployeeIdResource(Resource):
    @responds(schema=EmployeeSchema())
    def get(self, id: int):
        """Get employee"""

        employee = EmployeeService.get_by_id(id)
        if not employee:
            abort(404, f"Employee with id {id} not found")
        return employee

    def delete(self, id: int):
        """Delete employee"""

        deleted_id = EmployeeService.delete_by_id(id)
        if not deleted_id:
            abort(404, f"Employee with id {id} not found")
        return jsonify(dict(status="Success", id=deleted_id))

    @accepts(schema=SimpleEmployeeSchema, api=api)
    @responds(schema=EmployeeSchema())
    def put(self, id: int):
        """Update employee"""

        employee = EmployeeService.get_by_id(id)
        if not employee:
            abort(404, f"Employee with id {id} not found")
        params = request.parsed_obj
        name = params['name']
        if EmployeeService.employee_exists(name, [employee.id]):
            return abort(400, f'Employee with name {name} already exists')
        updated_employee = EmployeeService.update(employee, params)
        return updated_employee
