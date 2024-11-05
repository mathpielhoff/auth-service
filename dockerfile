# Utiliser l'image officielle Python
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY ./src /app/src
COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Commande pour démarrer l'application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
