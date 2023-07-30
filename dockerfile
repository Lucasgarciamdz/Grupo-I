FROM python:3.11.4-alpine

COPY . .

WORKDIR /backend

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
