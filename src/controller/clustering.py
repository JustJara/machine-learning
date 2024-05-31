import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

import sys
sys.path.append('src')
from controller.database import Database

def process_csv_and_cluster(db : Database, file_path, num_clusters):
    try:
        # Leer el CSV y mostrar los primeros registros para diagnóstico
        data = pd.read_csv(file_path)
        print("Contenido completo del CSV:")
        print(data)
        
        # Seleccionar solo columnas numéricas
        numeric_data = data.select_dtypes(include=[np.number])
        print("Datos numéricos seleccionados:")
        print(numeric_data)

        if numeric_data.empty:
            return False, "No numeric data found in CSV for clustering."

        # Convertir todas las columnas a numéricas y manejar errores
        numeric_data = numeric_data.apply(pd.to_numeric, errors='coerce')
        print("Datos numéricos después de to_numeric:")
        print(numeric_data)
        
        # Llenar valores nulos con la media de la columna
        numeric_data.fillna(numeric_data.mean(), inplace=True)

        # Verificar si después de limpiar hay suficientes datos para el clustering
        if numeric_data.empty or numeric_data.isnull().values.any():
            return False, "After cleaning, no valid numeric data found for clustering."

        # Aplicar KMeans clustering
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(numeric_data)
        data['Cluster'] = kmeans.labels_

        # Guardar los resultados en la base de datos
        cluster_results = data.to_dict(orient='records')
        db.insert_clustering_result(file_path, num_clusters, cluster_results)

        return [True, "Clustering successful.",data,numeric_data]

    except Exception as e:
        return False, f"Error processing CSV and performing clustering: {e}"