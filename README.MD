# Data Clustering Project

## Autores
- Felipe Villa Jaramillo
- Angie Diaz Abaunza

## ¿Qué y para qué es?

El objetivo principal del proyecto de clustering de datos es agrupar un conjunto de datos en clusters, de tal manera que los elementos dentro de cada grupo sean más similares entre sí que a los de otros grupos. 

Nota: Este proyecto no fué codificado por los autores anteriormente mencionados, nosotros solo nos encargamos de realizar una interfaz web funcional para este proyecto, así que la lógica y el código sin la interfaz web lo podrá encontrar en el repositorio de github original: https://github.com/Broznif/CUARTA-ENTREGA-COD-LIMPIO---CELESTE-Y-ESTEFANNY.git

Aquí se describen las etapas y componentes clave del proyecto:

### 1. Recopilación de Datos:

   - **Fuentes de Datos:** Archivos CSV cargados por el usuario.
   - **Almacenamiento:** Datos almacenados en dataframes para su procesamiento.

### 2. Preprocesamiento de Datos:
   - **Limpieza de Datos:** Eliminación de valores atípicos y corrección de datos faltantes.
   - **Transformación de Datos:** Normalización o estandarización.
   - **Selección de Características:** Elegir las características relevantes.

### 3. Algoritmo de Clustering: K-Means
   - **Configuración:** Determinación del número de clusters (K) especificado por el usuario.
   - **Entrenamiento:** Aplicación del algoritmo K-Means para agrupar los datos.

### 4. Aplicación del Algoritmo
   - **Generación de Clusters:** Creación de clusters mediante el algoritmo K-Means.
   - **Evaluación:** Uso de métricas como la inercia y el coeficiente de silueta para evaluar los clusters.

### 5. Visualización y Análisis
   - **Visualización:** Representación tabular de los clusters.

## Prerrequisitos para hacerlo funcionar

- **Editor de código fuente (Opcional)**: Asegúrate de tener instalado un editor de código fuente en tu sistema. Te recomendamos Visual Studio Code, puedes descargarlo e instalarlo desde el [sitio oficial de Visual Studio Code](https://code.visualstudio.com/).

- **Python**: Debes tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde el [sitio oficial de Python](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la casilla "Agregar Python al PATH".

- **Flask**: Debes instalar Flask en tu sistema. Es posible descargarlo utilizando el comando `pip install flask` en la terminal de tu sistema.

- **Scikit-learn**: Debes instalar scikit-learn en tu sistema. Es posible descargarlo utilizando el comando `pip install scikit-learn`.

- **Numpy**: Debes instalar numpy en tu sistema. Es posible descargarlo utilizando el comando `pip install numpy`.

- **Pandas**: Debes instalar pandas en tu sistema. Es posible descargarlo utilizando el comando `pip install pandas`.

- **Matplotlib**: Debes instalar matplotlib en tu sistema. Es posible descargarlo utilizando el comando `pip install matplotlib`.

- **Kivy**: Debes instalar matplotlib en tu sistema. Es posible descargarlo utilizando el comando `pip install kivy["base"]`.

## ¿Cómo lo hago funcionar?

1. Copia el link del repositorio. (https://github.com/JustJara/machine-learning.git/)
2. Entra al escritorio de tu computadora, das click derecho y presiona la opción open git bash here.
3. En la consola de git bash escribe el comando "git clone" y pega el link del repositorio.
4. En el archivo SecretConfigExample.py que se encuentra en la carpeta controller guarde sus datos de conexión con la base de datos de NeonTech y posteriormente guarde el archivo dentro de la misma carpeta con el nombre de 'SecretConfig.py'.

## Ejecutar la interfaz web

1. Abra la terminal en su computadora.
2. Navegue a la carpeta donde está ubicado el proyecto. Por ejemplo, si está en el escritorio, puede usar el siguiente comando (ajuste la ruta según sea necesario): (cd Escritorio/machine-learning-main/)
3. Asegúrese de estar en el directorio raíz del proyecto. Verifique que puede ver los archivos y carpetas como app.py, src, static, etc.
4. Ejecute el siguiente comando para iniciar la aplicación: python3 app.py
5. Una vez ejecutado el comando anterior, busque en la terminal la línea que dice "Running on" y el URL que se muestra a continuación. Presione las teclas CTRL + Click en el URL para abrir directamente la página en su navegador web.

## Ejecutar pruebas unitarias

1. Abra la terminal en su computadora.
2. Navegue a la carpeta donde está ubicado el proyecto. Por ejemplo, si está en el escritorio, puede usar el siguiente comando (ajuste la ruta según sea necesario): (cd Escritorio/machine-learning-main/)
3. Asegúrese de estar en el directorio raíz del proyecto. Verifique que puede ver los archivos y carpetas como app.py, src, static, etc.
4. Los tests se encuentran en la carpeta 'Test' y a continuación se mostrará cada comando para ejecutar los diferentes tests existentes:

   - **1_error_CM**: Ejecutar el siguiente comando `python3 Test/1_error_CM.py`.
   - **1_exp_CM**: Ejecutar el siguiente comando `python3 Test/1_exp_CM.py`.
   - **1_normal_CM**: Ejecutar el siguiente comando `python3 Test/1_normal_CM.py`.
   - **2_error_CD**: Ejecutar el siguiente comando `python3 Test/2_error_CD.py`.
   - **2_exp_CD**: Ejecutar el siguiente comando `python3 Test/2_exp_CD.py`.
   - **2_normal_CD**: Ejecutar el siguiente comando `python3 Test/2_normal_CD.py`.
   - **test_clustering.py**: Ejecutar el siguiente comando `python3 Test/test_clustering.py`.
   - **test_database**: Ejecutar el siguiente comando `python3 Test/test_database.py`.
