from flask import Flask, render_template
import os
import sys

rootDir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
for subdir in ['common', 'templator']:
    sys.path.append( os.path.join(rootDir, subdir))

import templator_service as ts

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hell():
    return render_template('hello.tmplt.html')

@app.route('/tables/<prefix>')
def tables_by_prefix(prefix):
    return ts.get_tables_by_prefix( prefix)

