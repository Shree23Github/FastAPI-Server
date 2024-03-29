from fastapi import Body, FastAPI
from fastapi.params import Body
app2=FastAPI()

@app2.get("/")
def root():
    return {"Message":"Another one"}

@app2.get("/posts")
def get_posts():
    return {"Data":"This is your posts"}

@app2.post("/createposts")
def create_post(payLoad:dict=Body(...)):
    print(payLoad)
    return {"new_post":f"Title{payLoad['Title']} Content:{payLoad['Content']}"}
    # return {"Message":"Successfully created post"} --->extracting data from the body of the payLoad
# Is going to extract all the fields from the Body and store it in form of dictionary in the variable "payLoad"




