FROM python:alpine
ARG WORKDIR=/workspace

WORKDIR $WORKDIR


COPY .  $WORKDIR


ENV VIRTUAL_ENV=$WORKDIR/src/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install wheel && \
    pip install setuptools && \
    pip install twine

RUN pip install -r $WORKDIR/src/requirements.txt

CMD [ "/bin/sh", "-c", "while sleep 1000; do :; done"]