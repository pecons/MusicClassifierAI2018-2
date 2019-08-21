<p align="center"><img src="https://i.imgur.com/ueLN6rk.jpg" width="1500" heigth="500"></p>


# Clasificador de Música por Género
**Integrantes**
- William Palomino
- Henry Peña
- Diego Medina


**Universidad Indsutrial De Santander** </br>
**Ingenieria de sistemas**</br>
**2019**</br>
<p align="center"><img src="http://garza.uis.edu.co/idayregreso/images/logoUIS.jpg" width="342" heigth="166"></p>

# ¡Clickea y mira el video!

[![Foo](https://i.imgur.com/4h13yFG.jpg)](https://youtu.be/5gOOh8O8p3k)

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
-Clasificar canciones por su respectivo género músical.<br> 
-Aprender acerca de los Modelos de DeepLearning, más especificamente los que ofrece la Librería Keras usando TensorFlow como backend.

# Referencias
Los datos del dataset y otros datos fueron recolectados por usuarios que Tambien tienen como propósito el tratamiento de señales de audio.

-https://www.kaggle.com/c/mlp2016-7-msd-genre/data

-https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8

-https://ieeexplore.ieee.org/document/1021072

-https://archive.ics.uci.edu/ml/datasets/FMA%3A+A+Dataset+For+Music+Analysis

-https://gist.github.com/parulnith/7f8c174e6ac099e86f0495d3d9a4c01e

-https://labrosa.ee.columbia.edu/millionsong/

TENSORFLOW Y KERAS:

-https://www.apsl.net/blog/2018/02/02/tensor-flow-para-principiantes-vi-uso-de-la-api-keras/

-https://enmilocalfunciona.io/deep-learning-basico-con-keras-parte-1/

-https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network

 METRICS:
 
 -https://stackoverflow.com/questions/34518656/how-to-interpret-loss-and-accuracy-for-a-machine-learning-model
 

GUI:

-https://stackoverflow.com/questions/42841542/encoding-a-tensorflow-neural-network-into-tkinter-gui

-https://likegeeks.com/es/ejemplos-de-la-gui-de-python/

-https://www.youtube.com/watch?v=HjNHATw6XgY&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=1

-http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

-https://docs.python.org/3/library/tk.html

