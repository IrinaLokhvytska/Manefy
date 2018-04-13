FROM python:3

WORKDIR /app
ADD . /app
RUN pip install pipenv
RUN pipenv install
EXPOSE 80

CMD [ "python", "manage.py" ]