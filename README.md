# La Galerie du Numerique

URL : https://galerie-numerique.herokuapp.com/
Admin : https://galerie-numerique.herokuapp.com/admin
Login : https://galerie-numerique.herokuapp.com/login




Créer l'environnement virtuel
```python
python -m venv env
```

Rentrer dans l'environnement virtuel
- Linux/MacOS
```python
source env/bin/activate
```

- Windows
```python
env/Scripts/Activate.ps1
```

Installer les dépendances
```python
 pip install -r requirements.txt
```

Se déplacer dans le dossier du projet
```python
 cd artwork_gallery
```

Initialiser la base de données
```python
python manage.py migrate 
```

Lancer le projet Django
```python
python manage.py runserver 
```

Pour créer un administrateur
```python
python manage.py createsuperuser 
```
