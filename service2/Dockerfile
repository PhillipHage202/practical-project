FROM python:3.7

RUN apt update
RUN apt install python3-pip
COPY . .
RUN pip3 install-r requirements.txt

EXPOSE 5001
ENTRYPOINT ["python", "app.py"]