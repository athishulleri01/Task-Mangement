# Task Management API

This project provides a Task Management API built using Django and Django REST Framework (DRF). It enables users to create tasks, assign tasks to multiple users, and retrieve tasks assigned to specific users.

## 🚀 Features
- Create new tasks with a name and description
- Assign tasks to one or multiple users
- Retrieve tasks assigned to a specific user
- Secure authentication with JWT-based authentication

## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL (or any other database)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/athishulleri01/Task-Mangement.git
cd Task-Mangement
```

### 3️⃣ Install Docker in your System

### 4️⃣ Set Up Environment Variables
Create a **.env** file in the root directory:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=postgres://username:password@localhost:5432/db_name
```
### 5️⃣ Run docker compose file
```bash
docker compose -f local.yml up --build -d --remove-orphans
```



### 6️⃣ Apply Migrations & Create Superuser
```bash
docker compose -f local.yml run --rm api python manage.py makemigrations
docker compose -f local.yml run --rm api python manage.py createsuperuser
```

### 7️⃣ Down the Docker
```bash
docker compose -f local.yml down
```

## 🔥 API Endpoints

### 🟢 **Obtain Access & Refresh Tokens (Login)**
#### **POST** `/api/v1/auth/token/`
**Request:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```
**Response:**
```json
{
  "message": "Login Successful."
}
```
---

### 🟢 **Refresh Access Token**
#### **POST** `/api/v1/auth/token/refresh/`
(No body required, uses refresh token from cookies)
**Response:**
```json
{
  "message": "Access tokens refreshed successfully"
}
```

---

### 🟢 **Social Authentication (Google, Facebook, etc.)**
#### **POST** `/api/v1/auth/social-auth/`
**Request:** *(Example: Google OAuth2)*
```json
{
  "provider": "google",
  "access_token": "your_google_access_token"
}
```
**Response:**
```json
{
  "message": "You are logged in successfully."
}
```

---

### 🟢 **Logout**
#### **POST** `/api/v1/auth/logout/`
**Response:**
```json
{
  "message": "Logged out successfully."
}
```


### 🟢 **Create a Task**
#### **POST** `/api/v1/tasks/`
**Request:**
```json
{
  "name": "Task 1",
  "description": "This is a sample task."
}
```
**Response:**
```json
{
  "id": 1,
  "name": "Task 1",
  "description": "This is a sample task.",
  "created_at": "2025-03-26T12:00:00Z"
}
```

---

### 🟢 **Assign a Task to Users**
#### **POST** `/api/v1/tasks/{task_id}/assign/`
**Request:**
```json
{
  "user_ids": [1, 2, 3]
}
```
**Response:**
```json
{
  "message": "Task assigned successfully!"
}
```
---

### 🟢 ** Fetches all tasks assigned to a particular user **
#### **GET** `/api/v1/tasks/user-tasks/{user_id}/`
**Response:**
```json
[
  {
    "id": 1,
    "name": "Task 1",
    "description": "This is a sample task.",
    "task_type": "Development",
    "created_at": "2024-03-26T12:00:00Z",
    "completed_at": null,
    "status": "pending",
    "assigned_users": [
      {
        "id": 2,
        "name": "John Doe",
        "email": "johndoe@example.com"
      }
    ]
  },
  {
    "id": 2,
    "name": "Task 2",
    "description": "This is another sample task.",
    "task_type": "Testing",
    "created_at": "2024-03-25T15:30:00Z",
    "completed_at": "2024-03-26T10:00:00Z",
    "status": "completed",
    "assigned_users": [
      {
        "id": 2,
        "name": "John Doe",
        "email": "johndoe@example.com"
      },
      {
        "id": 3,
        "name": "Jane Smith",
        "email": "janesmith@example.com"
      }
    ]
  }
]

```
