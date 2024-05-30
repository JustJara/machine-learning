import sys
sys.path.append('src')

from controller.clustering import process_csv_and_cluster
from flask import Blueprint, render_template, request, redirect, url_for
from controller.database import Database


blueprint = Blueprint('web', __name__, template_folder='templates')
from SecretConfig import PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/clustering', methods=['POST'])
def show_clustering():
    try:
        db = f"dbname={PGDATABASE}, user={PGUSER}, password={PGPASSWORD}, host={PGHOST}, port={PGPORT}"
        db_connect = Database(db)
        db_connect.connect()
        db_connect.create_tables()
        numclusters = int(request.form['numClusters'])
        file = request.files['csvFile']
        if file.filename == '':
            return 'No file selected', 400
        # Guardar el archivo en una ubicación temporal
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)
        info=  process_csv_and_cluster(db_connect,file_path, numclusters)
        if info[0]:
            data_to_html = info[2].to_html()
            return render_template('clustering.html', data=data_to_html, clusters=info[3])
        else:
            print('Entro al else')
            return info[1], 400
    except KeyError as e:
        return f"Missing form key: {e.args[0]}", 400
    except Exception as e:
        return str(e), 500
