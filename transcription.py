
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

def traduire_audio_anglais(audio_file):
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
            task="translate",
            language="ar",
            fp16=False
        )
        return resultat["text"]

    finally:
        if os.path.exists(chemin_audio):
            os.remove(chemin_audio)

from transformers import pipeline

@st.cache_resource
def charger_traducteur_francais():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-ar-fr",
        device=-1
    )

def traduire_texte_francais(texte_arabe):
    traducteur = charger_traducteur_francais()
    if not texte_arabe.strip():
        return ""

    mots = texte_arabe.split()
    morceaux = []
    morceau = []

    # Diviser le texte en petits groupes de mots
    for mot in mots:
        morceau.append(mot)

        if len(morceau) >= 30:
            morceaux.append(" ".join(morceau))
            morceau = []

    if morceau:
        morceaux.append(" ".join(morceau))

    traductions = []

    for partie in morceaux:
        resultat = traducteur(
            partie,
            max_length=256,
            truncation=True
        )

        traductions.append(
            resultat[0]["translation_text"]
        )

    return " ".join(traductions)
