import streamlit as st
import pyjokes
import random
import requests

st.set_page_config(page_title="Witz-Generator", page_icon="😄", layout="centered")

farben = ["#FFFAE3", "#E0FFFF", "#FFF0F5", "#F0FFF0"]
emojis = ["😄", "😎", "🙃", "😊"]

# Kleinere Hauptüberschrift
st.markdown("<h2 style='text-align:center; margin-bottom:10px;'>Lach mal wieder! 😄</h2>", unsafe_allow_html=True)

# Ausgewogene Zwischenüberschrift
st.markdown("<h4 style='text-align:center; margin-bottom:20px;'>Witz-Generator mit zwei Quellen</h4>", unsafe_allow_html=True)

# Größere Buttons mit Abstand
col1, col2 = st.columns(2)
with col1:
    if st.button("😄 Witze anzeigen", use_container_width=True):
        farbe = random.choice(farben)
        emoji = random.choice(emojis)
        jokes = pyjokes.get_jokes(language='de', category='neutral')
        zufallswitze = random.sample(jokes, min(3, len(jokes)))
        st.markdown(f"""
            <div style='background-color:{farbe}; padding:15px; border-radius:10px; margin-top:20px;'>
                <h3 style='color:black;'>{emoji}</h3>
                <p style='color:black; font-size:18px;'>{'<br><br>'.join(zufallswitze)}</p>
            </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("🌐 Zugabe?", use_container_width=True):
        farbe = random.choice(farben)
        try:
            url = "https://witzapi.de/api/joke/?limit=1"
            response = requests.get(url, timeout=5)
            daten = response.json()
            if daten and "text" in daten[0]:
                witz = daten[0]["text"]
                st.markdown(f"""
                    <div style='background-color:{farbe}; padding:15px; border-radius:10px; margin-top:20px;'>
                        <p style='color:black; font-size:18px;'>{witz}</p>
                        <p style='color:gray;'>🌐 WitzAPI.de</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                raise ValueError("Keine Witze erhalten")
        except:
            fallback = "API nicht erreichbar – vielleicht ein Witz aus der Steckdose?"
            st.markdown(f"""
                <div style='background-color:{farbe}; padding:15px; border-radius:10px; margin-top:20px;'>
                    <p style='color:black; font-size:18px;'>{fallback}</p>
                    <p style='color:gray;'>⚠️ Quelle: Offline</p>
                </div>
            """, unsafe_allow_html=True)
