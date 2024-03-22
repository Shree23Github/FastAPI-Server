# Fast API Development Notes

## What is an endpoint ?

- An endpoint is a specific URL that is used to perform a specific task.
- For Example

1. in a URL: `localhost/delete-user`
   `delete-user` is an endpoint
2. url: `localhost/create-user`
   `create-user` is an endpoint
3. There are different types of endpoints

## Type of Endpoints

1. `GET`: To get data from the server
2. `POST`: To send data to the server
3. `PUT`: To update data on the server
4. `DELETE`: To delete data from the server

## What are Path Parameters ?

- Path parameters are used to pass data to the server through the URL.
- In Path Parameters
  We need to add whatever the parameter wants to collect in the URL in the endpoints.
- For Example
  - `localhost/user/1`
    - Here `1` is a path parameter
    - We can use this parameter to get the user with id `1`

## Notes on uvicorn and its functioning

### Meaning of the above command line by line

1. `python`: This command invokes the Python interpreter to execute the following script or module.
2. `-m uvicorn` : (a)tells Python to run the 'uvicorn' module as a script.
   (b)"uvicorn" is an ASGI i.e.Asynchronous Server Gateway Interface,used for running asynchronous web
   application in Python
3. `main:app` : Here 'main'is the name of the particular Python module(usually a Python file) containing
   the FastAPI application object and 'app'is the name of the FastAPI application object within
   that module.
   FastAPI is a modern,fast(high performance),web framework for
   building APIs with Python.
4. `--reload` : This flag enables automatic reload.

- Current command being used to run the server

```bash
python -m uvicorn main:app --reload
```

- Uvicorn is a web server for Python that is used with FastAPI and is optimized for asynchronous programming.
- Uvicorn is an ASGI server, which means it uses the Asynchronous Server Gateway
- Interface, which is a modern standard for Python asynchronous applications.
  Uvicorn is known for its high performance and user-friendly design, which makes it a good choice for running FastAPI applications.

- The url `http://127.0.0.1:8000` is the particular url where the server runs...

- `8000`: is the Port number
  The url prints exactly what we wanted to return as a response.

- http://127.0.0.1:8000/docs can be used to test our API without using any external service to test API...

1. Click on the website link and execute it.
2. Clicking on execute gives the whole details of it.

- Endpoint Parameters:
  Name Parameter: They are used to return a data relating to an input in the part or in the endpoint.

* We have 2 input parameters:

1. Path Parameter
2. Query Parameter

The three dots in Python
known as ellipsis
used to:

- show that some parts of the function can be left out.


## Query Parameter--->


We want to get the data by the name of the students:
eg:
```python
@app.get("/get-by-name?name=Shourya")
```
So the value passed after the question mark: passed as a `Query Parameter`
