#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /codigo

# COPY ./codigo/requirements requirements

WORKDIR /codigo

RUN pip install --upgrade pip

RUN pip install -r /codigo/requirements

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000", "--reload"]
