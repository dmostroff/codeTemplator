import os
import base_service as bs
import templator_repository as tr
import templator_helper as th
import templator_view as tv
from flask import request, jsonify

def create_routes( prefix):
    df = tr.get_tables_and_columns_by_prefix( os.getenv('SCHEMA'), prefix)
    return th.write_routes(prefix, df)

def create_service( prefix):
    df = tr.get_tables_and_columns_by_prefix( os.getenv('SCHEMA'), prefix)
    return th.write_service(prefix, df)

def create_repository( prefix):
    df = tr.get_tables_and_columns_by_prefix( os.getenv('SCHEMA'), prefix)
    return th.write_repository(prefix, df)

def create_api_js_service( prefix):
    df = tr.get_tables_and_columns_by_prefix( os.getenv('SCHEMA'), prefix)
    return th.write_api_js_service(prefix, df)

def create_vue_component( prefix):
    df = tr.get_tables_and_columns_by_prefix( os.getenv('SCHEMA'), prefix)
    tables = th.create_tables( df)
    fwritten = []
    for (table) in tables:
        fwritten.append( th.write_vue_component( prefix, table))
    return jsonify(fwritten)

def get_tables_by_prefix( prefix):
    schema = os.getenv('SCHEMA')
    df = tr.get_tables_and_columns_by_prefix(schema, prefix)
    return tv.tables_select(df.to_dict("records"))

# def gen_headers( table_name):
#     schema = os.getenv('SCHEMA')
#     df = tr.get_column_info( schema, table_name)
#     headers = vth.create_headers(df)
#     th.save_render( os.getenv('TARGET_DIR'), table_name, 'js', headers)

#     return tv.tables_select(df.to_dict("records"))


def create_api_resource( table_name):
    """
    docstring
    """
    target_dir = request.form.get('targetdir')
    table_name = request.form.get('table_name')
