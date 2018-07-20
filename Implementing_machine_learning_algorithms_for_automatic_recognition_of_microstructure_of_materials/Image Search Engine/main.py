import random, os
import tkinter
from search.colordescriptor import Descriptor
from search.searcher import Searcher
import argparse
from tkinter import *
from tkinter import filedialog
from skimage import data, color, feature
from keras.preprocessing import image
import PIL.Image
import PIL.Image as im
import PIL.ImageTk
from keras import applications
from keras.models import Model
from keras.models import load_model
import numpy as np
from keras.applications.vgg19 import preprocess_input
import cv2
import os

def main():
    
    model = applications.resnet50.ResNet50(weights='imagenet', include_top=False, pooling='avg')
    m = load_model('model_task_1.h5')
    m_f = load_model('model_task_2.h5')

    print('loaded')
    window = Tk()
 
    window.title("Image Search Engine")
    
    window.geometry('350x200')
    
    def Clicked1():
        
        in_path = filedialog.askopenfilename()
        print (in_path)

        root = Toplevel()
        
        img = image.load_img(in_path, target_size=(224, 224))
        if img is not None:
            np.set_printoptions(suppress=True,formatter={'float_kind':'{:f}'.format})
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            features = model.predict(x)[0]
            features = features.reshape(1,2048)
            p = m.predict_classes(features)
            k = m.predict(features)
            p_f = m_f.predict_classes(features)
            k_f = m_f.predict(features)
        im = PIL.Image.open(in_path).resize((300,300))
        photo = PIL.ImageTk.PhotoImage(im)
        
        
        if(p[0]==0):
            s = "Type of Material is Ceramic"
        elif(p[0]==1):
            s = "Type of Material is Composite"
        elif(p[0]==2):
            s = "Type of Material is Iron"
        elif(p[0]==3):
            s = "Type of Material is Aluminium"
        elif(p[0]==4):
            s = "Type of Material is Copper"
        elif(p[0]==5):
            s = "Type of Material is Magnesium"
        elif(p[0]==6):
            s = "Type of Material is Misc"
        elif(p[0]==7):
            s = "Type of Material is Refactory"            
        elif(p[0]==8):
            s = "Type of Material is SuperAlloy"
        elif(p[0]==9):
            s = "Type of Material is Titanium"
        elif(p[0]==10):
            s = "Type of Material is Steel"     
        
        if(p_f[0]==0):
            s_f = "Ferrous"
        elif(p_f[0]==1):
            s_f = "Non Ferrous"
        elif(p_f[0]==2):
            s_f = "Others"
            
        pr = round((k[0][p[0]] * 100),3)
        prob = str(pr) 
        
        pr_f = round((k_f[0][p_f[0]] * 100),3)
        prob_f = str(pr_f)
        
        label = Label(root, image=photo,font=("Arial Bold", 10), text= s + " with probability of " + prob + " %" + "\n" + " and " + s_f + " with probability of " + prob_f + " % ",    compound=tkinter.BOTTOM).pack()
        
        label.image = photo  
    
    def Clicked2():         
        
        window = Tk()
 
        window.title("Search By Text")
    
        window.geometry('350x200')   
        
        txt = Entry(window,width=25)
        txt.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        def c2():
            image_array=[]
            i=0
            num= 1
            t = None
            root = Toplevel()
            root.title("Search Results for "+ txt.get() + " Images..." )
    
            if (txt.get()=="ceramic"):
                t = 0
            elif(txt.get()=="composite"):
                t=1
            elif(txt.get()=="iron"):
                t=2
            elif(txt.get()=="aluminium"):
                t=3
            elif(txt.get()=="copper"):
                t=4
            elif(txt.get()=="magnesium"):
                t=5
            elif(txt.get()=="misc"):
                t=6
            elif(txt.get()=="refactory"):
                t=7
            elif(txt.get()=="superalloy"):
                t=8
            elif(txt.get()=="titanium"):
                t=9
            elif(txt.get()=="steel"):
                t=10
            
            path="dataset/"
          
            while(i<=2):
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                
                img = image.load_img(os.path.join(path, random_filename), target_size=(224, 224))
                if img is not None:
                    x = image.img_to_array(img)
                    x = np.expand_dims(x, axis=0)
                    x = preprocess_input(x)
                    features = model.predict(x)[0]
                    features = features.reshape(1,2048)
                    p = m.predict_classes(features)
                    k = m.predict(features)
                    if (p[0]==t):
                        i = i+1
                        image_array.append(os.path.join(path, random_filename))
            print(image_array) 
            
            root.grid_rowconfigure(0, weight=1)
            root.grid_columnconfigure(0, weight=1)
            cnv = Canvas(root)
            cnv.grid(row=0, column=0, sticky='nswe')
            hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
            hScroll.grid(row=1, column=0, sticky='we')
            vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
            vScroll.grid(row=0, column=1, sticky='ns')
            cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
            frm = Frame(cnv)
            cnv.create_window(0, 0, window=frm, anchor='nw')
            for s in image_array:
                nn= str(num)
                im = PIL.Image.open(s).resize((200,200))
                tkimage =  PIL.ImageTk.PhotoImage(im)
                myvar=Label(frm,image = tkimage, font=("Arial Bold", 10),text = "(" + nn + ")", compound=tkinter.BOTTOM)
                myvar.image = tkimage
                myvar.pack()
                num = num + 1
            frm.update_idletasks()
            cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
            
        
        btn = Button(window, text="Search",command = c2)
        btn.place(relx=0.5, rely=0.5, anchor=CENTER)
 
        
        
    
    def Clicked3():
        
        cd = Descriptor((8, 12, 3))
        in_path = filedialog.askopenfilename()
        num= 1
        print (in_path)

        query = cv2.imread(in_path)
        features = cd.describe(query)

        searcher = Searcher("compare_hist.csv")
        results = searcher.search(features)
        print(results)
        
        root = Toplevel()
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        cnv = Canvas(root)
        cnv.grid(row=0, column=0, sticky='nswe')
        hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
        vScroll.grid(row=0, column=1, sticky='ns')
        cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
        frm = Frame(cnv)
        cnv.create_window(0, 0, window=frm, anchor='nw')
            
        for r,s in results:
            
            print('inside')
            
            img = image.load_img(s, target_size=(224, 224))
            if img is not None:
                t = "test"
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)
                features = model.predict(x)[0]
                features = features.reshape(1,2048)
                p = m.predict_classes(features)
                p_f = m_f.predict_classes(features)
                k = m.predict(features)
                print(p[0])
                
            if(p[0]==0):
                t = "Type of Material: Ceramic"
            elif(p[0]==1):
                t = "Type of Material: Composite"
            elif(p[0]==2):
                t = "Type of Material: Iron"
            elif(p[0]==3):
                t = "Type of Material: Aluminium"
            elif(p[0]==4):
                t = "Type of Material: Copper"
            elif(p[0]==5):
                t = "Type of Material: Magnesium"
            elif(p[0]==6):
                t = "Type of Material: Misc"
            elif(p[0]==7):
                t = "Type of Material: Refactory"            
            elif(p[0]==8):
                t = "Type of Material: SuperAlloy"
            elif(p[0]==9):
                t = "Type of Material: Titanium"
            elif(p[0]==10):
                t = "Type of Material: Steel"     
        
            if(p_f[0]==0):
                s_f = "Ferrous"
            elif(p_f[0]==1):
                s_f = "Non Ferrous"
            elif(p_f[0]==2):
                s_f = "Others"
            
            nn= str(num)
            im = PIL.Image.open(s).resize((200,200))   
            tkimage =  PIL.ImageTk.PhotoImage(im)
            myvar=Label(frm,image = tkimage, text ="(" + nn + ") " + t + " / " + s_f, compound=tkinter.BOTTOM)
            myvar.image = tkimage
            num = num + 1
            myvar.pack()

        frm.update_idletasks()
        cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
            
        
    btn1 = Button(window, text="Predict type of Image",bg="blue", fg="white", command=Clicked1)
    
    btn1.place(relx=0.5, rely=0.2, anchor=CENTER)
 
    btn2 = Button(window, text="Search by text",bg="blue", fg="white", command = Clicked2)
    
    btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
 
    btn3 = Button(window, text="Search By Image",bg="blue", fg="white", command = Clicked3)
    
    btn3.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    window.mainloop()
if __name__ == "__main__":
    main()