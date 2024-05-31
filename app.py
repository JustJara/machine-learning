import sys
sys.path.append("src")

from flask import Flask, render_template
from view_web import web_view

app = Flask(__name__)
app.register_blueprint(web_view.blueprint)

@app.errorhandler(404)
def page_not_found(e):
    '''
    This method is called when a 404 error occurs. It renders the error.html template with a "Page not found" message.

    Este método se llama cuando se produce un error 404. Renderiza la plantilla error.html con un mensaje de "Página no encontrada".

    Returns
    -------
    render_template : HTML template
        The error.html template with a "Page not found" message. La plantilla error.html con un mensaje de "Página no encontrada".

    '''
    return render_template('error.html', error_message="Página no encontrada"), 404


if __name__ == '__main__':
    app.run(debug=True)