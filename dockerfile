FROM python:3.11-slim as base

ENV PTHONNUNBUFFERED 1

WORKDIR /project

COPY src ./

RUN pip install pdm

ENV PYTHONPATH=/project/__pypackages__/3.11/lib:/project/__pypackages__/3.11/bin