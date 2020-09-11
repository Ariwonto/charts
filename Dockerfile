FROM  python:3.7
LABEL buildapp="docker build --network=host -t aw/pepetrueno:latest . "
LABEL pushapp="docker push aw/pepetrueno:latest . "
LABEL executeapp="docker run -itd -p 8000:8000 aw/pepetrueno:latest "

ARG GITHUB_SHA
ARG GITHUB_REF
ENV SHA=$GITHUB_SHA
ENV REF=$GITHUB_REF
# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# # uWSGI will listen on this port
# EXPOSE 8000

RUN pip install --upgrade pip && pip install --no-cache-dir virtualenv && virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
ADD . /app
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt && \
    /env/bin/python /app/manage.py makemigrations && /env/bin/python /app/manage.py migrate \
    && /env/bin/python /app/manage.py collectstatic --noinput



WORKDIR /app

# # Change to a non-root user
# USER ${APP_USER}:${APP_USER}

# Uncomment after creating your docker-entrypoint.sh
# ENTRYPOINT ["/app/docker-entrypoint.sh"]


CMD gunicorn -b :8000 graficos.wsgi