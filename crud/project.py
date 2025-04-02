from sqlalchemy.orm import Session
from models import project as models
from schemas import project as schemas

def create_project(db: Session, project: schemas.ProjectCreate) -> models.Project:
    new_project = models.Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def get_project(db: Session, project_id: int) -> models.Project:
    return db.query(models.Project).filter(models.Project.id == project_id).first()
