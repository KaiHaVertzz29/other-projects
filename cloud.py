from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog 
from tkinter.filedialog import askopenfilename 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2 
from sklearn.cluster import KMeans
import os
main = tkinter.Tk()

main.title("Detecting clouds and predicting their movement from INSAT imagery")
main.geometry("1300x1200")

global filename
x=[]
y=[]
com = []

def drawImage(img,status):
    if status == 0:
        plt.title("Original Image")
    else:
        plt.title("Track Cloud Movement using Blue Dot")
    plt.imshow(img)
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close()

def uploadImage():
    global filename
    filename = filedialog.askdirectory(initialdir=".")
    pathlabel.config(text=filename)
    text.delete('1.0', END)
    text.insert(END,filename+" loaded\n");

def func(img):
    all_pixels = img.reshape((-1,1))
    km = KMeans(n_clusters=2)
    km.fit(all_pixels)
    centers = km.cluster_centers_
    com.append(centers)
    labels =km.labels_
    labels = labels.reshape((300,300))
    newImage = np.zeros((300,300))
    xint=0
    yint =0
    count=0
    for i in range(300):
        for j in range(300):
            if centers[0]<centers[1]:
                if(labels[i][j]==1):
                    newImage[i][j]=1
                    xint+=i
                    yint+=j
                    count+=1
                else:
                    newImage[i][j]=0
            else:
                if(labels[i][j]==0):
                    newImage[i][j]=1
                    xint+=i
                    yint+=j
                    count+=1
                else:
                    newImage[i][j]=0
    x.append(xint/count)
    y.append(yint/count)
    plt.scatter(xint/count,yint/count,c='blue')
    drawImage(newImage,1)

def detectCloud():
    timeaccord= []
    for fname in os.listdir(filename):
        timeaccord.append(fname)
    timeaccord.sort()
    final = []
    for fname in timeaccord[:24]:
        img = Image.open(os.path.join(filename, fname))
        img = img.resize((300,300))
        image = img
        drawImage(img,0)
        imarray = np.array(img)
        func(imarray)
        final.append(imarray)

def exit():
    main.destroy()
    
font = ('times', 16, 'bold')
title = Label(main, text='Detecting clouds and predicting their movement from INSAT imagery')
title.config(bg='light cyan', fg='pale violet red')
title.config(font=font)
title.config(height=3, width=120)
title.place(x=0,y=5)

font1 = ('times', 14, 'bold')
uploadButton = Button(main, text="Upload INSAT Image", command=uploadImage)
uploadButton.place(x=50,y=100)
uploadButton.config(font=font1) 

pathlabel = Label(main)
pathlabel.config(bg='light cyan', fg='pale violet red')
pathlabel.config(font=font1)
pathlabel.place(x=460,y=100)

detectButton = Button(main, text="Detect Cloud& & Movement", command=detectCloud)
detectButton.place(x=50,y=150)
detectButton.config(font=font1) 

exitButton = Button(main, text="Exit", command=exit)
exitButton.place(x=330,y=150)
exitButton.config(font=font1) 

font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=250)
text.config(font=font1)
main.config(bg='snow3')
main.mainloop()