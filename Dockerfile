FROM sada001/myrepos:sada-centdjango

RUN mkdir /service
WORKDIR /service
COPY  . /service/
EXPOSE 8003
RUN chmod -R 777 /service
#ENTRYPOINT  ["python", "run.py"]
#ENTRYPOINT  ["gunicorn", "-c", "gunicorn.py", "aiservices.wsgi"]
CMD [ "/bin/bash" ]

