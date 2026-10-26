#pull the python image from docker hub.
#Use a lightweight python image
FROM python:3.14-slim

#Set the working directory insie the container
WORKDIR /app

#copy dependency list before copying aplication code.
COPY requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

#copy the application code and saved model inside /app
COPY . .

#Document the port used by the FastAPI application
EXPOSE 8000

#start the APi server when container is ready.
#0.0.0.0 allows the server to be accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

