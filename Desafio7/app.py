from api import get_informacion
from renderer import render_html

datos_aves = get_informacion()
html_content = render_html(datos_aves)

with open('aves_chile.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print('El sitio web ha sido generado correctamente en el archivo aves_chile.html')