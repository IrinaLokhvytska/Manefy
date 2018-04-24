FROM python:3

USER monefy
WORKDIR /app
ADD . /app
RUN pip install pipenv
RUN pipenv install --dev
EXPOSE 80
CMD [ "python", "app.py" ]
