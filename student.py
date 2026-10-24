from student_database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__= "students"

    student_id = Column(Integer, primary_key= True)
    roll = Column(String(20), unique=True, nullable= False)
    name = Column(String(50), nullable= False)
    english_marks = Column(Integer)
    mathematics_marks = Column(Integer)
    science_marks = Column(Integer)