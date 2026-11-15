# DHIKRA-AI
# DHIKRA AI — ذكرى
### Préserver les voix du passé, transmettre la mémoire de demain.

**Projet développé dans le cadre du Hackathon IA Éthique 360°**

## 1. Présentation du projet

DHIKRA AI est une plateforme d'intelligence artificielle éthique dédiée à la préservation, à la valorisation et à l'accessibilité du patrimoine audiovisuel culturel du Maroc et du Maghreb.

Notre projet vise à faciliter la transcription, la traduction et la conservation des récits oraux, des témoignages, des contes traditionnels et des archives audiovisuelles.

DHIKRA AI place l'humain au cœur du processus, en associant l'intelligence artificielle à la validation humaine et à la protection des droits culturels.

## 2. Problématique

Le patrimoine oral maghrébin représente une richesse culturelle importante. Pourtant, de nombreux enregistrements audiovisuels sont difficiles à consulter, à comprendre ou à exploiter.

Plusieurs difficultés peuvent se présenter :

- Les enregistrements anciens ne disposent pas toujours de transcriptions.
- Les dialectes locaux, notamment la darija, peuvent être mal reconnus par les outils automatiques.
- L'absence de sous-titres limite l'accessibilité à certains publics.
- Les expressions culturelles et les proverbes risquent de perdre leur sens lors de la traduction.
- Les droits des personnes enregistrées et la provenance des archives doivent être respectés.

**Notre question centrale :**

Comment utiliser une intelligence artificielle éthique pour préserver et rendre accessible le patrimoine audiovisuel oral maghrébin, tout en respectant les langues, les cultures et les droits des créateurs ?

## 3. Notre solution

DHIKRA AI propose un processus de traitement des archives audiovisuelles :
1. Importation de l'enregistrement.
2. Remplissage de la fiche de provenance culturelle et déclaration des droits.
3. Calcul de l'empreinte SHA-256.
4. Transcription automatique avec Whisper.
5. Correction et validation humaine.
6. Téléchargement des résultats.

Notre approche repose sur un principe essentiel : **l'intelligence artificielle assiste les humains, mais ne remplace pas leur expertise culturelle.**

## 4. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Développement principal |
| Streamlit | Interface utilisateur |
| Whisper | Reconnaissance vocale et transcription |
| hashlib / SHA-256 | Vérification de l'intégrité des fichiers |
| GitHub | Collaboration et gestion du code |
| FFmpeg | Traitement des fichiers audio, si nécessaire |


## 5. Fonctionnalités du prototype

DHIKRA AI — ذكرى est un prototype d'intelligence artificielle éthique dédié à la préservation et à la valorisation du patrimoine oral et audiovisuel marocain et maghrébin.

### Fonctionnalités développées

- **Importation audio :** prise en charge des enregistrements aux formats MP3, WAV, M4A, OGG et FLAC.
- **Transcription automatique :** conversion de la parole en texte arabe à l'aide du modèle Whisper.
- **Correction humaine :** possibilité de vérifier et de modifier les transcriptions produites par l'IA.
- **Traduction française :** traduction des transcriptions arabes vers le français, avec possibilité de correction.
- **Exportation des textes :** téléchargement des transcriptions et des traductions.
- **Traçabilité :** génération d'une empreinte numérique SHA-256 et d'une fiche de provenance.
- **Consentement :** distinction entre l'autorisation de traitement par IA, l'autorisation de publication et l'autorisation de conservation.
- **Archivage local privé :** sauvegarde des enregistrements audio avec leurs métadonnées, leur transcription et leur traduction, sous réserve de vérification des données enregistrées.

### Fonctionnalités prévues

Le prototype sera progressivement enrichi avec :

- Une bibliothèque numérique permettant de consulter et de rechercher les récits sauvegardés.
- Un lecteur audio intégré pour écouter les archives.
- Un glossaire intelligent des expressions culturelles et des termes en darija.
- Des sous-titres synchronisés avec les enregistrements.
- Une carte interactive pour explorer les récits par région.
- L'exportation de fiches patrimoniales au format PDF.
- Des mécanismes de validation communautaire et de gestion des demandes de suppression.

### État du projet

DHIKRA AI est actuellement en phase de prototypage. Les principales fonctions de traitement audio et de traduction sont disponibles, tandis que l'archivage et les fonctionnalités de consultation font l'objet d'améliorations.

