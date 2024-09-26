
# Alim_gestion_v3 - Projet de Gestion des repas 

## Introduction
Alim_gestion_v3 est une application de gestion repas quotidien. Elle permet aux utilisateurs de suivre leurs repas, leurs consommation de calories, les activitiés physiques et leurs poids, les informations sont stockées dans une base de données.

## Structure du Projet
Le projet est structuré de manière modulaire pour faciliter le développement et la maintenance. Voici un aperçu de la structure actuelle :

```
alim_gestion_v3/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── meals.py
│   │           ├── ...
│   │           └── ...
│   ├── core/
│   |    ├── __init__.py
│   |    ├── config.py
│   |    └── sécurity.py
│   ├── db/
│   |    ├── __init__.py
│   |    ├── base.py
│   |    └── session.py
│   ├── models/
│   |    ├── __init__.py
│   |    ├── activity.py
│   |    ├── meal.py
│   |    └── ...
│   ├── repositories/
│   |    ├── __init__.py
│   |    ├── activity_repository.py
│   |    ├── meal_repository.py
│   |    └── ...
│   ├── schemas/
│   |    ├── __init__.py
│   |    ├── activity.py
│   |    ├── meal.py
│   |    └── ...
│   ├── services/
│   |    ├── __init__.py
│   |    ├── activity_service.py
│   |    ├── meal_service.py
│   |    └── ...
│   ├── routes/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── meals.py
│   │       │   └── ...
│   │       ├── auth.py
│   │       └── middleware.py
│   ├── templates/
│   |    ├── base.html
│   |    ├── index.html
│   |    └── ...
│   └── static/
│       ├── styles.css
│       └── ...
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── api/
│   │   └── v1/
│   │       ├── test_activities_api.py
│   │       └── ...
│   ├── repositories/
│   │   ├── test_activity_repository.py
│   │   └── ...
│   └── services/
│       ├── test_activity_repository.py
│       └── ...
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── docker-compose.yml
├── run_me.sh
└── Dockerfile
```

## Installation
Pour installer le projet en local, suivez les étapes ci-dessous :

1. Clonez le dépôt GitHub :
   ```
   git clone https://github.com/votre-utilisateur/bolo_kono.git
   ```

2. Accédez au répertoire du projet :
   ```
   cd alim_gestion_v3
   ```

3. Créez et activez un environnement virtuel :
   ```
   python -m venv ENV
   source ENV/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

4. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

5. Configurez les variables d'environnement dans un fichier `.env` :
   ```
   # Exemple de fichier .env
   ENVIRONMENT=production
   DATABASE_URL=sqlite:///./data.db
   DATABASE_URL_TEST=sqlite:///./app/db/dev.db

   SECRET_KEY=votre_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. Démarrez l'application :
   ```
   uvicorn app.main:app --reload
   ```
   ou en executant le script run_me.sh
   ```
   sh run_me.sh # sur un terminal bash
   ```
## Déploiement en utilisant Docker
1. Création de l'image Docker :
   ```
   docker build -t alim_gestion_v3 .
   ```
2. Lancer le conteneur Docker :
   ```
   docker run -d -p 8000:8000 --name alim_gestion alim_gestion_v3:latest
   ```

## Contribution et Gestion des Pull Requests

### Branches
- **main** : Contient le code de production stable.
- **develop** : Utilisé pour le développement général, contient le code en cours de développement.
- **feature/nom-de-la-fonctionnalité** : Chaque nouvelle fonctionnalité doit être développée dans une branche feature dédiée.

### Règles pour les Pull Requests
1. **Créer une Pull Request (PR)** : Lorsque vous avez terminé de travailler sur une fonctionnalité dans une branche feature, créez une PR pour fusionner cette branche dans `develop`.

2. **Respecter les Conventions de Codage** : Le code doit respecter les conventions de style Python (PEP8). Utilisez des outils comme `flake8` pour vérifier votre code.

3. **Ajouter des Tests** : Assurez-vous d'avoir ajouté des tests unitaires pour toute nouvelle fonctionnalité ou modification.

4. **Exécution des Tests** : Avant de soumettre une PR, exécutez tous les tests pour vous assurer que rien n'est cassé :
   ```
   pytest --cov=app tests/
   ```

5. **Revue de Code** : Chaque PR doit être revue par au moins un autre membre de l'équipe avant d'être fusionnée. La revue doit inclure :
   - Vérification de la qualité du code.
   - Vérification que les tests sont complets et passent correctement.
   - Validation que les fonctionnalités ajoutées répondent aux exigences.

6. **Résolution des Conflits** : Si des conflits surviennent lors de la fusion, ils doivent être résolus avant la validation de la PR.

7. **Merge** : Une fois la PR approuvée et les conflits résolus, elle peut être fusionnée dans `develop`. Ne fusionnez pas directement dans `master` sans passer par `develop`.

## Documentation
La documentation complète sur l'architecture du projet, les fonctionnalités, et les instructions pour les développeurs sera mise à jour au fur et à mesure que le projet avance.

## Exemple de Commits Suivants Cette Version
**Ajoute la gestion des revenus**
**Corrige l'erreur de calcul dans le tableau de bord**
**Supprime le code obsolète**
**Modifie le formulaire de connexion**
**Met à jour la documentation**

## Version
**Version 0.0.0** - Sprint Zéro du projet "Lancement"
