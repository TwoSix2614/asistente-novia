cat << 'EOF' > lienzo_pao.py
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuracion de la pagina
st.set_page_config(page_title="Nuestro Lienzo de Arte 🎨", page_icon="🖌️", layout="centered")

st.title("🎨 ¡Dibuje algo que me lo quiero tatuar!")
st.write("¡Hola mi niña! Hice este espacio para que podamos dibujar juntos. Puedes usar el mouse o tu dedo en el celular para pintar lo que quieras en la cuadricula.")

st.divider()

# Selector de herramientas en la barra lateral
st.sidebar.header("🛠️ Herramientas de Arte")
color_elegido = st.sidebar.color_picker("Elige tu color para pintar:", "#FF4B4B")
grosor_pincel = st.sidebar.slider("Grosor del pincel:", 5, 30, 15)
herramienta = st.sidebar.selectbox("Herramienta:", ("freedraw", "rect", "circle", "transform"))

st.sidebar.divider()
st.sidebar.markdown("""
### 💡 Ideas para dibujar hoy:
* 🥂 ¡Un 4 loko!
* 🦅 El logo del America (o un intento).
* 💘 Algo que reprsente tus gustos.
""")

# Crear el lienzo interactivo
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno para formas
    stroke_width=grosor_pincel,
    stroke_color=color_elegido,
    background_color="#FFFFFF", # Fondo blanco limpio
    height=400,
    width=500,
    drawing_mode=herramienta,
    key="lienzo_amor",
)

st.divider()

# Interaccion especial: Guardar o dedicar el dibujo
st.subheader("💌 Guarda nuestra obra de arte")
nombre_obra = st.text_input("Dale un titulo a nuestro dibujo:", "Momento Juntos ❤️")

if st.button("✨ Dedicar este dibujo"):
    st.balloons()
    st.success(f"¡Obra '{nombre_obra}' guardada con exito en el corazon de Edu! Gracias por pintar conmigo, mi amor. 🥰🎨")
EOF
