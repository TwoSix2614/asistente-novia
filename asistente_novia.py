import streamlit as st
import random
import datetime

# Configuracion de la pagina web
st.set_page_config(page_title="Tu Asistente para que no me olvides", page_icon="💝", layout="centered")

# Frases personalizadas
CUMPLIDOS = [
    "Eres perfecta y cada detalle te hace unica. 😍",
    "Tu sonrisa ilumina perfectamente mi dia entero.",
    "¿Ya te dije hoy que tienes los ojos mas hermosos del mundo?",
    "Me encanta tu forma de ser y eres la mejor.",
    "Eres mi persona favorita in el mundo. 🌍❤️"
]

PLANES_MOMENTOSJUNTOS = [
    "🦅 Ver el partido del america y burlarnos de lo que pasa.",
    "🎵 Hacer Jam y escuchar juntos a tus cantantes favoritos.",
    "🥂 Tomar juntos, tu un 4 loko y yo agua.",
    "🎮 Jugar minecraft juntos, los dos aprendemos juntos.",
    "📱 Hacer llamada para pasar el rato y hacerle compañia."
]

# Titulo de la pagina
st.title("💖 ¡Hola, Mi Amor! Bienvenida a tu asistente personal")
st.write(f"Hoy es **{datetime.date.today().strftime('%d/%m/%Y')}** y es un dia perfecto para recordarte cuanto te amo.")

st.divider()

# Seccion de cumplidos
st.subheader("🌸 ¿Necesitas una sonrisa?")
if st.button("¡Haz clic aqui para recibir un cumplido!"):
    cumplido_aleatorio = random.choice(CUMPLIDOS)
    st.balloons()
    st.success(cumplido_aleatorio)

st.divider()

# Seccion del momento juntos
st.subheader("✨ Elige el momento juntos de hoy")
st.write("¿No sabes que elegir? Deja que el destino decida por ti:")
if st.button("Generar idea de momento aleatoria"):
    momento_elegido = random.choice(PLANES_MOMENTOSJUNTOS)
    st.info(f"El universo dice que hoy deberiamos hacer: **{momento_elegido}**")

st.divider()

# Seccion del mensaje secreto (Codigo: 18/08)
st.subheader("🔒 Tu buzon de mensajes secretos")
codigo = st.text_input("Introduce nuestra fecha de aniversario (ejemplo: 18/08) para abrir tu carta:")

if codigo == "18/08": 
    st.markdown("""
    ### 💌 Mi carta para ti:
    *Hola mi amor, hice este pequeño programa pensado en ti para sacarte una sonrisa.* 
    *Gracias por ser mi novia, mi mundo y el amor de mi vida.*
    *Te amo desde el primer dia y eso siempre sera asi. ❤️*
    """)
elif codigo != "":
    st.error("Codigo incorrecto... ¡Pidele una pista a tu novio! 🕵️‍♂️")
