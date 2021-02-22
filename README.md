# Details about Project
This a Role Based Authentiction system that retricts users to certian endpoints based on the roles of the users
There are 5 roles in this system now:
    - OWNER = 0
    - INVESTOR = 1
    - ADMIN = 2
    - WRITE = 3
    - READ_ONLY = 4
The owner has access to all endpoints, while the rest are restricted. 

# Authentication
Although when logging in a jwt token is passed, but it shouldn't be added when sending requests, as the authentication is been recieved from the cookie when sending a request. this cookis is automtically set when you log in. 

# Hosted
This API is hosted here:
https://rbas-app.herokuapp.com/

# Documentation

The documentation for this API is here:
https://documenter.getpostman.com/view/10820292/TWDXpH9