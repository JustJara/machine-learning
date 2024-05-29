# database.py

import psycopg2
import json

class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos")
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            self.cursor = None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_tables(self):
        if not self.cursor:
            print("No se puede crear la tabla porque el cursor es None. Asegúrate de que la conexión esté establecida.")
            return
        
        create_table_query = """
            CREATE TABLE IF NOT EXISTS my_schema.clustering_results (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                num_clusters INTEGER NOT NULL,
                cluster_results JSONB NOT NULL
            );
        """
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Tabla creada exitosamente")
        except psycopg2.Error as e:
            print(f"Error al crear la tabla: {e}")

    def insert_clustering_result(self, filename, num_clusters, cluster_results):
        if not self.cursor:
            print("No se puede insertar datos porque el cursor es None. Asegúrate de que la conexión esté establecida.")
            return
        
        insert_query = """
            INSERT INTO my_schema.clustering_results (filename, num_clusters, cluster_results)
            VALUES (%s, %s, %s);
        """
        try:
            self.cursor.execute(insert_query, (filename, num_clusters, json.dumps(cluster_results)))
            self.connection.commit()
            print("Datos insertados exitosamente")
        except psycopg2.Error as e:
            print(f"Error al insertar datos: {e}")
