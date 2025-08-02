import streamlit as st
def ejecutar_test_condiciones_clinicas():
    st.subheader("Módulo 3: Condiciones Clínicas Opcionales")
    sintomas = [
        "Cansancio crónico", "Hinchazón digestiva", "Dolor muscular frecuente",
        "Cambios hormonales", "Enfermedades frecuentes", "Ansiedad constante"
    ]
    resultados = {}
    for sintoma in sintomas:
        resultados[sintoma] = st.radio(sintoma, [1, 2, 3], key=sintoma)
    if st.button("Guardar resultado condiciones clínicas"):
        st.success("Datos guardados")
