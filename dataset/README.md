
---

# Projet de Détection d'Obstacles avec YOLO

## Description du Projet

Ce projet utilise un modèle YOLO (You Only Look Once) pour détecter des obstacles dans un environnement urbain, tels que des poteaux, poubelles, escaliers, et autres objets couramment rencontrés. Le modèle est exécuté sur un ensemble d'images et les résultats de la détection sont sauvegardés dans différents sous-dossiers (`predict`, `predict2`, `predict3`, etc.). 

Ce dépôt contient :
- Un modèle YOLO (`best.pt`) pré-entraîné pour détecter des obstacles.
- Un notebook Python qui permet de télècharger le dataset, tester des images, et visualiser les obstacles détectés


## Structure du doosier

- **AccessVision_Dataset_notebook.ipynb** : Contient le notebook pour la visualisation des résultats de détection.

- **best.pt** : le modèle entrainé sur le dataset télèchargeable depuis le notebook pour reconnaistre les obstacles : escaliers, poteaux, poubelles


#### Étapes pour utiliser le notebook :
1. Ouvrez le notebook `AccessVision_Dataset_notebook.ipynb`.
2. Exécutez les cellules. Importez le poids best.pt. Le notebook chargera automatiquement les images des sous-dossiers dans `runs/detect/` et les affichera. 
3. Les images seront affichées en une seule colonne, une image par sous-dossier.

### 3. Sélection Aléatoire d'Images

Le notebook est conçu pour sélectionner aléatoirement des images dans les dossiers prédits et les afficher dans une colonne. Cela vous permet de vérifier les résultats de la détection sans avoir à parcourir manuellement chaque sous-dossier.

### 4. Gestion des Sous-dossiers

Chaque fois que vous exécutez la détection YOLO, les résultats sont enregistrés dans un nouveau dossier sous `runs/detect/` avec des noms comme `predict`, `predict2`, `predict3`, etc. Le notebook permet d'explorer ces sous-dossiers automatiquement et d'afficher une image de chaque dossier.



---

