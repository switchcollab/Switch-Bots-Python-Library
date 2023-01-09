FROM python:alpine
ARG WORKDIR=/workspace

WORKDIR $WORKDIR


COPY .  $WORKDIR


ENV VIRTUAL_ENV=$WORKDIR/src/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    && apk add --no-cache \
    bash \
    git \
    openssh \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --upgrade wheel \
    && pip install --upgrade twine \
    && apk del .build-deps

RUN pip install -r $WORKDIR/src/requirements.txt

CMD [ "/bin/sh", "-c", "while sleep 1000; do :; done"]