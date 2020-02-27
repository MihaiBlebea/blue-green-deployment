# FROM frankwolf/rpi-python3
FROM python:3


WORKDIR /app

RUN pip3 install flask

RUN pip3 install requests

COPY main.py /app/main.py

EXPOSE 8080

CMD [ "python3", "./main.py", "8080" ]