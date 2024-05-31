import os
import sys
import tempfile
sys.path.append('src')

from controller.clustering import process_csv_and_cluster
from flask import Blueprint, render_template, request, redirect, url_for
from controller.database import Database

# Configurar la ruta a la carpeta de plantillas
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'templates')
blueprint = Blueprint('web', __name__, template_folder=template_dir)


@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/clustering', methods=['GET', 'POST'])
def show_clustering():
    '''
    This method is called when the user accesses the /clustering route. It renders the clustering.html template when the request method is GET.
      When the request method is POST, it processes the uploaded CSV file and returns the clustering results in an HTML table.

    Este método se llama cuando el usuario accede a la ruta /clustering. Renderiza la plantilla clustering.html cuando el método de solicitud es GET.
        Cuando el método de solicitud es POST, procesa el archivo CSV cargado y devuelve los resultados de agrupamiento en una tabla HTML.
    '''

    if request.method == 'GET':
        return render_template('clustering.html')
    
    elif request.method == 'POST':
        try:
            DATABASE = Database('connection_string')
            DATABASE.connect()
            DATABASE.create_tables()

            numclusters = (request.form.get('numClusters', None))
            file = request.files['csvFile']

            # Verificar si se seleccionó un archivo y si es un archivo CSV
            if not file or file.filename == '':
                return render_template('errors_template.html', error_message="No se seleccionó ningún archivo"), 400
            
            # Verificar si el archivo es un archivo CSV
            if not file.filename.endswith('.csv'):
                return render_template('errors_template.html', error_message="El archivo debe ser un archivo CSV"), 400
            
            # Verificar si el número de clusters no está vacío
            if not numclusters:
                return render_template('errors_template.html', error_message="El número de clusters no puede estar vacío"), 400
            
            # Convertir el número de clusters a un entero
            numclusters = int(numclusters)
            
            # Guardar el archivo en una ubicación temporal
            # Se llama al método para comprobar que el archivo se guarda en la ubicación temporal correcta
            file_path = get_temp_file_path(file.filename)
            file.save(file_path)

            # Procesar el archivo CSV y realizar el clustering
            cluster_response = process_csv_and_cluster(DATABASE, file_path, numclusters)
            if cluster_response[0]:
                data_in_html = cluster_response[2].to_html()
                numeric_data_in_html = cluster_response[3].to_html()
                return render_template('Resultados.html', data=data_in_html, numeric_data=numeric_data_in_html)
            else:
                return render_template('errors_template.html', error_message=cluster_response[1])
            
        except KeyError as e:
            return render_template('errors_template.html', error_mmessage=str(e))
        except Exception as e:
            return render_template('errors_template.html', error_message=str(e))
        

def get_temp_file_path(filename):
    '''
    This method returns the path to a temporary file based on the operating system.

    Este método devuelve la ruta a un archivo temporal basado en el sistema operativo.

    Returns
    -------

    file_path : str
        The path to the temporary file. La ruta al archivo temporal.
    '''

    if os.name == 'nt':  # Windows
        file_path = tempfile.gettempdir() + f"\\{file.filename}"
    else:  # Unix-based systems
        temp_dir = '/tmp'
        file_path = os.path.join(temp_dir, filename)
    return file_path

@blueprint.route('/resultados')
def resultados():
    '''
    This method is called when the user accesses the /resultados route. It renders the Resultados.html template.

    Este método se llama cuando el usuario accede a la ruta /resultados. Renderiza la plantilla Resultados.html.

    Returns
    -------
    render_template : HTML template
        The Resultados.html template. La plantilla Resultados.html.
    '''
    return render_template('Resultados.html')




