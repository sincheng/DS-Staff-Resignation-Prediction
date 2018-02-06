import pandas as pd
from tkinter import StringVar
from tkinter import filedialog
from tkinter import *
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
import numpy


def run_model(df):
    df = df.rename(columns={ 'sales' : 'department'})
    lb = LabelEncoder()
    df['department'] = lb.fit_transform(df.department)
    df['salary'] = lb.fit_transform(df.salary)
    cart = joblib.load('cart.pkl')
    predicted_cart = cart.predict(df)
    df['predict'] = predicted_cart
    df_left = df.loc[df['predict'] == 1]

    # unique, counts = numpy.unique(predicted_cart, return_counts=True)
    # print(dict(zip(unique, counts)))
    print(len(df_left))
    return df_left

def save_model(df):
    # csv_file_path = filedialog.askopenfilename(filetypes=[('.csvfiles', '.csv')])
    # df = pd.read_csv(csv_file_path)
    df = df.rename(columns={ 'sales' : 'department'})
    lb = LabelEncoder()
    df['department'] = lb.fit_transform(df.department)
    df['salary'] = lb.fit_transform(df.salary)
    is_test = np.random.uniform(0, 1, len(df)) > 0.7
    train = df[is_test==False]
    test = df[is_test==True]
    x = train.drop("left",1)
    y = train.left
    cart = DecisionTreeClassifier()
    cart.fit(x,y)
    joblib.dump(cart,'cart.pkl')
