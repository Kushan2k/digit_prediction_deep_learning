from ttkbootstrap import Window
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import widgets,style
from tkinter import filedialog,messagebox

from cv2 import imread
import cv2
import joblib
from numpy import array,argmax


window=Window("Digit Classifire")
window.geometry('300x200+100+100')
window.resizable(False,False)

ans=StringVar('')
accuracy=StringVar('')

model=joblib.load('model.joblib')


#labels
lebal=widgets.Label(master=window,text='Answer:- ',style=style.SUCCESS,font=('serif',20))
lebal.pack(fill=X,pady=10,padx=10)
lebal_accuracy=widgets.Label(master=window,text='Accuracy:- ',style=style.SUCCESS,font=('serif',20))
lebal.pack(side=BOTTOM,fill=X,pady=10,padx=10)

#button
button=widgets.Button(window,text='Browse')
button.pack(pady=10,padx=10,side=TOP,ipadx=5,ipady=5)


#callbacks

def button_click(event):
  try:
    filename=filedialog.askopenfilename(defaultextension='png',filetypes=[("Image Files","*.png"),("Image JPG",'*.JPG')],parent=window,title="Please Select an image")

    cv_img=imread(filename)

    resized_image=cv2.cvtColor(cv2.resize(cv_img,(28,28),interpolation=cv2.INTER_NEAREST_EXACT),cv2.COLOR_BGR2GRAY)

    np_rezied_img=array(resized_image)/255

    # print(np_rezied_img.shape)
    
    # print(dir(model))

    # np_rezied_img.reshape((1,28*28))
    predicted_number=model.predict(np_rezied_img.reshape((1,28*28)))
    # print(argmax(predicted_number[0]))
    [print(i,' -- ',ele) for i,ele in enumerate(predicted_number[0])]
    most_close_ans=argmax(predicted_number[0])
    accurecy=predicted_number[0][most_close_ans]

    print(most_close_ans,accurecy,sep=' ---- ')
    ans.set(str(most_close_ans))

    lebal.config(text=f'Predict Answer:- {ans.get()}')

  except Exception as e:
    print(e)
    messagebox.showerror(title="error",message=str(e))



#bindings

button.bind('<Button-1>',button_click)


window.mainloop()