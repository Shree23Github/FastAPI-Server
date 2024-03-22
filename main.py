from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app=FastAPI() #Creating the instance of the FastAPI object--->FastAPI

# Students is a dictornary which contains the data of the students
# The key is the student_id and the value is the dictionary containing the data of the student

students={
    
}

# the main error that you were doing here was that you were storing the data coming from the user incorrectly into the dictornary and then returning data wasd also incorrect.

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None
    
    
# To create a new API--->
@app.get("/")
#We can put the domain name of any website created by us--->
def index():
    return {"name": "First Date"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(...,description="The id of the student you want to view.",gt=0,lt=3)):
    # gt=n: greater than n;lt=x lesser than x and if any value not greater than n is given then it shows error...
    #if any value b/w n and x is written then,if doesn't have data corresponding to it then it show "Internal Server Error"
    # initialising the student id as "int"
    return students[student_id]
# student_id is the key of the dictionary using which the values of the particluar student_id is returned

#The statement inside the {} of the return statement is printed or basically returned on running--->

# python -m uvicorn main:app --reload--->To run the server

# Syntax

@app.get("/get-by-name/{student_id}")
def get_Student(*,student_id:int,name: Optional[str]=None):
    print(name)
    for student_id in students:
        if students[student_id].name==name:
            return students[student_id]
    return {"Data":"Not Found"}

# POST: to create a new object or new data

@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    # students[student_id]=student
    students.update({student_id:student})
    
    #  return the newly created student
    print(students)
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:Student):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    if student.name!=None:
        students[student_id].name=student.name
    if student.age!=None:
        students[student_id].age=student.age
    if student.year!=None:
        students[student_id].year=student.year
    return students[student_id]


        
    
    
    