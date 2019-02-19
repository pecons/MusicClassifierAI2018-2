# Clasificador de Música por Género
**Integrantes**
- William Palomino
- Henry Peña
- Diego Medina


**Universidad Indsutrial De Santander** </br>
**Ingenieria de sistemas**</br>
**2019**</br>
<p align="center"><img src="http://garza.uis.edu.co/idayregreso/images/logoUIS.jpg" width="342" heigth="166"></p>

# Introduccion
El planteamiento del proyecto consiste en crear un clasificador de canciones por su género, por medio de caracteristicas similares preprocesadas en los espectrogramas de las canciones.

Para esto se Utilizará como entrenamiento un Dataset de canciones 1000 canciones en formato au con su respectivo género, 10 en total.

Para entrenar un modelo, primero se necesita obtener de cada una de esas canciones sus caracteristicas más relevantes para el problema de clasificación, por lo que se utilizó la Librería *LIBROSE* para explorar los espectrogramas y sacar así las siguentes características:

<ul>
   <li> Coeficientes ceptrales en la frecuencia de mel (MFCC)(20)
   <li> Spectral Centroid,
   <li> Zero Crossing Rate
   <li> Chroma Frequencies
   <li> Spectral Roll-off.
</ul>




# Objetivo
Clasificar canciones por su respectivo género músical.

# Referencias
Los datos del dataset y otros datos fueron recolectados por usuarios que Tambien tienen como propósito el tratamiento de señales de audio.

-https://www.kaggle.com/c/mlp2016-7-msd-genre/data

-https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8

-https://ieeexplore.ieee.org/document/1021072

-https://archive.ics.uci.edu/ml/datasets/FMA%3A+A+Dataset+For+Music+Analysis

-https://gist.github.com/parulnith/7f8c174e6ac099e86f0495d3d9a4c01e

-https://labrosa.ee.columbia.edu/millionsong/

