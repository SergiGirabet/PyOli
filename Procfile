release: bash -c "python3 manage.py flush --no-input && python3 manage.py collectstatic && python3 manage.py migrate"
gunicorn pyoli.wsgi --log-file -