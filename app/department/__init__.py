from .model import Department
from .schema import DepartmentSchema

BASE_ROUTE = "departments"


def register_routes(api, app, root="api"):
    from .controller import api as department_api

    api.add_namespace(department_api, path=f"/{root}/{BASE_ROUTE}")
