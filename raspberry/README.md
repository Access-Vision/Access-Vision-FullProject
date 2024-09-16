# Raspberry Pi avec YOLO

Ce repository contient le code pour la détection d'obstacles exécuté sur le Raspberry Pi avec YOLO.

## Description

Le boîtier Raspberry Pi est équipé d'une caméra qui capture un flux vidéo en temps réel. \
Lorsque le boitier démarre, il lance un fichier Python qui écoute les messages Bluetooth envoyés par l'application mobile permettant de lancer ou stopper la détection d'objet.\
Le modèle YOLO (You Only Look Once) est utilisé pour détecter les obstacles dans le champ de vision de la caméra à l'aide d'un modèle que nous avons entrainé. \
Les informations sur les obstacles détectés sont envoyées à l'application mobile via Bluetooth pour fournir des instructions audio à l'utilisateur. 

## Fonctionnalités principales

- **Connectivité Bluetooth** : Se connecte à l'application mobile pour recevoir des instructions de démarrage et d'arrêt de la détection d'obstacles.
- **Détection d'obstacles** : Utilise YOLO pour détecter une large gamme d'obstacles en temps réel via la caméra du boîtier.


## Installation

Pour installer le code sur le Raspberry Pi, suivez les étapes suivantes :
- Clonez ce repository sur votre Raspberry Pi.
- Installer les dépendances nécessaires en exécutant la commande `pip install -r requirements.txt`.
- Assurez-vous que le Raspberry Pi est correctement configuré avec la caméra et le Bluetooth.
- Lancez le script Python avec la commande `python yolo.py`.

- Pour lancer le script au démarrage du Raspberry Pi, vous pouvez effectuer la commande  `crontab -e` et ajouter la ligne suivante : \
`@reboot /usr/bin/python3 /path/to/raspberry/yolo.py >> /path/to/logsCrontab.log 2>&1`