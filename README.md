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

1. Importation d'un fichier audio autorisé.
2. Transcription automatique à l'aide de l'intelligence artificielle.
3. Correction et validation humaine de la transcription.
4. Préparation de traductions et de sous-titres pour améliorer l'accessibilité.
5. Calcul d'une empreinte numérique pour contrôler l'intégrité du fichier.
6. Gestion progressive des informations de provenance et d'autorisation.

Notre approche repose sur un principe essentiel : **l'intelligence artificielle assiste les humains, mais ne remplace pas leur expertise culturelle.**

## 4. Technologies envisagées

| Technologie | Utilisation |
|---|---|
| Python | Développement principal |
| Streamlit | Interface utilisateur |
| Whisper | Reconnaissance vocale et transcription |
| hashlib / SHA-256 | Vérification de l'intégrité des fichiers |
| GitHub | Collaboration et gestion du code |
| FFmpeg | Traitement des fichiers audio, si nécessaire |

## 5. Fonctionnalités du prototype

Les fonctionnalités prévues pour le premier prototype sont :

- Importer un fichier audio.
- Écouter l'enregistrement importé.
- Générer une transcription automatique.
- Corriger manuellement la transcription.
- Calculer l'empreinte SHA-256 du fichier.
- Demander la confirmation des droits d'utilisation.

**État du projet :** prototype en cours de développement. Les fonctionnalités mentionnées ci-dessus sont des objectifs techniques et ne sont pas toutes encore implémentées.

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

DHIKRA AI prévoit d'utiliser l'algorithme SHA-256 pour calculer l'empreinte numérique d'un fichier.

Cette empreinte permet de détecter une modification du fichier en comparant deux valeurs calculées à différents moments.

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

Les instructions d'installation seront complétées après la mise en place du premier prototype.

Technologies prévues : Python et Streamlit.

## 12. Équipe

Projet réalisé par une équipe de deux développeuses ou développeurs dans le cadre du Hackathon IA Éthique 360°.

**DHIKRA AI — Chaque voix est une mémoire. Chaque mémoire mérite de vivre.**
