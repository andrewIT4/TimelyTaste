1. Overview of the Python flask application auth.py

   1.1 The Python flask API accepts the following endpoints for the HTTP method:
     
        1.1.1 POST /login: Return a JWT token if login verification is successful
     
        1.1.2 POST　/signup:  Return a JWT token if signup is successful
        
        1.1.3 GET /accounts: Return all accounts information if there is any account information
        
        1.1.4 GET /accounts/<username>: Return specified account information if there is any account information

        1.1.5 PUT /accounts/<username> : Return Success Message if account information was successfully updated

        1.1.6 DELETE /accounts/<username> : Return Success Message if account information was successfully deleted

   1.2 The Error Handling 
     
        1.2.1 For the endpoints stated in 1.1.1, a JSON object of the error message "Bad username or password" will be returned when there is no any matching login record is found
     
        1.2.2 When signup process is failed, the error message "Error" will be prompted.	
        
        1.2.3 For the endpoints stated in 1.1.3 and 1.1.4 , a JSON object of the error message "not found" will be prompted if no data match the requests

        1.2.4 For the endpoints stated in 1.1.5 , a JSON OBJECT of the error message "Customer data are same" if the input data is same as before

        1.2.5 For the endpoints stated in 1.1.5 , a JSON OBJECT of the error message "No such customer data " if the input username not found in database

        1.2.6 For the endpoints stated in 1.1.6 , a JSON OBJECT of the error message "No such account data " if the input username not found in database

2. Instructions(Under Windows CMD/Linux Terminal):

      2.1 To start the MongoDB and account_service docker containers inside the folder:
      
         docker-compose up
			
3. Testing Command(Under Windows CMD/Linux Terminal):
	
    curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"wonderpp\",\"password\":\"123456789\"}" http://localhost:80/account_api/login
	
    curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:80/account_api/signup 
        
    curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:80/account_api/login
  
    curl -X GET http://localhost:80/account_api/accounts

    curl -X GET http://localhost:80/account_api/accounts/admin2

    curl -X PUT -H "Content-Type: application/json" -d "{
        "credit_no": "5",
        "firstname": "admin4",
        "lastname": "admin4",
        "location": "admin5",
        "role": "admin"
    }"  
    http://localhost:80/account_api/accounts/admin2

    curl -X DELETE http://localhost:80/account_api/accounts/admin2

5. References:

   https://www.maxlist.xyz/2020/05/01/flask-jwt-extended/
