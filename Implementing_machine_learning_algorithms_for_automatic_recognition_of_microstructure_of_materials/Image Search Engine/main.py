#import necessary libraries

import random, os
import tkinter
import Descriptor
import searcher
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
    
    #this model is imported so that the resnet50 model can be used as a feature extractor for a input micrograph and then predict the type of micrograph with the trained Model 4 for both Task1 and Task2
    model = applications.resnet50.ResNet50(weights='imagenet', include_top=False, pooling='avg')
    # model_task_1 and model_task_2 is nothing but Model 4 (model which gave the best accuracy for task1 and task2) for task 1 and task 2 respectively.
    m = load_model('model_task_1.h5')
    m_f = load_model('model_task_2.h5')

    print('loaded')
    window = Tk()
    #create a tkinter window, which will have 3 buttons to perform 3 fuctions:
    #1. Predict the type of microstructure.
    #2. Search microstructures by keyword.
    #3. Search visually similar microstructures.
    window.title("Image Search Engine")
    
    window.geometry('350x200')
    #This function is to return the string value for a predicted integer value by Model 4
    def getText(text,text_f):
        
        if(text==0):
            s = "Type of Material is Ceramic"
        elif(text==1):
            s = "Type of Material is Composite"
        elif(text==2):
            s = "Type of Material is Iron"
        elif(text==3):
            s = "Type of Material is Aluminium"
        elif(text==4):
            s = "Type of Material is Copper"
        elif(text==5):
            s = "Type of Material is Magnesium"
        elif(text==6):
            s = "Type of Material is Misc"
        elif(text==7):
            s = "Type of Material is Refactory"            
        elif(text==8):
            s = "Type of Material is SuperAlloy"
        elif(text==9):
            s = "Type of Material is Titanium"
        elif(text==10):
            s = "Type of Material is Steel"     
        
        if(text_f==0):
            s_f = "Ferrous"
        elif(text_f==1):
            s_f = "Non Ferrous"
        elif(text_f==2):
            s_f = "Others"
            
        return s, s_f    
        
    #this function implements working of 1st function (Predict the type of microstructure)
    def Clicked1():
        
        in_path = filedialog.askopenfilename()
        print (in_path)

        root = Toplevel()
        #the input microstructure image is conveted into dimension of 224 by 224 as required by the Resnet50 architecture0
        img = image.load_img(in_path, target_size=(224, 224))
        if img is not None:
            #this conversion is used to print the rounded value of the predicted probability score.
            np.set_printoptions(suppress=True,formatter={'float_kind':'{:f}'.format})
            #the features of input microstructure are converted into arrays
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            features = model.predict(x)[0]
            features = features.reshape(1,2048)
            # p is the prediction value by a model
            # k is the prediction score by a model
            p = m.predict_classes(features)
            k = m.predict(features)
            p_f = m_f.predict_classes(features)
            k_f = m_f.predict(features)
        im = PIL.Image.open(in_path).resize((300,300))
        photo = PIL.ImageTk.PhotoImage(im)
        s, s_f = getText(p[0],p_f[0])
        
        
        pr = round((k[0][p[0]] * 100),3)
        prob = str(pr) 
        
        pr_f = round((k_f[0][p_f[0]] * 100),3)
        prob_f = str(pr_f)
        
        label = Label(root, image=photo,font=("Arial Bold", 10), text= s + " with probability of " + prob + " %" + "\n" + " and " + s_f + " with probability of " + prob_f + " % ",    compound=tkinter.BOTTOM).pack()
        
        label.image = photo  
    
    #this function is for implementing 2nd feature of image search engine (search microstructrues by keywords)
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
          
            #this is while loop is to search for only 3 similar microsrtucture. If 3 microstructure for a given keyword is found then the while loop is exited.
            while(i<=2):
                # the code randomly picks a microstructure image from a pool of all microstructures of different type
                random_filename = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
                # this extracts the feature of selected microstructure and predict its type
                img = image.load_img(os.path.join(path, random_filename), target_size=(224, 224))
                if img is not None:
                    x = image.img_to_array(img)
                    x = np.expand_dims(x, axis=0)
                    x = preprocess_input(x)
                    features = model.predict(x)[0]
                    features = features.reshape(1,2048)
                    p = m.predict_classes(features)
                    k = m.predict(features)
                    #if the predicted type is same as the searched text, then it is added to an array else a new random microstructure is selected again
                    if (p[0]==t):
                        i = i+1
                        image_array.append(os.path.join(path, random_filename))
            print(image_array) 
            
            root.grid_rowconfigure(0, weight=1)
            root.grid_columnconfigure(0, weight=1)
            cnv = Canvas(root)
            cnv.grid(row=0, column=0, sticky='nswe')
            #this is the window scroll function
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
        
    # this fucntion implements 3rd feature of image search engine (search for visually similar microstructures)
    def Clicked3():
        
        cd = Descriptor((8, 12, 3))
        in_path = filedialog.askopenfilename()
        num= 1
        print (in_path)

        query = cv2.imread(in_path)
        features = cd.describe(query)
        #histogram of the input microstructure is compared to histograms of all other microstructures/
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
                t, s_f = getText(p[0],p_f[0])
                
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
