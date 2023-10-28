from sqlalchemy.orm import Session


def create_handler(db: Session, object: any):

    db.add(object)
    db.commit()
    db.flush(object)
