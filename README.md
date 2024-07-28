# Projet MLOPS : Déploiement d'IA pour la retranscription d'audio

## Description

Ce projet a pour but de déployer des modèles d'intelligence artificielle spécialisés dans la retranscription audio en utilisant TensorFlow. Pour ce faire, une page web est exposée par un serveur Flask en Python, permettant une intégration aisée des modèles dans divers environnements embarqués. Ce projet a été réalisé dans le cadre du cursus de spécialisation en IA et Data, la majeure SCIA a EPITA dans le cadre des deux dernières années du cycle ingénieur. Nous avons passé ce Git en public, les projets pour cette matières étants libre et laissant cours à l'innovation et la curiosité des élèves, ne posant donc pas de soucis au bon déroulement de ce cours pour les futures années et pouvant même potentiellement inspirer des élèves à l'avenir à se lancer dans le développement d'IA pour des utilisations en embarqué. 

## Fonctionnalités

- **Retranscription Audio** : Les modèles d'IA traitent les fichiers audio pour fournir une retranscription textuelle.
- **API Web** : Interface accessible via HTTP pour interagir avec les modèles de retranscription.
- **Technologies Utilisées** : TensorFlow et TensorflowLite pour le traitement des modèles d'IA et Flask pour la gestion des requêtes API.
- **Matériel utilisé** : Raspberry Pi 4 Model B servant de support pour déployer les modeles de facon embarquée.   

## Architecture du Projet

- **Modèles TensorFlow** : 
  - `models/normal_model.h5` : Modèle TensorFlow au format HDF5.
  - `models/model_default.tflite` : Modèle TensorFlow Lite avec optimisation par défaut.
  - `models/model_experimental.tflite` : Modèle TensorFlow Lite expérimental.
  - `models/model_float16.tflite` : Modèle TensorFlow Lite optimisé en précision flottante 16 bits.
  - `models/model_no_opti.tflite` : Modèle TensorFlow Lite sans optimisation.

- **Serveur Flask** : Gère les requêtes HTTP et communique avec les modèles TensorFlow pour fournir des réponses.
- **API** : Permet aux utilisateurs de soumettre des fichiers audio et de recevoir des transcriptions en retour.

## Points de Terminaison API

- **`POST `** : Soumet un fichier audio pour retranscription. Le serveur renvoie le texte transcrit de l'audio. La réponse est ensuite affichée sur la page web directement.

===============================================================================================================================================================================================================

# MLOPS Project: Deployment of AI for audio transcription

## Description

This project aims to deploy artificial intelligence models specialized in audio transcription using TensorFlow. To do this, a web page is exposed by a Flask server in Python, allowing easy integration of models into various embedded environments. This project was carried out within the framework of the specialization course in AI and Data, the major SCIA has EPITA within the last two years of the engineering cycle. We’ve put this Git in public, the projects for this subject are free and open to innovation and curiosity of students, Thus, it does not pose any problems for the smooth running of this course for future years and may even potentially inspire students in the future to start developing AI for onboard uses. 

## Features

- **Audio Transcription** AI models process audio files to provide a textual transcription.
- **Web API** : Interface accessible via HTTP to interact with transcription templates.
- **Technologies Used** : TensorFlow and TensorflowLite for processing AI models and Flask for handling API requests.
- **Hardware used** : Raspberry Pi 4 Model B as a support for deploying embedded models. 

## Project Architecture

- **TensorFlow Templates**: 
  - ‘models/normal_model.h5’: TensorFlow template in HDF5 format.
  - ‘models/model_default.tflite’: TensorFlow Lite model with default optimization.
  - ‘models/model_experimental.tflite’: TensorFlow Lite experimental model.
  - ‘models/model_float16.tflite’: TensorFlow Lite model optimized for 16-bit floating accuracy.
  - ‘models/model_no_opti.tflite’: TensorFlow Lite model without optimization.
 
- **Flask Server** Manages HTTP requests and communicates with TensorFlow templates to provide responses.
- **API** Allows users to submit audio files and receive transcripts in return.

## API Endpoints

- **`POST `** Submits an audio file for transcription. The server returns the transcribed text of the audio. The answer is then displayed on the web page directly. 
