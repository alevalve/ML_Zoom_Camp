FROM python:3.10

ENV PYTHONUNBUFFERED=TRUE

RUN pip install pipenv

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy 

COPY [ "prediction.py", "lar.bin", "./" ]

EXPOSE 8080

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8080", "prediction:app"]