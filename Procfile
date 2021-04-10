release: bash -c "python3 manage.py collectstatic -y && python3 manage.py migrate"
gunicorn pyoli.wsgi --log-file -