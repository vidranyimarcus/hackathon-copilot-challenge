# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a fully functional API with endpoints for creating, reading, updating, and deleting resources, while understanding HTTP methods, status codes, and data validation.

## 📝 Tasks

### 🛠️	Create a Task Management API

#### Description
Build a REST API for managing tasks with FastAPI. The API should support full CRUD (Create, Read, Update, Delete) operations for task items.

#### Requirements
Completed program should:

- Create a FastAPI application with proper routing
- Implement GET endpoint to retrieve all tasks
- Implement GET endpoint to retrieve a single task by ID
- Implement POST endpoint to create new tasks with validation
- Implement PUT endpoint to update existing tasks
- Implement DELETE endpoint to remove tasks
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include interactive API documentation (automatic with FastAPI)


### 🛠️	Add Data Validation and Error Handling

#### Description
Enhance your API with proper input validation and error handling to make it robust and user-friendly.

#### Requirements
Completed program should:

- Validate task data using Pydantic (e.g., required fields, data types)
- Handle invalid task IDs with 404 Not Found responses
- Return meaningful error messages for validation failures
- Use appropriate status codes for different scenarios
- Test all endpoints using the interactive documentation at `/docs`
