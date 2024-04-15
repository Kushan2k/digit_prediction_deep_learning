from ttkbootstrap import Window
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import widgets
from tkinter import filedialog,messagebox

from cv2 import imread
import cv2
import joblib
from numpy import array,argmax


window=Window("Digit Classifire")
window.geometry('300x200+100+100')
window.resizable(False,False)

model=joblib.load('model.joblib')

def button_click():
  try:
    filename=filedialog.askopenfilename(defaultextension='png',filetypes=[("Image Files","*.png"),("Image JPG",'*.JPG')],parent=window,title="Please Select an image")

    cv_img=imread(filename)

    resized_image=cv2.cvtColor(cv2.resize(cv_img,(28,28),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY)

    np_rezied_img=array(resized_image)

    # print(np_rezied_img.shape)
    
    # print(dir(model))

    # np_rezied_img.reshape((1,28*28))
    predicted_number=model.predict(np_rezied_img.reshape((1,28*28)))
    # print(argmax(predicted_number[0]))
    [print(i) for i in predicted_number[0]]

  except Exception as e:
    print(e)
    messagebox.showerror(title="error",message=str(e))

  print(filename)

  pass


button=widgets.Button(window,text='Browse',command=button_click)
button.pack()





window.mainloop()