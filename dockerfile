FROM python:3.11

WORKDIR /app

ENV BOT_TOKEN="5863465594:AAHmlSGqtQBrKE6kCd9a5k5ghfkeCuDLmyI"
ENV OPENAI_TOKEN="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"


ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "bot.py"]