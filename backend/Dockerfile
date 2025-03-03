FROM python:3.11-slim-bullseye
USER 0
ENV PYTHONUNBUFFERED=True
RUN apt-get update -y 
# needed for pycairo pip package
RUN apt-get install -y libcairo2-dev pkg-config python3-dev gcc ffmpeg libsm6 libxext6 poppler-utils tesseract-ocr
#### chrome driver - start ######################################


RUN mkdir -p /app/
ENV BRANDING_APP=/app
# Define the version of Poetry to install (default is 1.7.0)
# Copy the requirements.txt first to install dependencies before copying the app (for efficient caching)
# COPY requirements.txt /app/
COPY . /app/
# Copy AWS credentials to the container (optional and for development purposes only)
COPY config /root/.aws/config
# Install the Python dependencies
WORKDIR /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code




# Expose the port FastAPI will run on (default FastAPI port is 8000)
EXPOSE 8000

# Set the command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
