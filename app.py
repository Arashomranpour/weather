import requests
import streamlit as st

st.header("Weather app")
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    st.error("Set the OPENWEATHER_API_KEY environment variable.")
    st.stop()
city = st.text_input("Enter city: ") 

if city:  # بررسی اینکه ورودی city خالی نباشد
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    req = requests.get(url)
    response = req.json()

    st.write(response["weather"][0]["main"])
    st.write(response["main"]["temp"])
else:
    st.write("لطفاً یک شهر وارد کنید.")
