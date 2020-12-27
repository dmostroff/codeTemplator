import os
import templator_repository as tr
import templator_helper as th
import templator_view as tv
import vue_table_headers as vth
from flask import request

def get_tables_by_prefix( prefix):
    schema = os.getenv('SCHEMA')
    df = tr.get_tables_by_prefix(schema, prefix)
    return tv.tables_select(df.to_dict("records"))

def gen_headers( table_name):
    schema = os.getenv('SCHEMA')
    df = tr.get_column_info( schema, table_name)
    headers = vth.create_headers(df)
    th.save_render( os.getenv('TARGET_DIR'), table_name, 'js', headers)

    return tv.tables_select(df.to_dict("records"))


def create_api_resource( table_name):
    """
    docstring
    """
    target_dir = request.form.get('targetdir')
    table_name = request.form.get('table_name')
