from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renderiza index4.html desde la carpeta templates

@app.route('/grafica')
def grafica():
    # Cargar datos y crear la figura
    df = pd.read_csv('data/test_1.csv')
    conteo_colores = df['color'].value_counts()
    
    fig = px.pie(
        values=conteo_colores,
        names=conteo_colores.index,
        title='',
        color=conteo_colores.index,
        color_discrete_sequence=['red', 'green'],
    )
    
    # Guardar la figura como un objeto HTML
    graph_html = fig.to_html(full_html=False)
    
    return graph_html  # Retorna el HTML de la gráfica

if __name__ == '__main__':
    app.run(debug=True)