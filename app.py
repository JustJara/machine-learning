import sys
sys.path.append("src")

from flask import Flask

from view_web import web_view

app = Flask(__name__)
app.register_blueprint(web_view.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
