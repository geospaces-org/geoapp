export PORT=7005

if [ $# -gt 0 ]; then
	export PORT=$1
fi

if [ $# -lt 2 ]
then
    echo "RUNNING LOCAL server at ${PORT}"
    python manage.py runserver 0:${PORT}
else
    echo "RUNNING GUNICORN server at ${PORT}"
    gunicorn -c gunicorn.config.py mainapp.wsgi
fi