Le projet privilégie une approche centrée sur l'humain : les résultats de l'IA doivent pouvoir être vérifiés et corrigés, les autorisations doivent être respectées et les contenus ne doivent pas être publiés automatiquement.

L'objectif est de faire évoluer ce prototype vers une plateforme collaborative et responsable de préservation du patrimoine culturel.


### Limites actuelles

Le prototype utilise un modèle Whisper préentraîné.
La qualité de transcription dépend de la langue, de la qualité
sonore et des caractéristiques de l'enregistrement.

Une validation humaine reste nécessaire pour préserver
la fidélité linguistique et culturelle des récits.

## 6. Notre approche éthique à 360°

### Respect des créateurs
Les auteurs, conteurs et détenteurs des archives doivent être reconnus. L'IA ne doit pas effacer leur contribution.

### Droits et consentement
Les fichiers doivent être traités avec l'autorisation appropriée. Une archive ne doit pas être publiée sans vérification des droits applicables.

### Protection des données et provenance
Les informations personnelles et les enregistrements sensibles doivent être protégés. La provenance des archives doit être documentée autant que possible.

### Respect des cultures et des langues
Les dialectes, expressions traditionnelles et références culturelles doivent être préservés. Les transcriptions automatiques peuvent être corrigées par une personne compétente.

### Transparence
Les utilisateurs doivent savoir quelles parties du contenu ont été générées ou modifiées par l'IA. Les limites de reconnaissance de la darija doivent être clairement signalées.

### Responsabilité environnementale
Le projet privilégiera des modèles préentraînés, des traitements proportionnés et la limitation des calculs inutiles.

## 7. Sécurité et intégrité

DHIKRA AI utilise l'algorithme SHA-256 pour calculer l'empreinte numérique des fichiers audio importés. Cette empreinte permet de vérifier ultérieurement si le contenu d'un fichier a été modifié, en comparant les empreintes calculées.

**Limite importante :** SHA-256 ne prouve pas qu'un enregistrement est historiquement authentique ou qu'il a été obtenu avec consentement.

## 8. Public cible

DHIKRA AI s'adresse notamment :

- Aux associations culturelles.
- Aux musées et centres d'archives.
- Aux producteurs de documentaires.
- Aux chercheurs en patrimoine et en langues.
- Aux créateurs de contenus culturels.

## 9. Modèle économique envisagé

Nous envisageons un modèle combinant :

- Une offre gratuite limitée pour les particuliers et petites associations.
- Des abonnements professionnels pour les institutions culturelles.
- Des prestations de traitement d'archives pour les organismes disposant de collections audiovisuelles.

Ce modèle devra être validé auprès des utilisateurs potentiels.

## 10. Vision future

Notre ambition est de commencer par les récits oraux marocains, notamment en darija, puis d'étendre progressivement la plateforme à d'autres langues et variétés linguistiques du Maghreb.

Les évolutions envisagées comprennent la traduction assistée, les sous-titres synchronisés, la recherche dans les archives et l'enrichissement des métadonnées culturelles.


## 11. Installation et exécution

### Prérequis
- Python 3.12
- Git
- FFmpeg

### Installation

Cloner le dépôt :

```bash
git clone https://github.com/hibaelahmadi/DHIKRA-AI.git
cd DHIKRA-AI
```

Créer un environnement virtuel :

```bash
python -m venv .venv312
```

Activer l'environnement sous Windows PowerShell :

```powershell
.\.venv312\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

### Lancer l'application

```bash
python -m streamlit run app.py
```

Ouvrir l'adresse locale indiquée dans le terminal.

### Remarques

- Le modèle Whisper peut être téléchargé lors de sa première utilisation.
- La transcription peut prendre du temps selon la durée de l'audio et les performances de l'ordinateur.
- Les transcriptions automatiques doivent être vérifiées par une personne compétente, notamment pour la darija.
- Les utilisateurs doivent disposer des autorisations nécessaires pour traiter les enregistrements.

## 12. Équipe

Projet réalisé par une équipe de quatre développeuses ou développeurs dans le cadre du Hackathon IA Éthique 360°.

**DHIKRA AI — Chaque voix est une mémoire. Chaque mémoire mérite de vivre.**
