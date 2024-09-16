#!/bin/bash

if ! [ -x "$(command -v docker)" ]; then
  echo 'Erreur : Docker n\'est pas installé.' >&2
  exit 1
fi

IMAGE_NAME="zach27/file-to-json:latest"

echo "Téléchargement de l'image Docker..."
docker pull $IMAGE_NAME

echo "Démarrage de l'application Streamlit..."
docker run -d -p 8501:8501 --name streamlit-app $IMAGE_NAME

echo "L'application Streamlit est maintenant disponible à l'adresse http://localhost:8501"