FROM python:3.7

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

WORKDIR /app

ADD app.py app.py
ADD config.py config.py

CMD [ "python", "-u" ,"/app/app.py" ]