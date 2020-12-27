from flask import render_template
from jinja2 import Environment, FileSystemLoader

def read_template( template_name):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    return template




def tables_select( tables):
    template = read_template( 'tables_select.tmplt.html')
    return template.render(tables=tables)