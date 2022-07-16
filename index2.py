from urllib.parse import quote
import datetime
from sqlalchemy import create_engine, true
from sqlalchemy import Column,Integer,String,DateTime,Date,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


db_name = '/user.db'
engine = create_engine(f'sqlite://{db_name}')


class Student(Base):
    __tablename__ = "Student"
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = Session()
    print(db)
    try:
        yield db
    finally:
        db.close()


    
if __name__ =="__main__":
    db = next(get_db())

    # instance = Student(
    #     first_name = 'first_name',
    #     last_name = 'last_name',
    #     age = 20        
    # )
    # db.add(instance)
    # db.commit()

    results = db.query(Student).filter(Student.first_name == "first_name").all()
    print([e.first_name for e in results])