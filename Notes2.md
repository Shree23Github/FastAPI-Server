--reload: Automatically starts the server
# If we have the same API request with the same path,the FastAPI goes down the code and searches for the first match with respect to the API request parameters...

# And hence,the order does matter when hitting the same paths in an URL...since,the first path that matches the API request runs first.

Eg. request Get method url: "/" made then it searches for the first match with respect to the API request parameters and returns the first match.

Not only send data in the body within a POSTMAN request but also extract data and send it right back to the user...

# Create new Post,save them in the database and anytime user wants to retrieve the post we fetch it from the database.

* Why do we need a Schema?
1. Its difficult to get all the values from the body
2. The client can send whatever data they want.
3. The data isn't getting validated
4. We ultimately want to force the client to send data in a schema that we expect