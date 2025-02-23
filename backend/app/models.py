from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

DATABASE_URL = "postgresql://user:password@db:5432/mydb"


engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()


class PersonData(Base):
    __tablename__ = "person_data"
    
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime(timezone=True))
    num_bboxes = Column(Integer)
    result_image_file_path = Column(String)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)