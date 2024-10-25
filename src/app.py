'''Este es main y es donde vamos a escribir el código de nuestra app'''

import pandas as pd


import plotly.express as px


##AQUÍ ES DONDE VAMOS A INSERTAR LA DIRECCIÓN DEL ARCHIVO EN##
##FORMA DE STRING##

##df = pd.read_csv({STRING})##

from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Ruta principal: carga del formulario
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Ruta para procesar el archivo CSV
@app.route('/upload', methods=['POST'])

def upload_file():
    if 'file' not in request.files:
        return 'No file part'  # Error si no se adjuntó archivo

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'  # Error si no se seleccionó archivo

    if file and file.filename.endswith('.csv'):

        df = pd.read_csv(file)

        conteo_colores = df['color'].value_counts()

        fig = px.pie(
            values = conteo_colores,
            names = conteo_colores.index,
            title = 'Aquí va un Title',
            color = conteo_colores.index,
            color_discrete_sequence = ['red', 'green'],   
        )

        ##FIGURA GENERADA COMO OBJETO HTML##
        ##ESTE OBJETO ES EL QUE QUEREMOS INSERTAR EN EL VISUALIZADOR##
        graph_html = pio.to_html(fig, full_html=False)
        return render_template('graph.html', graph_html=graph_html)
    
    return 'El archivo debe ser un archivo CSV (.csv)'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#Estoy reconectandome pipipi
