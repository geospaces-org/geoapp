export PORT=7003

if [ $# -gt 0 ]; then
	export PORT=$1
fi

# uncomment the following to run in https mode
OPTS=' --cert /tmp/cert'

daphne -b 0.0.0.0 -p ${PORT}  geoapp.asgi:application 

