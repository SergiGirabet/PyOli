release: bash -c "python3 manage.py collectstatic && cat <(echo "yes") - && python3 manage.py migrate"
gunicorn pyoli.wsgi --log-file -