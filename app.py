from flask import Flask, render_template
import os
import sys
from dotenv import load_dotenv

load_dotenv(verbose=True)

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


@app.route('/headers/<table_name>')
def table_headers(table_name):
    return ts.gen_headers( table_name)

@app.route('/routes/<prefix>')
def create_routes( prefix):
    retval = ts.create_routes(prefix)
    return retval

@app.route('/service/<prefix>')
def create_service( prefix):
    retval = ts.create_service(prefix)
    return retval

@app.route('/repository/<prefix>')
def create_repository( prefix):
    retval = ts.create_repository(prefix)
    return retval

@app.route('/api_js_service/<prefix>')
def create_api_js_service( prefix):
    retval = ts.create_api_js_service(prefix)
    return retval

@app.route( '/vue/<prefix>')
def create_vue_component( prefix):
    retval = ts.create_vue_component( prefix)
    return retval