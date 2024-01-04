from sqlalchemy.orm.session import Session
from schemy import UserBase
from db.models import DbUser


def create_user(db: Session, request: UserBase):
    user = DbUser(

        username=request.username,
        email=request.email,
        description=request.description
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
