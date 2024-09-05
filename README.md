# Access-Vision-FullProject


Ce repository contient le code source et les ressources pour le projet Access Vision

## Description

Le système se compose de deux principaux composants :

1. **Boîtier Raspberry Pi avec YOLO** : Un boîtier équipé d'une caméra et d'un Raspberry Pi, qui capture un flux vidéo et utilise un modèle YOLO pour détecter les obstacles en temps réel.
2. **Application mobile Ionic** : Une application mobile qui se connecte au Raspberry Pi via Bluetooth et fournit à l'utilisateur des instructions audio basées sur les informations reçues du boîtier.

L'objectif est d'améliorer la mobilité des utilisateurs en leur fournissant une analyse précise et rapide de leur environnement, réduisant ainsi les risques liés à la navigation.

## Structure du repository

- **raspberry/** : Ce dossier contient le code pour la détection d'obstacles exécuté sur le Raspberry Pi avec YOLO.

- **IonicApp/** : Ce dossier contient le code de l'application mobile Ionic.

- **dataset/** : Contient le dataset utilisé pour entraîner le modèle YOLO, les poids du modèle pré-entraîné, et un notebook expliquant le processus d'entraînement.

## Fonctionnalités principales

- **Détection d'obstacles** : Utilise YOLO pour détecter une large gamme d'obstacles en temps réel via la caméra du boîtier.
- **Instructions audio en temps réel** : Fournit des instructions audio détaillées via l'application mobile connectée.
- **Mobilité améliorée** : Réduit les incertitudes de navigation pour l'utilisateur, assurant une expérience de mobilité plus sûre.


---
