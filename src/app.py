'''Este es main y es donde vamos a escribir el código de nuestra app'''

import pandas as pd

import plotly.express as px


##AQUÍ ES DONDE VAMOS A INSERTAR LA DIRECCIÓN DEL ARCHIVO EN##
##FORMA DE STRING##

##df = pd.read_csv({STRING})##

df = pd.read_csv('data/test_1.csv')

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
fig.show()

