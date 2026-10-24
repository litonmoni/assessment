from student_repository import StudentRepository
from sqlalchemy.orm import Session
from schema import StudentUpdateRequest, StudentCreateRequet, StudentResponse
from fastapi import HTTPException
from student import Student


class StudentService:
    def __init__(self):
        self.repository = StudentRepository()

    def map_response(self, student: Student):
        summary = (student.english_marks+student.mathematics_marks+student.science_marks)/3
        status = ''
        if summary>=80:
            status="Excelent"
        elif summary >=60:
            status="Pass"
        else:
            status = "Need Improvement"
        return StudentResponse(id= student.student_id, roll=student.roll, name= student.name, result=status, english_marks= student.english_marks,
                               science_marks=student.science_marks, mathematics_marks=student.mathematics_marks)
        

    def get_student_by_roll(self, db: Session, roll: str):
        student =  self.repository.get_student_by_roll(db, roll)
        return self.map_response(student)

    def update_student(self, db: Session, update_student: StudentUpdateRequest, roll: str):
        student = self.repository.get_student_by_roll(db, roll)
        if not student:
            raise HTTPException(status_code=404, detail="Item not found")
        
        
        student.english_marks = update_student.english_marks
        student.mathematics_marks = update_student.mathematics_marks   
        student.science_marks = update_student.science_marks
        return self.repository.update_student(db, student)

    def create_student(self, db: Session, student_payload : StudentCreateRequet):
        student = Student(name = student_payload.name,
                            english_marks = student_payload.english_marks,
                            mathematics_marks = student_payload.mathematics_marks,
                            science_marks = student_payload.science_marks,
                            roll = student_payload.roll,
)
        return self.repository.create_student(db,student)

    def get_all_students(self, db: Session):
        students = self.repository.get_all(db=db)
        student_list=[]
        for student in students:
            student_list.append(self.map_response(student))
        return student_list 

    def delete_student(self, roll:str, db:Session):
        self.repository.delete_student(db, roll)


