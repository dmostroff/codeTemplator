import {{ group}}_repository as {{group_initial}}r
import base_service as bs
{% for table in tables %}
#--------------------
# {{table.name}}
#--------------------
from {{table.class}} import {{table.class}}

@bs.repository_call
def get_{{table.name}} ():
    return {{group_initial}}r.get_{{table.name}}()

@bs.repository_call
def get_{{table.name}}_by_{{group}}_id ({{group}}_id):
    return {{group_initial}}r.get_{{table.name}}_by_{{group}}_id({{group}}_id)

@bs.repository_call
def get_{{table.name}}_by_id (id):
    return {{group_initial}}r.get_{{table.name}}_by_id(id)

@bs.repository_call
def post_{{table.name}} ( {{table.name}}:{{table.class}}):
    return {{group_initial}}r.upsert_{{table.name}}({{table.name}})

@bs.repository_call
def put_{{table.name}} ({{table.name}}:{{table.class}}):
    return {{group_initial}}r.insert_{{table.name}}({{table.name}})

{% endfor %}