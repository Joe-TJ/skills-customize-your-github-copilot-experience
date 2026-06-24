# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI and Python. In this assignment, you will create endpoints, work with request and response data, and manage simple in-memory records using standard REST patterns.

## 📝 Tasks

### 🛠️ FastAPI App Setup

#### Description
Create a FastAPI application and add basic endpoints so the server can start successfully and respond to simple requests.

#### Requirements
Completed program should:

- Create a FastAPI application object.
- Add a GET endpoint at / that returns a short welcome message.
- Add a GET endpoint at /health that returns a status response such as {"status": "ok"}.
- Run successfully with Uvicorn without syntax errors.


### 🛠️ Create and List API Resources

#### Description
Define a resource model and implement endpoints that allow a client to create new records and list all saved records.

#### Requirements
Completed program should:

- Define a Pydantic model for an API resource with at least id, title, and completed fields.
- Store records in an in-memory list.
- Add a GET endpoint at /tasks that returns all stored records.
- Add a POST endpoint at /tasks that accepts JSON input and stores a new record.


### 🛠️ Retrieve and Update Individual Resources

#### Description
Add endpoints for working with one record at a time so clients can retrieve a specific task and update its completion status.

#### Requirements
Completed program should:

- Add a GET endpoint at /tasks/{task_id} that returns one matching task.
- Return a clear error response when the requested task does not exist.
- Add a PUT endpoint at /tasks/{task_id} to update an existing task.
- Allow the completed value to be changed through the update request.