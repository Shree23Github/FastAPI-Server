from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app=FastAPI() #Creating the instance of the FastAPI object--->FastAPI

students={
    1:{
        "name":"Shourya",
        "age":21,
        "Class":"year 2024"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None
    


# What is an endpoint--->
'''
for example--->
1. in a URL:  localhost/delete-user
delete-user is an endpoint
2. url---> localhost/create-user
create-user is an endpoint
3. There are different types of endpoints--->
'''
# amazon.com/create-user
'''
1. GET    -  GET/RETURN/SHOW AN INFORMATION
2. POST   -  CREATE SOMETHING NEW
3. PUT    -  UPDATE AN INFORMATION
4. DELETE -  DELETE SOMETHING
'''
# To create a new API--->
@app.get("/")
#We can put the domain name of any website created by us--->
def index():
    return {"name": "First Date"}
# Path Parameters
'''
In Path Parameters --->
We need to add whatever the parameter wants to collect in the URL in the endpoints.
'''
@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(...,description="The id of the student you want to view.",gt=0,lt=3)):
    # gt=n: greater than n;lt=x lesser than x and if any value not greater than n is given then it shows error...
    #if any value b/w n and x is written then,if doesn't have data corresponding to it then it show "Internal Server Error"
    # initialising the student id as "int"
    return students[student_id]
# student_id is the key of the dictionary using which the values of the particluar student_id is returned

    
#The statement inside the {} of the return statement is printed or basically returned on running--->

# python -m uvicorn main:app --reload--->To run the server
'''
Meaning of the above command line by line--->
1. python: This command invokes the Python interpreter to execute the following script or module.
2. -m uvicorn : (a)tells Python to run the 'uvicorn' module as a script.
                (b)"uvicorn" is an ASGI i.e.Asynchronous Server Gateway Interface,used for running asynchronous web
                   application in Python
3. main:app : Here 'main'is the name of the particular Python module(usually a Python file) containing
              the FastAPI application object and 'app'is the name of the FastAPI application object within
              that module.
              FastAPI is a modern,fast(high performance),web framework for
              building APIs with Python.
4. --reload : This flag enables automatic reload.
              
'''

# Syntax--->
'''
" python -m uvicorn filename:objectname --reload "

'''

'''
Uvicorn is a web server for Python that is used with FastAPI and is optimized for asynchronous programming. 
Uvicorn is an ASGI server, which means it uses the Asynchronous Server Gateway Interface, which is a modern standard for Python asynchronous applications. 
Uvicorn is known for its high performance and user-friendly design, which makes it a good choice for running FastAPI applications.
'''

'''
The url---> http://127.0.0.1:8000 is the particular url where the server runs...
8000: is the Port number
The url prints exactly what we wanted to return as a response.
'''

'''
http://127.0.0.1:8000/docs ---> can be used to test our API without using any external service to test API...
1. Click on the website link and execute it...
2. Clicking on execute gives the whole details of it...
'''

'''
* Endpoint Parameters:
Name Parameter--->used to return a data relating to an input in the part or in the endpoint...
We have 2 input parameters--->
a. Path Parameter
b. Query Parameter
'''
'''
The three dots in Python--->
known as ellipsis--->
used to:
* show that some parts of the function can be left out.
'''
# Query Parameter--->
'''
We want to get the data by the name of the students--->
eg.
@app.get("/get-by-name?name=Shourya")
So the value passed after the question mark: passed as a Query Parameter
'''
@app.get("/get-by-name/{student_id}")
def get_Student(*,student_id:int,name: Optional[str]=None):
    print(name)
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}

'''
POST: to create a new object or new data
'''
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    # students[student_id]=student
    students.update(student_id=student_id, student=student)
    return students.values[student_id]
'''


'''
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


        
    
    
    