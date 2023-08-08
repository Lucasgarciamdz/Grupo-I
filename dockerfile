FROM python:3.11.4-alpine

WORKDIR /backend

COPY backend/ .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


CMD ["python", "app.py"]
