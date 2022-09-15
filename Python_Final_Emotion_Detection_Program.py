import os  
import cv2  
import numpy as np  
from keras.models import model_from_json  
from keras.preprocessing import image  
 
#load model  
model = model_from_json(open("fer.json", "r").read())  
#load weights  
model.load_weights('fer.h5')


from tensorflow.keras.utils import load_img, img_to_array
from skimage import io
from keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.utils import load_img
import matplotlib.pyplot as plt
import numpy as np
objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

import pyttsx3 
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def upload_file():
    global filename
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 = tk.Button(root,image=img)
    #b2.grid(row=3,column=1)
    canvas.create_window(400, 350, window=b2)


def emotion():
  
    img = tf.keras.utils.load_img(filename, grayscale=True, target_size=(48, 48))
    show_img=tf.keras.utils.load_img(filename,target_size=(200, 200))
    x = img_to_array(img)
    x = np.expand_dims(x, axis = 0)

    x /= 255

    custom = model.predict(x)
    #print(custom[0])
    #emotion_analysis(custom[0])

    x = np.array(x, 'float32')
    x = x.reshape([48, 48]);

    #plt.gray()
    #plt.imshow(show_img)
    #plt.show()


    m=0.000000000000000000001
    a=custom[0]
    for i in range(0,len(a)):
        if a[i]>m:
            m=a[i]
            ind=i
    print('Expression Prediction:',objects[ind])
    org = (50, 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    thickness = 2
    color = (255, 0, 0)
    t=('Expression Prediction:',objects[ind])
    #text = cv2.putText(img,'Expression Prediction:',objects[ind],org, font, 
                   #fontScale, color, thickness,)
    l3 = tk.Label(root,text='I think the emotion is:',width=20,font=rootfont)
    canvas.create_window(900, 350, window=l3)
    l2 = tk.Label(root,text=objects[ind],width=5,font=rootfont)
    canvas.create_window(900, 400, window=l2)
    ans="I think the emotion is", objects[ind]
    SpeakText(ans)
    
#Tkinter canvas
root= tk.Tk()
canvas = tk.Canvas(root, width = 1200, height = 900, bg='blue')
canvas.pack()
root.title("Emotion Detector")
rootfont=('times',18,'bold')
l1 = tk.Label(root,text='Welcome to the Emotion Detector',width=30,font=rootfont)
canvas.create_window(600, 30, window=l1)
#l1.grid(row=1,column=1)
b1 = tk.Button(root, text='Upload File',
width=10,command = lambda:upload_file())
#b1.grid(row=2,column=1)
canvas.create_window(545, 70,window=b1)
b1 = tk.Button(root, text='Submit',
width=8,command = emotion)
#b1.grid(row=2,column=1)
canvas.create_window(635, 70,window=b1)
root.mainloop()
