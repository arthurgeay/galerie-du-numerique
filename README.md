# La Galerie du Numerique

URL : https://galerie-numerique.herokuapp.com/

Admin : https://galerie-numerique.herokuapp.com/admin

Login : https://galerie-numerique.herokuapp.com/login


## Installation

```sh
# Créer l'environnement virtuel
python -m venv env

# Rentrer dans l'environnement virtuel
# Linux/MacOS :
source env/bin/activate

# Windows
env/Scripts/Activate.ps1

# Installer les dépendances
 pip install -r requirements.txt

# Se déplacer dans le dossier du projet
cd artwork_gallery_project

# Base de données - Ce projet utilise PostgreSQL

# Vous pouvez utiliser Docker avec docker-compose.
docker-compose up -d

# OU si vous n'avez pas Docker, créez une nouvelle base de donnée
CREATE DATABASE galerie_numerique; 

# Créer un fichier de variable d'environnement et remplir les différentes valeurs en fonction de vos réglages
cp .env.example .env

# Example du fichier .env si vous utilisez docker-compose
DB_HOST=localhost  
DB_NAME=postgres  
DB_USER=postgres  
DB_PASSWORD=root  
DB_PORT=5432  
DEBUG=True
EMAIL_USER=
EMAIL_PASSWORD=
MEDIAWIKI_ACCESS_CODE=
MEDIAWIKI_SECRET_CODE=
ALLOWED_HOSTS=

#Exécuter les migrations
python manage.py migrate 

# Pour créer un administrateur
python manage.py createsuperuser 
```

## Utilisation
```
# Lancer le projet Django
python manage.py runserver 
```

Par défaut le serveur tourne sur le port 8000.


## Linter

Le linter ``Black`` est lancé à chaque PR et merge sur la branche `master`.

Pour pouvoir corriger les erreurs levées (CI/CD)

``` 
black .
```

Pour lancer l'analyseur manuellement
```sh
cd artwork_gallery_project 
black --check --verbose .
```

## Tests
```sh 
# Lancer les tests
python manage.py test

# Lancer les tests + la couverture de code
coverage run --source='.' manage.py test && coverage report
```

## Commandes personnalisées
- Supprimer les votes hebdomadaires
```sh
python manage.py delete_votes
```

- Mettre à jour les données
```sh
python manage.py fetch_missing_data
```
