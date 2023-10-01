FROM python:3.10

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt


# Запускаем бота
CMD ["python", "main.py"]