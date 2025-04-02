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
