web: python artwork_gallery/manage.py runserver 0.0.0.0:$PORT
release: python artwork_gallery/manage.py migrate &&  python artwork_gallery manage.py createsuperuser2 --no-input --username $ADMIN_USERNAME --password $ADMIN_PASSWORD

