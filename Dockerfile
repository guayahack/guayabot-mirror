FROM python:3.10.3

WORKDIR /app

COPY Pipfile* ./
RUN pip install pipenv && pipenv sync

COPY . .

CMD ["pipenv", "run", "python", "main.py"]  