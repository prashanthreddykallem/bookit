FROM python:3.11-slim-buster
WORKDIR /python-docker

COPY ./requirements.txt /python-docker
RUN pip install -r requirements.txt

COPY . .

# install dbmate
RUN apt update
RUN apt install -y curl
RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 && chmod +x /usr/local/bin/dbmate

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["/bin/bash", "-c", "chmod +x wait-for-it.sh && ./wait-for-it.sh bookit-database:3306 && dbmate up && flask run --host 0.0.0.0"]