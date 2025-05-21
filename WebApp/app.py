import streamlit as st 
import os
import pickle
import pandas as pd
import re
def a_fun(y):
    return re.search(r'(.*?)(?=\.)',y).group(1).strip()

def ap(x):
    return x.map(a_fun)

def a_fun2(val):
    return "Rare" if val in ["Master","Dr","Rev","Major","Col","Mlle","Capt","Sir","Jonkheer","Mme","Don","Ms","Lady","the Countess"] else val


def ap2(x):
    return x.map(a_fun2)

f = os.path.join(os.path.dirname(__file__),'TitanicM.pkl')
with open(f,'rb') as t :
    P = pickle.load(t)

st.title("Titanic Data Explorer")

image_path = os.path.join(os.path.dirname(__file__), "titanic.jpg")
st.image(image_path)

st.divider()

st.header("Passenger Details")

Name = st.text_input("Name")


Pclass = st.selectbox(
    "Class",
    ("1st", "2nd", "3rd"),
    index=None,
    placeholder="Select Class...",
)

Sex = st.radio(
    "Gender",
    ("Male", "Female"),
    index=None,
)

Age = st.slider("Age",0,100)

Fare = st.slider("Fare",0,550)

Cabin = st.selectbox(
    "Cabin",
    ("A", "B","C","D","E", "F", "G", "T", "N"),
    index=None,
    placeholder="Select Cabin...",
)

Embarked = st.radio(
    "Embarked",
    ("S","C","Q"),
    index=None,
)

Family = st.radio(
    "Family",
    ("Alone", "Small","Big"),
    index=None,
)

if Sex == "Male":
    Sex = "male"
else:
    Sex = "female"

if Pclass!=None:
    Pclass = int(Pclass[0])

if st.button("Predict",type="secondary"):
    p = {"Pclass":[Pclass],
    "Name":[Name],
    "Sex":[Sex],
    "Age":[Age],
    "Fare":[Fare],
    "Cabin":[Cabin],
    "Embarked":[Embarked],
    "Family":[Family]}
    p = pd.DataFrame(p)
    ans = P.predict(p)
    if ans:
        st.badge("Survived", icon = "✅",color = "green")
        image_path1 = os.path.join(os.path.dirname(__file__), "boatfail.gif")
        st.image(image_path1)
    else:
        st.badge("Did not Survived", icon = "❌",color = "red")
        image_path2 = os.path.join(os.path.dirname(__file__), "goingdown.gif")
        st.image(image_path2)    
        