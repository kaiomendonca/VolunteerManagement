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
### List Volunteers with Filters

**Endpoint:**
GET /volunteers

**Query Parameters (optional):**
- desired_position
- availability
- status

**Example Request:**
GET /volunteers?desired_position=backend&availability=weekends

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "João Silva",
    "email": "joao@example.com",
    "phone": "21999999999",
    "desired_position": "backend",
    "availability": "weekends",
    "status": "active",
    "created_at": "2026-03-26T15:00:00"
  }
]
```

### Get Volunteer by ID

**Endpoint:**
GET /volunteers/{id}

**Example Request:**
GET /volunteers/1

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@example.com",
  "phone": "21999999999",
  "desired_position": "backend",
  "availability": "weekends",
  "status": "active",
  "created_at": "2026-03-26T15:00:00"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Volunteer not found"
}
```

### Update Volunteer

**Endpoint:**
PATCH /volunteers/{id}

**Request Body (partial update allowed):**
```json
{
  "phone": "21988888888",
  "availability": "weekdays"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@example.com",
  "phone": "21988888888",
  "desired_position": "backend",
  "availability": "weekdays",
  "status": "active",
  "created_at": "2026-03-26T15:00:00"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Volunteer not found"
}
```

### Soft Delete (Inactivate Volunteer)

**Endpoint:**
DELETE /volunteers/{id}

**Behavior:**
Marks the volunteer as inactive instead of deleting from database.

**Response (200 OK):**
```json
{
  "message": "Volunteer inactivated successfully"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Volunteer not found"
}
```

## Important technical decisions

### Technical Decisions

**Use of Poetry**

At the beginning of the project, I faced some difficulty using Poetry due to a lack of familiarity with the tool. To overcome this, I studied the official documentation, performed several tests, and gradually adapted to its workflow.

By the end of the process, I was able to use Poetry effectively for dependency management and project organization, which contributed to a cleaner and more structured development environment.

### Choice of Software Architecture

One of the most important decisions in this project was the choice of software architecture.

I opted for an approach that promotes separation of concerns, aiming to keep the codebase scalable, readable, and easy to maintain. This structure makes it easier to evolve the application over time, add new features, and maintain consistency across different layers of the system.

### Use of Docker

Instead of using an in-memory approach (such as lists) for data storage, I chose to use Docker as a way to demonstrate practical knowledge of containerization and real-world application setup.

This decision was initially challenging, especially when integrating Docker with Poetry, but it provided a more realistic development environment.

The application was structured using three containers:

- API (Volunteers): Responsible for handling requests and business logic
- PostgreSQL: Database used for persistent data storage
- PgAdmin: Graphical interface for database management and queries

Using Docker helped reduce some manual setup steps, although Poetry was still used for dependency management and local development workflows.


### Focus on Code Readability

Another important decision was to prioritize code readability across the entire project.

This includes:

- Clear and descriptive variable names
- Well-defined schemas and models
- Organized structure of classes and modules

The goal was to make the application easy to understand and use, even for developers with only basic familiarity with the technologies involved.

### Documentation Strategy

Special attention was given to the construction of the README.

The goal was to keep the documentation concise and objective, allowing anyone to understand and start using the application within a few minutes, without unnecessary complexity.





