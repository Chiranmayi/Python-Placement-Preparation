# Day 3 — HTTP & FastAPI Basics

Name:Chiranmayi Sadena  
Date: 28 October 2026  
Topic: HTTP, FastAPI, Pydantic v2, Response Models, Error Handling and File Uploads

## 1. Objective

The objective of this assignment is to understand HTTP methods and status codes, build a REST-style API using FastAPI, validate incoming data using Pydantic v2, handle errors, define response models, and implement a basic file upload endpoint.

## 2. HTTP Methods and Status Codes

| HTTP Method | Purpose | Use Case | Example Status Code |
|---|---|---|---|
| GET | Retrieve data | Retrieve an item by ID | 200 OK |
| POST | Create or submit data | Create a new item | 201 Created |
| PUT | Replace a resource representation | Replace item details | 200 OK |
| PATCH | Partially update a resource | Update only an item's price | 200 OK |
| DELETE | Delete a resource | Delete an item | 204 No Content |

### Common HTTP Status Codes

- 200 OK: The request succeeded.
- 201 Created: A new resource was created.
- 204 No Content: The request succeeded without a response body.
- 400 Bad Request:The request is invalid.
- 401 Unauthorized: Authentication is missing or invalid.
- 403 Forbidden: The user does not have permission.
- 404 Not Found: The requested resource does not exist.
- 409 Conflict:The request conflicts with the current resource state.
- 422 Unprocessable Content: Request validation failed.
- 500 Internal Server Error: An unexpected server error occurred.

## 3. Project Structure

text
Day-3-HTTP-FastAPI/
├── main.py
├── requirements.txt
└── README.md


## 4. Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic v2
- Swagger UI
- Git and GitHub

## 5. FastAPI Endpoints

| Method | Endpoint | Description | Expected Status |
|---|---|---|---|
| GET | `/` | Checks whether the API is running | 200 |
| POST | `/items` | Creates a new item | 201 |
| GET | `/items/{item_id}` | Retrieves an item by ID | 200 |
| GET | `/items?limit=5` | Retrieves a limited list of items | 200 |
| POST | `/upload` | Accepts a file and returns its metadata | 200 |

## 6. Path Parameters and Query Parameters

### Path Parameter

Example:

text
GET /items/1


The value `1` is the item ID. The endpoint uses it to retrieve a specific item.

### Query Parameter

Example:

text
GET /items?limit=5


The parameter `limit=5` requests up to five items.

The API validates the limit to ensure it is between 1 and 100.

## 7. Pydantic Request Model and Validation

The `ItemCreate` model validates the data sent to the API.

Validation rules:

- The item name must be a string.
- The item name must contain between 1 and 100 characters.
- A name containing only whitespace is rejected.
- The price must be greater than zero.

Example valid request:
json
{
  "name": "Notebook",
  "price": 50
}


Example invalid request:

json
{
  "name": "Pen",
  "price": 0
}


Invalid request data produces a `422 Unprocessable Content` response by default.

## 8. Response Models and Error Handling

The `ItemResponse` Pydantic model defines the response fields:

- `id`
- `name`
- `price`

Using `response_model` documents the response structure and helps prevent accidental exposure of fields outside the public schema.

The API uses `HTTPException` to return deliberate errors.

Example:

python
raise HTTPException(
    status_code=404,
    detail="Item not found"
)


When an item does not exist, the API returns `404 Not Found`.

## 9. File Upload Endpoint

The application implements a basic file upload endpoint using FastAPI's `UploadFile`.

The endpoint returns:

- Filename
- Declared content type
- Confirmation message

The current implementation returns file metadata only and does not save the uploaded file.

### File Upload Security Safeguards

Before using file uploads in production, I would implement:

1. Maximum file-size limits.
2. File type and content validation.
3. Server-generated filenames.
4. Protection against path traversal.
5. Secure file storage.
6. Appropriate error handling and resource limits.

## 10. Setup Instructions

### Step 1: Create and activate a virtual environment

powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1


### Step 2: Install dependencies

powershell
python -m pip install -r requirements.txt


The `requirements.txt` file contains:

text
fastapi
uvicorn
python-multipart


### Step 3: Start the application

powershell
uvicorn main:app --reload


### Step 4: Open the API documentation

Open the following URL in your browser:
text
http://127.0.0.1:8000/docs


Swagger UI provides an interactive interface for testing the endpoints.

## 11. Testing and Results

I tested the API using Swagger UI.

| Test Case | Expected Result | Result |
|---|---|---|
| GET `/` | 200 OK | Passed |
| POST `/items` with valid data | 201 Created | Passed |
| GET `/items/1` | 200 OK | Passed |
| GET `/items?limit=5` | 200 OK | Passed |
| GET `/items/999` | 404 Not Found | Passed |
| POST `/upload` with a test file | 200 OK | Passed |

All six listed test cases were marked as passed.

### Additional Validation Tests

The following cases should also be tested:

- Missing item name.
- Price equal to zero.
- Whitespace-only item name.
- Query limit greater than 100.

Expected validation response: `422 Unprocessable Content`.

## 12. Limitations

- Items are stored in an in-memory Python dictionary.
- Data is lost when the application restarts.
- The file upload endpoint returns metadata but does not save or inspect the file contents.
- Production security measures have not been fully implemented.

## 13. What I Learned

Through this assignment, I learned how HTTP requests and responses work, the differences between GET, POST, PUT, PATCH and DELETE, and how HTTP status codes communicate request outcomes.

I also learned to create API endpoints using FastAPI, use path and query parameters, validate input with Pydantic v2, define response models, handle errors with `HTTPException`, and accept file uploads using `UploadFile`.

Finally, I learned the importance of testing both valid and invalid requests and documenting security considerations before deploying an API.


# Day-3-HTTP-FastAPI
