FROM python:3.8.5-alpine
ENV FLASK_APP=passageidentity/__init__.py

WORKDIR /app
COPY . /app

RUN pip3 install .
EXPOSE 5000
COPY . .
CMD [ "flask", "run" ]