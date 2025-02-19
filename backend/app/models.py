from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"


engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()


class PersonData(Base):
    __tablename__ = "person_data"
    
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime(timezone=True), default=datetime.now())
    num_bboxes = Column(Integer)
    result_image_file_path = Column(String)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)