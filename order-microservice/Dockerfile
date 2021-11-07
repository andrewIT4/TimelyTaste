# python 3.7 alpine is specified as parent image
FROM python:3.7-alpine
# edit the 3 environment variables
# app.py is specified to run when we run Flask
ENV FLASK_APP=order_service.py
# the host and port are set so that the REST API should listen at port 15000 at 0.0.0.0
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=15000
# get the requirements.txt file into the image
COPY requirements.txt requirements.txt
# execute the command pip install to install all dependencies listed from requirements.txt
RUN pip install -r requirements.txt
# inform Docker that the container listens on 15000 at runtime
EXPOSE 15000
# add the source code into the image
COPY . .
# when the image is executed, start flask application
CMD ["flask", "run"]
