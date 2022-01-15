FROM python:latest

WORKDIR /usr/src/app

ADD requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD sample.py .

CMD [ "python", "./sample.py" ]
