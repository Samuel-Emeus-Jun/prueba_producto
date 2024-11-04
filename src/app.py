from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])

def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'  

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

        graph_html = pio.to_html(fig, full_html=False)
        return render_template('graph.html', graph_html=graph_html)
    
    return 'El archivo debe ser un archivo CSV (.csv)'

if __name__ == '__main__':
    app.run(debug=True)