from pydantic import BaseModel, Field


class BaseStudent(BaseModel):
    roll: int
    name: str
    english_marks: int= Field(gt=0, le=100)
    mathematics_marks: int = Field(gt=0, le=100)
    science_marks: int= Field(gt=0, le=100)

class StudentCreateRequet(BaseStudent):
    pass

class StudentUpdateRequest(BaseModel):
    english_marks: int
    mathematics_marks: int
    science_marks: int

class StudentResponse(BaseModel):
    id: int
    roll: str
    name: str
    english_marks: int
    mathematics_marks: int
    science_marks: int
    result: str

    class Config:
        orm_mode = True 