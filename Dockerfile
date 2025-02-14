FROM postgres:latest
LABEL authors="Liexa"

ENV POSTGRES_PASSWORD=root
ENV POSTGRES_USER=root
ENV POSTGRES_DB=bonappdb
COPY init.sql /docker-entrypoint-initdb.d/