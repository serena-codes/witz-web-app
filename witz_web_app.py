import streamlit as st
import pyjokes
import random
import requests

st.set_page_config(page_title="Witz-Generator", page_icon="😄", layout="centered")

farben = ["#FFFAE3", "#E0FFFF", "#FFF0F5", "#F0FFF0"]
emojis = ["😄", "😎", "🙃", "😊"]

st.title("Lach mal wieder! 😄")
st.markdown("### Witz-Generator mit zwei Quellen")

# Lokale Witze (pyjokes)
if st.button("Witze anzeigen 😄"):
    farbe = random.choice(farben)
    emoji = random.choice(emojis)
    jokes = pyjokes.get_jokes(language='de', category='neutral')
    zufallswitze = random.sample(jokes, min(3, len(jokes)))
    st.markdown(f"""
        <div style='background-color:{farbe}; padding:15px; border-radius:10px;'>
            <h3 style='color:black;'>{emoji}</h3>
            <p style='color:black;'>{'<br><br>'.join(zufallswitze)}</p>
        </div>
    """, unsafe_allow_html=True)

# Online-Witze (WitzAPI.de)
if st.button("Zugabe? 🌐"):
    farbe = random.choice(farben)
    try:
        url = "https://witzapi.de/api/joke/?limit=1"
        response = requests.get(url, timeout=5)
        daten = response.json()
        if daten and "text" in daten[0]:
            witz = daten[0]["text"]
            st.markdown(f"""
                <div style='background-color:{farbe}; padding:15px; border-radius:10px;'>
                    <p style='color:black;'>{witz}</p>
                    <p style='color:gray;'>🌐 WitzAPI.de</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            raise ValueError("Keine Witze erhalten")
    except:
        fallback = "API nicht erreichbar – vielleicht ein Witz aus der Steckdose?"
        st.markdown(f"""
            <div style='background-color:{farbe}; padding:15px; border-radius:10px;'>
                <p style='color:black;'>{fallback}</p>
                <p style='color:gray;'>⚠️ Quelle: Offline</p>
            </div>
        """, unsafe_allow_html=True)
