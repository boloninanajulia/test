from flask import request, jsonify, abort
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .schema import DepartmentSchema, SimpleDepartmentSchema
from .service import DepartmentService

api = Namespace("Department", description='API for departments (CRUD)')


@api.route("/")
@api.response(500, 'Internal Server Error')
@api.response(400, 'Bad Request')
class DepartmentResource(Resource):
    """Departments"""

    @responds(schema=DepartmentSchema(many=True))
    @api.response(200, 'Success')
    def get(self):
        """Get all departments"""

        return DepartmentService.get_all()

    @accepts(schema=DepartmentSchema, api=api)
    @responds(schema=DepartmentSchema(), status_code=201)
    @api.response(201, 'Success')
    def post(self):
        """Create department"""

        return DepartmentService.create(request.parsed_obj)


@api.route("/<int:id>")
@api.param("id", "Department id")
@api.response(200, 'Success')
@api.response(500, 'Internal Server Error')
@api.response(400, 'Bad Request')
@api.response(404, 'Employee not found')
class DepartmentIdResource(Resource):
    @responds(schema=DepartmentSchema())
    def get(self, id: int):
        """Get department"""

        department =  DepartmentService.get_by_id(id)
        if not department:
            abort(404, f"Department with id {id} not found")
        return department

    def delete(self, id: int):
        """Delete department"""

        deleted_id = DepartmentService.delete_by_id(id)
        if not deleted_id:
            abort(404, f"Department with id {id} not found")
        return jsonify(dict(status="Success", id=deleted_id))

    @accepts(schema=SimpleDepartmentSchema, api=api)
    @responds(schema=DepartmentSchema())
    def put(self, id: int):
        """Update department"""

        department = DepartmentService.get_by_id(id)
        if not department:
            abort(404, f"Department with id {id} not found")
        params = request.parsed_obj
        name = params['name']
        if DepartmentService.exists(name, [department.id]):
            return abort(400, f'Employee with name {name} already exists')
        updated_department = DepartmentService.update(department, params)
        return updated_department
