import streamlit as st
import json
import random

st.title("Quiz de Calidad - Guersom Arroyo")

with open("preguntas.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

if "preguntas_seleccionadas" not in st.session_state:
    st.session_state.preguntas_seleccionadas = random.sample(preguntas, 4)
    st.session_state.puntaje = 0
    st.session_state.pregunta_actual = 0

if st.session_state.pregunta_actual < 4:
    p = st.session_state.preguntas_seleccionadas[st.session_state.pregunta_actual]

    st.subheader(p["pregunta"])
    opcion = st.radio("Selecciona una opción:", p["opciones"])

    if st.button("Responder"):
        if opcion == p["respuesta"]:
            st.session_state.puntaje += 1
        st.session_state.pregunta_actual += 1
        st.rerun()
else:
    calificacion = (st.session_state.puntaje / 4) * 10
    st.success(f"Puntaje obtenido: {st.session_state.puntaje}/4")
    st.info(f"Calificación final: {calificacion:.1f}")

    if st.button("Reiniciar"):
        st.session_state.clear()
        st.rerun()
