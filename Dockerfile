# Step 1: Tell Docker to start with a standard Python 3.11 environment
FROM python:3.11-slim

# Step 2: Set the working directory inside the container to /code
WORKDIR /code

# Step 3: Copy our requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Step 4: Install the Python packages listed in the requirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Step 5: Copy our actual app code into the container
COPY ./app /code/app

# Step 6: Tell Docker what command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
