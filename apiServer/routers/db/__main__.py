import code
from . import crud, models, schemas
from database import SessionLocal, engine

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    a = models
    code.interact(local=locals())