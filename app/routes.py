def register_routes(api, app, root="api"):
    from app.department import register_routes as register_departments_routes
    from app.employee import register_routes as register_employees_routes

    # Add routes
    register_departments_routes(api, app, root)
    register_employees_routes(api, app, root)