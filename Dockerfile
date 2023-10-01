FROM python:3.8

WORKDIR /b1_words

COPY req.txt .

RUN pip install -r req.txt


COPY . .
RUN groupadd app    # Создание группы
RUN useradd -m -g app app -p PASSWORD   # Добавляем пользователя с паролем Password
RUN usermod -aG app app # Добавляем в группу

# Создание переменных
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

WORKDIR $APP_HOME



COPY . $APP_HOME



RUN chown -R app:app $APP_HOME
USER app
# Запускаем бота

CMD ["python", "main.py"]
