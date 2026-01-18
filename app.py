import streamlit as st
from translator import translate
from explainer import explain
from level_estimator import estimate_level_grammar


st.title("Mini-Übersetzer mit Erklärungen")

text = st.text_area("Text eingeben", height=150)

if st.button("Übersetzen"):
    translation = translate(text)
    explanation = explain(text, translation)

    st.subheader("Übersetzung")
    st.write(translation)

    st.subheader("Erklärung")
    st.write(explanation)

