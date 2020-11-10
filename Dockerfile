FROM python:3.10.0a2-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY /app .
CMD ["python", "index.py"]