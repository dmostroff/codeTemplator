import templator_repository as tr
import templator_view as tv
from flask import render_template

def get_tables_by_prefix( prefix):
    df = tr.get_tables_by_prefix(prefix)
    return tv.tables_select(df.to_dict("records"))



def create_api_resource( table_name):
    """
    docstring
    """
    pass