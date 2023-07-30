FROM python

COPY . .

WORKDIR /backend

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
