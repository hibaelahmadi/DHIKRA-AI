
import streamlit as st
from transcription import transcrire_audio

st.set_page_config(
    page_title="DHIKRA AI",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ DHIKRA AI — ذكرى")

st.write(
    "Préserver les voix du passé, "
    "transmettre la mémoire de demain."
)

st.divider()

st.subheader("📂 Importer un enregistrement audio")

consent = st.checkbox(
    "Je confirme disposer des droits nécessaires "
    "pour traiter cet enregistrement."
)

audio_file = st.file_uploader(
    "Choisissez un fichier audio",
    type=["mp3", "wav", "m4a"],
    disabled=not consent
)

if audio_file is not None and consent:
    st.success("Audio importé avec succès !")
    st.audio(audio_file)

    st.subheader("🧠 Transcription par IA")

    if st.button("Transcrire avec Whisper"):
        with st.spinner(
            "Transcription en cours, veuillez patienter..."
        ):
            try:
                texte = transcrire_audio(audio_file)
                st.session_state["transcription"] = texte
            except Exception as erreur:
                st.error(f"Erreur : {erreur}")

    if "transcription" in st.session_state:
        texte_corrige = st.text_area(
            "Corrigez la transcription si nécessaire :",
            value=st.session_state["transcription"],
            height=200
        )

        st.download_button(
            "📥 Télécharger la transcription",
            data=texte_corrige,
            file_name="transcription_dhikra.txt",
            mime="text/plain"
        )

st.divider()

st.caption(
    "DHIKRA AI — Intelligence artificielle "
    "éthique et patrimoine audiovisuel maghrébin"
)
