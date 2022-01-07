import flask
from flask import Flask, render_template, Response
import time
import psutil


app = Flask(__name__)


def fun():
    x =  psutil.cpu_percent(1)
    y =  psutil.virtual_memory()[2]
    return x, y;


@app.route('/content')
def content():
    def inner():
        while True:
            cpu, mem = fun()
            yield 'CPU usage: ' +  str(cpu) + '--------' + ' Memory usage: ' + str(mem) + '<br/>\n'
            time.sleep(10)
    return Response(inner(), mimetype='text/html')

@app.route('/')
def index():
    return render_template('index.html.jinja')


app.run(debug=True)
