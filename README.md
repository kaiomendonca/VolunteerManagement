# Volunteer Management API
- The documentation will be created using the English language to ensure standardization of the reading experience.
- A REST API developed for managing volunteers, allowing registration, updates, filtered queries, and soft deletion of records. The project was built as part of a technical challenge focused on backend best practices.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Pydantic
- Poetry

## How to run

### Clone the repository
`git clone <repo-url>`

`cd repo`

### Install Poetry
- Windows:
    `pip install poetry`

- Linux:
    `curl -sSL https://install.python-poetry.org | python3 -`


### Install dependencies
`poetry install`

This already does everything automatically:

- creates/uses a virtual environment
- installs all pyproject.toml dependencies
- ensures correct versions

### Environment Variables
- Create a `.env` file
  
    There is a `.env.example` file to base the environment variables used in the project on.

### Start database with Docker and Run application
`docker compose up --build`

## EndPoints

- **Register volunteers**  
  Create a new volunteer in the system.

- **Update volunteer data**  
  Partially or fully update an existing volunteer.

- **List volunteers with filters**  
  Filter volunteers by desired position, availability, and status.

- **Get volunteer by ID**  
  Retrieve a specific volunteer by its ID.

- **Soft delete (inactivate volunteer)**  
  Marks a volunteer as inactive instead of deleting it from the database.


## Example Usage

### Create a Volunteer

**Endpoint:**
POST /volunteers

**Request Body:**
```json
{
  "name": "example",
  "email": "example404@example.com",
  "phone": "21999999999",
  "desired_position": "frontend",
  "availability": "weekends"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "example",
  "email": "example404@example.com",
  "phone": "21999999999",
  "desired_position": "frontend",
  "availability": "weekends",
  "status": "active",
  "created_at": "2026-03-26T15:00:00"
}
```








