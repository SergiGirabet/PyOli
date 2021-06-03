release: bash -c "echo $DATABASE_URL && python3 manage.py migrate"
web: gunicorn pyoli.wsgi