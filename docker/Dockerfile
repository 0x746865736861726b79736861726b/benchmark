FROM python:3.14.0rc1-alpine3.22

WORKDIR /app

COPY ./database/test_database.json /app/test_database.json

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
