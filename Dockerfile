FROM python:3.9.1

WORKDIR /app
COPY . .

COPY .env.example .env
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
