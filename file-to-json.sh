#!/bin/bash

if ! [ -x "$(command -v docker)" ]; then
  echo "Erreur : Docker n'est pas installé." >&2
  exit 1
fi

echo "Téléchargement de l'image Docker..."
docker pull zach27/file-to-json:latest

echo "Démarrage de l'application Streamlit..."
docker run -d -p 8585:8501 --name streamlit-app zach27/file-to-json:latest

echo "L'application Streamlit est maintenant disponible à l'adresse http://localhost:8585"