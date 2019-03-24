#import para el backend y el modelo
import numpy as np
import pandas as pd #quitar luego
from sklearn.model_selection import train_test_split #quitar luego
from sklearn import preprocessing
import librosa
#imports para la gui
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
window = tk.Tk()
from loadModel import load_model

#Cargar el modelo
model = load_model()


#Propiedades de la Ventana
  
window.title("UIS Music Gender Classifier")
window.geometry('400x400')
window.maxsize(width=400,height=400)
frame1 = tk.Frame(window, bg='yellow green')
frame1.pack(fill='both', expand='yes')
#-------------------------#

#Widgets

lbl0 = tk.Label(frame1, text="Bienvenidos",
                bg='yellow green',
                fg='white',
                font=("Arial Bold",40))
lbl0.place(x=60,y=100)

#lbl1 = tk.Label(frame1, text="Hecho por : -Henry Iván Peña Contreras 2150606\n \t -Diego Fernando Medina Blanco 2150606\n \t  -William Giovanny Palomino 2150606",
#                bg='yellow green',
#                fg='snow4',
#                font=("Verdana",8))
#lbl1.place(x=40,y=550)
def create_new_window():
    window.destroy()
    window1 = tk.Tk()
    window1.title("Identificar Género de Canción")
    window1.geometry('800x600')
    window1.maxsize(width=800,height=600)
    frame2 = tk.Frame(window1, bg='yellow green')
    frame2.pack(fill='both', expand='yes')
    
def choose_file():
    filename = askopenfilename()
    return filename
    
def identificar_genero():
    audiopath = choose_file()
    if(audiopath != ""):
        #Se tiene el path del archivo, ahora se procede a realizar la regresión
        
        #Se empieza por cargar el achivo con librosa
        y , sr = librosa.load(audiopath, mono=True, duration=30)
        
        #se procede a extraer las características
        features = np.zeros(shape=(1,26))
        features = np.ndarray.astype(features, float)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        features[0][0] = np.mean(chroma_stft)
        rmse = librosa.feature.rms(y=y)
        features[0][1] = np.mean(rmse)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        features[0][2] = np.mean(spec_cent)
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        features[0][3] = np.mean(spec_bw)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        features[0][4] = np.mean(rolloff)
        zcr = librosa.feature.zero_crossing_rate(y)
        features[0][5] = np.mean(zcr)
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        i = 5
        #features = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
        for e in mfcc:
            i += 1
            features[0][i] = np.mean(e)
            
        features = np.array(features)
        
        #se cargan las medias y desviaciones estándar
        medias = np.load('../notebooks/medias.npy')
        desvest = np.load('../notebooks/desvest.npy')
        print(medias)
        print(desvest)
        #Se procede a estandarizar las caraceterísticas con respecto a las medias y desviaciones estándar
        print(features)
        for idx in range(features.shape[1]):
            features[0][idx] = (features[0][idx]-medias[idx])/desvest[idx]
        
        #Se procede a realizar la regresión con el modelo
        prediction = model.predict_classes(features)
        #print("X=%s, Predicted=%s" % (features, prediction))
        #print(features.shape)
        #ahora se procede a mostrar al usuario la predicción del genero musical del audio que ingresó
        generos = []
        #generos[0] = "blues"
        #generos[1] = "clasica"
        #generos[2] = "country"
        #generos[3] = "disco"
        #generos[4] = "hiphop"
        #generos[5] = "jazz"
        #generos[6] = "metal"
        #generos[7] = "pop"
        #generos[8] = "reggae"
        #generos[9] = "rock"}
        generos.append("Blues")
        generos.append("Clásica")
        generos.append("Country")
        generos.append("Disco")
        generos.append("Hiphop")
        generos.append("Jazz")
        generos.append("Metal")
        generos.append("Pop")
        generos.append("Reggae")
        generos.append("Rock")
        genero = generos[prediction[0]]
        text = "La canción es del género: " + genero + "."
        messagebox.showinfo("¡Éxito!", text)
        
    else:
        messagebox.showinfo("Error", "Ningún archivo seleccionado")


btn0 = tk.Button(frame1, text="Identificar Género Canción",
                 bg='pale goldenrod',
                 fg='dim gray',
                 font=("Verdana",10),
                 command= identificar_genero)
btn0.place(x=100,y=300)

def click_credits():       
    tk.messagebox.showinfo("Créditos","Hecho por : -Henry Iván Peña Contreras 2150606\n \t -Diego Fernando Medina Blanco 2150606\n \t  -William Giovanny Palomino 2150606 \n\n Universidad Industrial de Santander\n\t\t 2019")
    
    
btn1 = tk.Button(frame1, text="Créditos",
                 bg='pale goldenrod',
                 fg='dim gray',
                 font=("Verdana",10),
                 command=click_credits)
btn1.place(x=160,y=350)


window.mainloop()
