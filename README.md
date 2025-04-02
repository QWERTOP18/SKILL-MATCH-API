# setup

```sh
docker-compose up --build -d
# --build オプションをつけることで、変更があった場合にイメージを再ビルド
docker-compose down
```

```sh
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app


docker exec -it fastapi-app /bin/sh
```

```mermaid
erDiagram
Project }o--o{ User : ""
User ||--o{ Task : ""
User ||--o{ User_Badge : ""
Badge ||--|| User_Badge : ""
Project ||--o{ Task : ""
Status ||--|| Task : ""


    Project {
        int Project_id PK
        string name
        string memo
        string document
        string reference
        date start
        date deadline
    }


    User {
        int USER_ID PK
        int Project_ID FK
        string Name
        string Email
        string reference
        int technical_skill
        int problem_solving_ability
        int communication_skill
        int leadership_and_collaboration
        int frontend_skill
        int backend_skill
        int infrastructure_skill
        int security_awareness
    }

    Task {
        int TASK_ID PK
        int USER_ID FK
        int STATUS FK
        int Project_id FK
        string title
        string memo
        int technical_skill
        int problem_solving_ability
        int communication_skill
        int security_awareness
        int leadership_and_collaboration
        int frontend_skill
        int backend_skill
        int infrastructure_skill
    }

    Status {
        int Status_id PK
        string Name
        string Color
    }

    Badge {
        int User_Badge_id PK
        string Badge
        string Name
        string Field
        string Url
    }

    User_Badge {
        int User_Badge_id PK
        int User_id FK
        int Badge FK
        int level
    }

    Question {
        int Question_ID PK
        string Text
        int technical_skill
        int problem_solving_ability
        int communication_skill
        int leadership_and_collaboration
        int frontend_skill
        int backend_skill
        int infrastructure_skill
        int security_awareness
    }
```

# API Endpoints by Resource Type

## Authentication

| Priority | Method | Endpoint      | Description |
| -------- | ------ | ------------- | ----------- |
| 3        | POST   | /auth/signin  | Sign in     |
| 3        | POST   | /auth/signout | Sign out    |
| 3        | POST   | /auth/signup  | Sign up     |

## Users

| Priority | Method | Endpoint                   | Description                                      |
| -------- | ------ | -------------------------- | ------------------------------------------------ |
| 1        | POST   | /users                     | Add a new user                                   |
| 1        | GET    | /users/{users_id}          | Get user details. Return 404 if not current_user |
| 4        | PUT    | /users/{users_id}          | Update user information (name, email)            |
| 4        | DELETE | /users/{users_id}          | Not implemented                                  |
| 3        | GET    | /users/{users_id}/projects | Get list of projects the user belongs to         |
| 5        | GET    | /users/{users_id}/tasks    | Get list of tasks linked to a user               |
| 5        | GET    | /users/badges              | Get user badges                                  |

## Projects

| Priority | Method | Endpoint                               | Description                                                     |
| -------- | ------ | -------------------------------------- | --------------------------------------------------------------- |
| 3        | POST   | /projects                              | Add a new project                                               |
| 3        | GET    | /projects/{projects_id}                | Get project details. Return 404 if not current_user's project   |
| 3        | PUT    | /projects/{projects_id}                | Update project information (development period, deadline, etc.) |
| 5        | DELETE | /users/{user_id}/projects/{project_id} | User leaves a project                                           |
| 5        | DELETE | /projects/{project_id}/users/{user_id} | Admin removes a user from project                               |
| 3        | GET    | /projects/{projects_id}/tasks          | Get list of tasks for a project                                 |

## Tasks

| Priority | Method | Endpoint                      | Description              |
| -------- | ------ | ----------------------------- | ------------------------ |
| 3        | POST   | /projects/{projects_id}/tasks | Add a task               |
| 4        | PUT    | /projects/{projects_id}/tasks | Update a task            |
| 4        | GET    | /task_status                  | Get list of all statuses |
| 3        | GET    | /task_status/{status_id}      | Get specific task status |
| 5        | POST   | /task_status                  | Create task status       |
| 4        | PUT    | /task_status/{status_id}      | Update task status       |
| 5        | DELETE | /task_status/{status_id}      | Delete task status       |

## Questions

| Priority | Method | Endpoint   | Description       |
| -------- | ------ | ---------- | ----------------- |
| 2        | GET    | /questions | Get all questions |

## Badges

| Priority | Method | Endpoint            | Description            |
| -------- | ------ | ------------------- | ---------------------- |
| 5        | GET    | /badges             | Get list of all badges |
| 5        | GET    | /badges/{badges_id} | Get badge details      |
