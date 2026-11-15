
import json
import uuid
import hashlib
from pathlib import Path
from datetime import datetime, timezone

DOSSIER_ARCHIVES = Path(__file__).parent / "archives"


def sauvegarder_recit(
    audio_bytes,
    nom_fichier,
    transcription,
    traduction,
    titre,
    region,
    autorisation_conservation
):
    if not autorisation_conservation:
        raise PermissionError(
            "La conservation de l'audio doit être autorisée."
        )

    if not audio_bytes:
        raise ValueError("Le fichier audio est vide.")

    identifiant = uuid.uuid4().hex
    dossier_recit = DOSSIER_ARCHIVES / identifiant
    dossier_recit.mkdir(parents=True, exist_ok=False)

    extension = Path(nom_fichier).suffix.lower()
    if extension not in {".mp3", ".wav", ".m4a", ".ogg", ".flac"}:
        raise ValueError("Format audio non autorisé.")

    chemin_audio = dossier_recit / ("audio_original" + extension)
    chemin_audio.write_bytes(audio_bytes)

    empreinte = hashlib.sha256(audio_bytes).hexdigest()

    metadonnees = {
        "id": identifiant,
        "titre": titre,
        "region": region,
        "nom_fichier_original": Path(nom_fichier).name,
        "date_sauvegarde_utc": datetime.now(timezone.utc).isoformat(),
        "transcription": transcription,
        "traduction_francaise": traduction,
        "sha256_audio": empreinte,
        "autorisation_conservation": True,
        "publication_autorisee": False
    }

    chemin_json = dossier_recit / "metadonnees.json"
    chemin_json.write_text(
        json.dumps(metadonnees, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    return identifiant
