import pickle 
import streamlit as st
from win32com.client import Dispatch





def speak(text):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(text) 




model=pickle.load(open('tiwari.pkl','rb'))
cv1=pickle.load(open('ctvectorizer.pkl','rb'))




def main():
    st.title("CHADURATECHSPAM")
    st.subheader("SPAM or HAM")
    message=st.text_input("Enter a Text ")
    if st.button("Predict"):
        data=[message]
        vect=cv1.transform(data).toarray()
        
        
        prediction=model.predict(vect)
       
        #st.write(prediction)
        
        result=prediction[0]
        if result==1:
            st.error("This is a spam mail")
            speak("This is a spam mail")
        else:
            st.success("This is a Ham mail")
            speak("This is a Ham mail")
    


  
main()
