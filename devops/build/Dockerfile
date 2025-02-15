FROM ubuntu:24.04

RUN apt update
RUN apt install -y pip pipx
RUN PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install poetry==1.8.4
RUN poetry config virtualenvs.in-project true
RUN mkdir -p /oauth2-server/iam
COPY scripts/dev.sh /oauth2-server/dev.sh
RUN chmod +x /oauth2-server/dev.sh
RUN chown 1000:1000 -R /oauth2-server/
USER 1000
WORKDIR /oauth2-server