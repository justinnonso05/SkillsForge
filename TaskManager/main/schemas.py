''' These schemas are used to better structure the API documentations on the Swagger UI'''

from drf_spectacular.utils import extend_schema, OpenApiParameter

# User Signup Schema
signup_schema = extend_schema(
    summary="User Signup",
    description="Register a new user with username and password.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "password": {"type": "string"},
            },
        }
    },
    responses={
        201: {"type": "object", "properties": {"message": {"type": "string"}}},
        400: {"type": "object", "properties": {"error": {"type": "string"}}},
    },
)

# User Login Schema
login_schema = extend_schema(
    summary="User Login",
    description="Login an existing user and generate access and refresh tokens.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "password": {"type": "string"},
            },
        }
    },
    responses={
        200: {
            "type": "object",
            "properties": {
                "token": {"type": "string"},
                "refresh": {"type": "string"},
                "user": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "username": {"type": "string"}
                    }
                }
            }
        },
        401: {"type": "object", "properties": {"error": {"type": "string"}}},
    },
)

# Task List Schema
task_list_schema = extend_schema(
    summary="List Tasks",
    description="Retrieve a list of all Tasks of the user",
    parameters=[
        OpenApiParameter(name="category", type=str, description="Filter tasks by category", required=False),
        OpenApiParameter(name="search", type=str, description="Search for a task with a keyword", required=False),
        OpenApiParameter(name='page', description='Page number', required=False, type=int),
        OpenApiParameter(name='page_size', description='Number of tasks per page', required=False, type=int)
    ],
)

# Task overdue Schema
task_overdue_schema = extend_schema(
    summary="List overdue Tasks",
    description="Retrieve a list of all overue Tasks of the user.",
    parameters=[
        OpenApiParameter(name="category", type=str, description="Filter tasks by category", required=False),
        OpenApiParameter(name="search", type=str, description="Search for a task with a keyword", required=False),
        OpenApiParameter(name='page', description='Page number', required=False, type=int),
        OpenApiParameter(name='page_size', description='Number of tasks per page', required=False, type=int)
    ],
)

# Task Create Schema
task_create_schema = extend_schema(
    summary="Create a Task",
    description="Create a new Task by providing necessary details.",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "category": {"type": "string"},
                "due_date": {
                    "type": "string",
                    "format": "date-time",
                    "example": "2025-02-15T14:30:00Z"
                },
            },
        }
    },
)

# Task Retrieve Schema
task_retrieve_schema = extend_schema(
    summary="Retrieve a Task",
    description="Get details of a specific task by its ID.",
)

# Task Update Schema
task_update_schema = extend_schema(
    summary="Partially Update a Task",
    description="Update specific fields of a task without replacing the entire object.",
)

# Task Delete Schema
task_delete_schema = extend_schema(
    summary="Delete a Task",
    description="Remove a specific task from the system permanently.",
)
