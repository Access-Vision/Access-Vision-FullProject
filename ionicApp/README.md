# Application mobile Access Vision 

Ce repository contient le code source de l'application mobile Ionic pour le projet Access Vision.

## Description

L'application mobile se connecte au boîtier Raspberry Pi via Bluetooth et fournit à l'utilisateur des instructions audio basées sur les informations reçues du boîtier. 
Elle est conçue pour améliorer la mobilité des utilisateurs en leur fournissant une analyse précise et rapide de leur environnement, réduisant ainsi les risques liés à la navigation.

## Fonctionnalités principales

- **Connectivité Bluetooth** : Se connecte au boîtier Raspberry Pi pour recevoir des informations sur les obstacles détectés.
- **Instructions audio en temps réel** : Fournit des instructions audio détaillées basées sur les informations reçues du boîtier Raspberry Pi.
- **Interface utilisateur intuitive** : Conçue pour une utilisation facile et intuitive, même pour les utilisateurs novices.

## Installation

Pour installer l'application mobile, suivez les étapes suivantes :



1. Clonez ce repository sur votre machine locale.
2. Vérifier que Node.js et Ionic sont installés sur votre machine. Si ce n'est pas le cas, vous pouvez les installer en suivant les instructions sur les sites officiels de [Node.js](https://nodejs.org/) et [Ionic](https://ionicframework.com/).
3. Ouvrez un terminal dans le dossier `ionicApp/accessVision` et exécutez la commande `npm install --legacy-peer-deps` pour installer les dépendances du projet.
4. Exécutez la `commande npx cap open android` pour ouvrir le projet dans Android Studio.
5. Compilez et exécutez l'application sur un émulateur ou un appareil Android.