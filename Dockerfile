FROM python:3

WORKDIR /app
ADD . /app
COPY requirements.txt ./
RUN pip install pipenv
RUN pipenv install --no-cache-dir -r requirements.txt
RUN pipenv lock
EXPOSE 80

CMD [ "python", "app.py" ]