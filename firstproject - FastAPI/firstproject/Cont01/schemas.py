from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    department: str
    position: str
    salary: float

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    no: int

    class Config:
        orm_mode = True
