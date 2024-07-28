# Projet MLOPS : Déploiement d'IA pour la retranscription d'audio

## Description

Ce projet a pour but de déployer des modèles d'intelligence artificielle spécialisés dans la retranscription audio en utilisant TensorFlow. Pour ce faire, une API REST est exposée par un serveur Flask en Python, permettant une intégration aisée des modèles dans divers environnements embarqués.

## Fonctionnalités

- **Retranscription Audio** : Les modèles d'IA traitent les fichiers audio pour fournir une retranscription textuelle.
- **API RESTful** : Interface accessible via HTTP pour interagir avec les modèles de retranscription.
- **Technologies Utilisées** : TensorFlow pour le traitement des modèles d'IA et Flask pour la gestion des requêtes API.

## Architecture du Projet

- **Modèles TensorFlow** : Les modèles d'IA sont chargés et exécutés à l'aide de TensorFlow.
- **Serveur Flask** : Gère les requêtes HTTP et communique avec les modèles TensorFlow pour fournir des réponses.
- **API** : Permet aux utilisateurs de soumettre des fichiers audio et de recevoir des transcriptions en retour.

## Points de Terminaison API

- **`POST /transcribe`** : Soumet un fichier audio pour retranscription. Le serveur renvoie le texte transcrit de l'audio.

## Exemple de Réponse

```json
{
  "transcription": "Texte transcrit de l'audio..."
}
