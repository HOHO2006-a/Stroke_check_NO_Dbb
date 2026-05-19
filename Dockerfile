# Utiliser l'image officielle FrankenPHP (PHP 8.2)
FROM dunglas/frankenphp:php8.2

# Installer Python 3, Pip et les outils de compilation (requis pour SHAP)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Définir le dossier de travail
WORKDIR /app

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

# Copier le projet
COPY . .

# Définir les autorisations
RUN chown -R www-data:www-data /app && chmod -R 755 /app

# Configuration du port dynamique pour Railway
ENV PORT=80
EXPOSE 80

# Commande de démarrage : utilisation explicite de --listen pour le port de Railway
CMD ["sh", "-c", "frankenphp php-server --listen :${PORT}"]
