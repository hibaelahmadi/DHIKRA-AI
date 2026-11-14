
import streamlit as st
from transcription import transcrire_audio
from security import calculer_sha256
import json

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
    type=["mp3", "wav", "m4a" , "ogg", "flac"],
    disabled=not consent
)

if audio_file is not None and consent:
    st.success("Audio importé avec succès !")
    st.audio(audio_file)

    st.subheader("📜 Fiche de provenance culturelle")

    titre = st.text_input("Titre de l'enregistrement")

    region = st.text_input(
        "Région ou lieu d'origine",
        placeholder="Ex. : Marrakech, Maroc"
    )

    langue = st.selectbox(
        "Langue de l'enregistrement",
        ["Darija", "Amazigh", "Arabe", "Français", "Autre"]
    )

    contexte = st.text_area(
        "Contexte culturel ou historique"
    )

    source = st.text_input(
        "Source ou détenteur de l'enregistrement"
    )

    st.subheader("⚖️ Consentement et droits d'utilisation")

    statut_droits = st.selectbox(
        "Quel est votre statut concernant cet enregistrement ?",
        [
            "Je suis le créateur de l'enregistrement",
            "Je dispose d'une autorisation du détenteur des droits",
            "L'enregistrement est sous licence ouverte",
            "L'enregistrement est dans le domaine public",
            "Statut juridique incertain"
        ]
    )

    autorisation_ia = st.checkbox(
        "J'autorise le traitement de cet audio par l'IA pour la transcription."
    )

    autorisation_partage = st.checkbox(
        "J'autorise le partage public de cet enregistrement."
    )

    st.caption(
        "L'autorisation de transcription ne signifie pas "
        "une autorisation de publication ou de réutilisation."
    )


    st.caption(
        "Ces informations sont déclarées par la personne "
        "qui importe l'enregistrement et doivent être vérifiées."
    )

    st.subheader("🔐 Intégrité de l'enregistrement")

    empreinte = calculer_sha256(audio_file)


    fiche_provenance = {
        "titre": titre,
        "region_origine": region,
        "langue": langue,
        "contexte_culturel": contexte,
        "source": source,
        "nom_fichier_audio": audio_file.name,
        "empreinte_sha256": empreinte,
        "droits_declares": consent,
        "statut_droits": statut_droits,
        "autorisation_ia": autorisation_ia,
        "autorisation_partage": autorisation_partage
    }

    fiche_json = json.dumps(
        fiche_provenance,
        ensure_ascii=False,
        indent=4
    )

    st.download_button(
        label="📥 Télécharger la fiche de provenance",
        data=fiche_json,
        file_name="fiche_provenance_dhikra.json",
        mime="application/json"
    )


    st.write("Empreinte numérique SHA-256 :")
    st.code(empreinte)

    st.subheader("🧠 Transcription par IA")
    if not autorisation_ia:
        st.warning(
            "Vous devez autoriser le traitement par IA "
            "avant de lancer la transcription."
        )
    if st.button(
        "Transcrire avec Whisper",
        disabled=not autorisation_ia
    ):
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
