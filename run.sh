export PORT=7003

if [ $# -eq 0 ]
then
    echo "RUNNING LOCAL server at ${PORT}"
    python manage.py runserver 0:${PORT}
else
    echo "RUNNING GUNICORN server at ${PORT}"
    gunicorn -c gunicorn.config.py mainapp.wsgi
fi
