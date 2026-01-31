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

TOTAL_PREGUNTAS_POR_PARTIDA = 4

# ---------------- ESTADO INICIAL ----------------
if "preguntas_seleccionadas" not in st.session_state:
    st.session_state.preguntas_seleccionadas = random.sample(preguntas, TOTAL_PREGUNTAS_POR_PARTIDA)
    st.session_state.puntaje = 0
    st.session_state.pregunta_actual = 0

# ---------------- QUIZ ----------------
if st.session_state.pregunta_actual < TOTAL_PREGUNTAS_POR_PARTIDA:
    idx = st.session_state.pregunta_actual
    p = st.session_state.preguntas_seleccionadas[idx]

    # Contador + restantes
    numero_pregunta = idx + 1
    restantes = TOTAL_PREGUNTAS_POR_PARTIDA - numero_pregunta
    st.markdown(f"### Pregunta {numero_pregunta} de {TOTAL_PREGUNTAS_POR_PARTIDA}")
    st.caption(f"Te quedan {restantes} por responder.")
    
    # Progreso
    st.progress(numero_pregunta / TOTAL_PREGUNTAS_POR_PARTIDA)
    st.divider()

    st.subheader(p["pregunta"])
    opcion = st.radio(
        "Selecciona una opción:",
        p["opciones"],
        key=f"q_{idx}"
    )

    if st.button("Responder"):
        if opcion == p["respuesta"]:
