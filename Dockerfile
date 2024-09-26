# Étape 1 : Utiliser une image Python officielle légère
FROM python:3.9-slim

# Étape 2 : Définir une variable d'environnement pour désigner l'environnement de production
ENV ENVIRONMENT=production

ENV DATABASE_URL=sqlite:////app/db_data/data.db
ENV DATABASE_URL_TEST=sqlite:////app/db_data/test_db.db

ENV SECRET_KEY=votre_secret_key
ENV ALGORITHM=HS256
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30

# Étape 3 : Définir un chemin par défaut pour stocker la base de données (modifiable via un argument)
ARG DB_PATH=/app/db
ENV DB_PATH=${DB_PATH}

# Étape 4 : Créer le répertoire pour stocker la base de données
RUN mkdir -p $DB_PATH

# Étape 5 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 6 : Copier les fichiers de dépendances (requirements.txt) dans le conteneur
COPY requirements.txt .

# Étape 7 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 8 : Copier le reste de l'application dans le conteneur
COPY . .

# Étape 9 : Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Étape 10 : Commande pour démarrer l'application avec uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]