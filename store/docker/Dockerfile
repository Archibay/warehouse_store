FROM python:3.10

COPY ./store/requirements.txt /

RUN pip install -r requirements.txt

COPY ./store/docker/docker-entrypoint.sh ./store/docker/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY ./store/ /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
