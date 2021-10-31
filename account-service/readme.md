1. Overview of the Python flask application auth.py

1.1 The Python flask API accepts the following endpoints for the HTTP GET method:
     1.1.1 /login: Return a JWT token if login verification is successful
     1.1.2 /signup:  Return a JWT token if signup is successful
    
1.2 The Error Handling 
     1.2.1 Forthe endpoints stated in 1.1, a JSON object of the error message "Bad username or password" will be returned when there is no any matching login record is found
     1.2.2 When signup process is failed, the error message "Error" will be prompted.	

2. Instructions(Under Windows CMD/Linux Terminal):
      2.1 To build the docker image student_svc with the Dockerfile inside the folder:
      
         docker build . -t timelytaste_auth 

      2.2 To run the docker image timelytaste_auth under a network connected to the MongoDB docker container:
      
         docker run --rm --network project -e MONGO_USERNAME=comp3122 -e MONGO_PASSWORD=12345 -e MONGO_SERVER_HOST='mongo' -e  MONGO_SERVER_PORT='27017' -p 5000:15000 timelytaste_auth
			
3. Testing Command(Under Windows CMD/Linux Terminal):
	
          curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"wonderpp\",\"password\":\"123456789\"}" http://localhost:5000/login
	  
	  curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:5000/signup 
	  
	  curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"jackytang\",\"password\":\"1234567890\"}"  http://localhost:5000/login
	  
4. References:

   https://www.maxlist.xyz/2020/05/01/flask-jwt-extended/
