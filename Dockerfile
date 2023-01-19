FROM python:alpine
ARG WORKDIR=/workspace

WORKDIR $WORKDIR


COPY .  $WORKDIR


RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    && apk add --no-cache \
    bash \
    git \
    openssh  \
    && apk del .build-deps


ENV VIRTUAL_ENV=$WORKDIR/src/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install wheel && \
    pip install setuptools && \
    pip install twine

RUN pip install -Ur $WORKDIR/src/requirements-dev.txt

CMD [ "/bin/sh", "-c", "while sleep 1000; do :; done"]