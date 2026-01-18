import streamlit as st

st.title("Mini-Übersetzer mit Erklärungen")

text = st.text_area("Text eingeben")

if st.button("Übersetzen"):
    st.write("Übersetzung kommt hier")
    st.write("Erklärung kommt hier")
