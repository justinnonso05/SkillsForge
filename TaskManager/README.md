# Task Manager API

This is a Django-based Task Manager API that allows users to perform CRUD operations on tasks. The API supports user authentication using JWT tokens and provides endpoints for user signup, login, and task management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication with JWT tokens
- CRUD operations for tasks
- Task filtering and searching
- API documentation with Swagger UI

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/task-manager-api.git
    cd task-manager-api
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

To use the API, you can use tools like `curl`, `Postman`, or any other API client. Below are the available endpoints and their usage.

## API Endpoints

### User Authentication

- **Signup**: `POST /auth/signup/`
- **Login**: `POST /auth/login/`

### Task Management

- **List Tasks**: `GET /api/tasks/list`
- **Create Task**: `POST /api/tasks/create`
- **Retrieve Task**: `GET /api/tasks/<str:pk>/`
- **Update Task**: `PATCH /api/tasks/<str:pk>/update/`
- **Delete Task**: `DELETE /api/tasks/<str:pk>/delete/`

### API Documentation

- **Swagger UI**: `GET /docs/`
- **Schema**: `GET /schema/`

## Authentication

The API uses JWT tokens for authentication. To access the protected endpoints, you need to include the JWT token in the `Authorization` header of your requests.

### Example

1. **Login** to get the JWT token:

    ```sh
    curl -X POST http://localhost:8000/auth/login/ -d "username=yourusername&password=yourpassword"
    ```

2. Use the token to access protected endpoints:

    ```sh
    curl -H "Authorization: Bearer yourtoken" http://localhost:8000/api/tasks/list
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to customize this README file as per your project's requirements.