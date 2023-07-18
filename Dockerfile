
ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-slim as base

RUN --mount=type=cache,target=/root/.cache/pip,mode=775 pip3 install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip,mode=775\
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip3 install -r requirements.txt


FROM base as final
RUN --mount=type=cache,target=/root/.cache/pip,mode=775 \
    pip3 install gunicorn

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/opt/appuser" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

USER appuser
WORKDIR /opt/appuser/src

COPY --chown=appuser:users . .

EXPOSE 5000

CMD gunicorn app:app --bind=0.0.0.0:5000
