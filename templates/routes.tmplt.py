import os
import sys
from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

rootDir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
for subdir in ['common', 'database', 'clients']:
    sys.path.append( os.path.join(rootDir, subdir))

app = FastAPI()

import {{ group}}_service as {{group_initial}}s
{% for table in tables %}
#-- {{ table.class }}
from {{ table.class}} import {{ table.class}}
@app.get('/{{ group }}/{{ '_'.join(table.name.split('_')[1:]) }}')
def get_{{table.name}} ():
    return {{group_initial}}s.get_{{table.name}}()

@app.get('/{{ group }}/{{ '{' }}{{group}}_id}/{{ '_'.join(table.name.split('_')[1:]) }}')
def get_{{table.name}}_by_{{group}}_id ({{group}}_id):
    return {{group_initial}}s.get_{{table.name}}_by_{{group}}_id({{group}}_id)

@app.get('/{{ group }}/{{ '_'.join(table.name.split('_')[1:]) }}/{id}')
def get_{{table.name}}_by_id (id):
    return {{group_initial}}s.get_{{table.name}}_by_id(id)

@app.post('/{{ group }}/{{ '_'.join(table.name.split('_')[1:]) }}')
def post_{{table.name}} ( {{table.name}}:{{table.class}}):
    return {{group_initial}}s.upsert_{{table.name}}({{table.name}})

{% endfor %}