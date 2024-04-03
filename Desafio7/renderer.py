from jinja2 import Environment, FileSystemLoader

def render_html(datos_aves):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    html = template.render(aves=datos_aves)
    return html