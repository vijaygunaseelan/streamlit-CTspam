import pickle 
import streamlit as st
from win32com.client import Dispatch

def speak(text):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)


sp=pickle.load(open('spamtech.pkl','rb'))
cv1=pickle.load(open('spamvectorizer.pkl','rb'))




def main()
    st.title("CTS")
    st.subheader("Build with streamlit & Python")
    msg=st.text_input("Enter a Text ")
    if st.button("Predict"):
        data=[msg]
        vect=cv1.transform(data).toarray()
        prediction=model.predict(vect)
        result=prediction[0]
        if result==1:
            st.error("This is a spam mail")
            speak("This is a spam mail")
        else:
            st.success("This is a Ham mail")



main()
