import streamlit as st
import json
import random

# ---------------- CONFIGURACIÓN DE LA PÁGINA ----------------
st.set_page_config(
    page_title="Quiz de Calidad",
    page_icon="✅",
    layout="centered"
)

# ---------------- ENCABEZADO ----------------
st.title("🧪 Quiz de Calidad")
st.caption("Proyecto Final · Fundamentos de Programación · Ingeniería Industrial")
st.divider()

# ---------------- CARGA DE PREGUNTAS ----------------
with open("preguntas.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

# ---------------- ESTADO INICIAL ----------------
if "preguntas_seleccionadas" not in st.session_state:
    st.session_state.preguntas_seleccionadas = random.sample(preguntas, 4)
    st.session_state.puntaje = 0
    st.session_state.pregunta_actual = 0

# ---------------- QUIZ ----------------
if st.session_state.pregunta_actual < 4:
    p = st.session_state.preguntas_seleccionadas[st.session_state.pregunta_actual]

    # Barra de progreso
    st.progress((st.session_state.pregunta_actual + 1) / 4)

    st.subheader(p["pregunta"])
    opcion = st.radio(
        "Selecciona una opción:",
        p["opciones"],
        key=st.session_state.pregunta_actual
    )

    if st.button("Responder"):
        if opcion == p["respuesta"]:
            st.success("✅ Correcto")
            st.session_state.puntaje += 1
        else:
            st.error("❌ Incorrecto")

        st.session_state.pregunta_actual += 1
        st.rerun()

# ---------------- RESULTADO FINAL ----------------
else:
    st.divider()
    st.subheader("📊 Resultado final")

    calificacion = (st.session_state.puntaje / 4) * 10

    st.metric(
        label="Calificación",
        value=f"{calificacion:.1f} / 10",
        delta=f"{st.session_state.puntaje} de 4 correctas"
    )

    if st.button("🔄 Reiniciar"):
        st.session_state.clear()
        st.rerun()

# -------------
