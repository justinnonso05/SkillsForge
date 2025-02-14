# Task Manager API

This is a Django-based Task Manager API that allows users to perform CRUD operations on tasks. The API supports user authentication using JWT tokens and provides endpoints for user signup, login, and task management.


## Features

- User authentication with JWT tokens
- CRUD operations for tasks
- Task filtering and searching
- API documentation with Swagger UI

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/justinnonso05/SkillsForge-task-manager-api
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

5. Run the development server:

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



   
## The Swagger UI Interactive Documentation
### How to use
Start the development server
 ```sh
python manage.py runserver
```

Access the swagger UI at
 ```sh
http://localhost:8000/docs/
```

Use the ```/auth/signup``` endpoint to create a new user
![image](https://github.com/user-attachments/assets/abf60d65-0a48-450e-af3e-ec10a3c3537e)
Use the execute button to execute 
![image](https://github.com/user-attachments/assets/77d47d2e-7d84-4ae1-8275-0c86e999d0c0)

Then use the ```/auth/login``` endpoint to login to the created user's account to get the access token for authorization.
![image](https://github.com/user-attachments/assets/b438a68a-2003-4669-b277-7fb450359c02)

Copy the ```access token``` generated in the response body
![image](https://github.com/user-attachments/assets/97f2d756-4669-4d40-be29-1eb8382a6544)

Paste it in the authorization section at the top section of the Swagger UI
![image](https://github.com/user-attachments/assets/71ab9d39-5347-49ae-8073-e9776f028e91)
![image](https://github.com/user-attachments/assets/94387731-53fc-4168-991d-501caa21d3ce)


After authorizing, you can now access the protected task management endpoints of the API 
![image](https://github.com/user-attachments/assets/83f5c140-f2ec-4561-af77-151de4279959)

Testing the ```/api/tasks/list``` endpoint. The fields for the query parameters are provided on the UI
![image](https://github.com/user-attachments/assets/0edb944c-470f-4c3c-b681-53ffac79558a)

Video playback
https://github.com/user-attachments/assets/16ae00bb-83dc-485e-bfa4-6383cd548e31


