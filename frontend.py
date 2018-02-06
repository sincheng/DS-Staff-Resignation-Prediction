from tkinter import *
import backend
from tkinter import filedialog
from tkinter import StringVar
import pandas as pd
from pandastable import Table

def model_command():
    global df_train
    csv_file_path = filedialog.askopenfilename(filetypes=[('.csvfiles', '.csv')])
    df_train = pd.read_csv(csv_file_path)
    backend.save_model(df_train)
    var = "Model Trained!!"
    l2.config(text=var)

def import_command():
    global df
    csv_file_path = filedialog.askopenfilename(filetypes=[('.csvfiles', '.csv')])
    df = pd.read_csv(csv_file_path)
    records= len(df)
    var = "Import Success!!" + str(records) + " records imported!"
    l2.config(text=var)

def run_command():
    global df_left
    df_left = backend.run_model(df);
    var = "Run Model!!" + str(len(df_left)) +" staff are predicted to be left"
    l2.config(text=var)

def export_command():
    df_left.to_csv('left.csv')
    var = "Exported!"
    l2.config(text=var)

window=Tk()
frame = Frame(window)
# frame.grid(row=1,column=2)
#rightframe = Frame(window)
# rightframe.pack(side = RIGHT)

window.wm_title("Staff Resign Prediction App")
window.minsize(300,180)
#Label
# l1=Label(window,text="Functions")
# l1.pack()

l2=Label(window,text="Status: Train the model")
l2.pack()

#Model Button
b1=Button(window,text="Train Model",width=12,command=model_command)
b1.pack()

#Import Button
b2=Button(window,text="Import CSV",width=12,command=import_command)
b2.pack()

#Run Button
b3=Button(window,text="Run",width=12,command=run_command)
b3.pack()

b4=Button(window,text="Export",width=12,command=export_command)
b4.pack()

# b5=Button(window,text="Email",width=12,command=email_command)
# b5.pack()

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.pack()

#List to view staff record
# list1=Listbox(window,height=7,width=50)
# list1.grid(row=2,column=1,rowspan=5,columnspan=10)
#
# sb1=Scrollbar(window)
# sb1.grid(row=2,column=2,rowspan=6)
#
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

window.mainloop()
