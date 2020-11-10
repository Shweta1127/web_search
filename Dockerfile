FROM python:3.10.0a2-buster
WORKDIR /app
RUN pip3 install flask
RUN pip3 install bs4
RUN pip3 install requests
COPY /app .
CMD ["python", "index.py"]
