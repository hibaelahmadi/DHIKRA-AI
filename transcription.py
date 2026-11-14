
import whisper
import streamlit as st
import tempfile
import os


@st.cache_resource
def charger_modele():
    return whisper.load_model("base")


def transcrire_audio(audio_file):
    modele = charger_modele()

    extension = os.path.splitext(audio_file.name)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=extension
    ) as fichier_temporaire:
        fichier_temporaire.write(audio_file.getvalue())
        chemin_audio = fichier_temporaire.name

    try:
        resultat = modele.transcribe(
            chemin_audio,
            language="ar",
            fp16=False
        )
        return resultat["text"]
    finally:
        if os.path.exists(chemin_audio):
            os.remove(chemin_audio)
