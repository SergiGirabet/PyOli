release: bash -c "python3 manage.py collectstatic\n yes\n && python3 manage.py migrate"
gunicorn pyoli.wsgi --log-file -