import numpy as np
import {{ group}}_repository as {{group_initial}}r
import base_service as bs
{% for table in tables %}
from {{table.class}} import {{table.class}}Model
{% endfor %}

{% for table in tables %}
#--------------------
# {{table.name}}
#--------------------

@bs.repository_call
def get_{{table.name}}s ():
    return {{group_initial}}r.get_{{table.name}}s()

# @bs.repository_call
# def get_{{table.name}}_by_{{group}}_id ({{group}}_id):
#     return {{group_initial}}r.get_{{table.name}}_by_{{group}}_id({{group}}_id)

@bs.repository_call_single_row
def get_{{table.name}}_by_id (id):
    return {{group_initial}}r.get_{{table.name}}_by_id(id)

def upsert_{{table.name}} ( {{table.name}}:{{table.class}}Model):
    df = {{group_initial}}r.upsert_{{table.name}}({{table.name}})
    id = np.int64(df['{{table.column_details[0].column_name}}'].values[0]).item()
    return get_{{table.name}}_by_id(id)

{% endfor %}