
import hashlib

def calculer_sha256(audio_file):
    contenu = audio_file.getvalue()
    return hashlib.sha256(contenu).hexdigest()

