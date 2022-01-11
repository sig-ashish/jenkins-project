FROM python:latest

WORKDIR /usr/src/app

ADD requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD sample.py .
RUN mkdir templates
ADD templates/index.html.jinja ./templates/

CMD [ "python3", "./sample.py" ]
