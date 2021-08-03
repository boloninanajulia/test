from .model import Employee
from .schema import EmployeeSchema

BASE_ROUTE = "employees"


def register_routes(api, app, root="api"):
    from .controller import api as employee_api

    api.add_namespace(employee_api, path=f"/{root}/{BASE_ROUTE}")