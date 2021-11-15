1. Overview of the Python flask application auth.py

   1.1 The Python flask API accepts the following endpoints for the HTTP GET method:
     
        1.1.1 /login: Return a JWT token if login verification is successful
     
        1.1.2 /signup:  Return a JWT token if signup is successful
    
   1.2 The Error Handling 
     
        1.2.1 For the endpoints stated in 1.1.1, a JSON object of the error message "Bad username or password" will be returned when there is no any matching login record is found
     
        1.2.2 When signup process is failed, the error message "Error" will be prompted.	

2. Instructions(Under Windows CMD/Linux Terminal):

      2.1 To start the MongoDB and account_service docker containers inside the folder:
      
         docker-compose up
			
3. Testing Command(Under Windows CMD/Linux Terminal):
	
	curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"wonderpp\",\"password\":\"123456789\"}" http://localhost:80/account_api/login
	
	curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:80/account_api/signup 
        
	curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:80/account_api/login
	  
4. References:

   https://www.maxlist.xyz/2020/05/01/flask-jwt-extended/
