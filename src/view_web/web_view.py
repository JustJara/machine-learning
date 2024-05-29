import sys
sys.path.append('src')

from controller.clustering import process_csv_and_cluster
from flask import Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint('web', __name__, template_folder='templates')

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/clustering', methods=['POST'])
def show_clustering():
    try:
        numclusters = int(request.form['numClusters'])
        db = ''
        file = request.files['csvFile']
        if file.filename == '':
            return 'No file selected', 400
        # Guardar el archivo en una ubicación temporal
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)
        process_csv_and_cluster(db,file_path, numclusters)
        return render_template('clustering.html', numclusters=numclusters)
    except KeyError as e:
        return f"Missing form key: {e.args[0]}", 400
    except Exception as e:
        return str(e), 500
