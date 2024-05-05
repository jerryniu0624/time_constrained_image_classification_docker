# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY ./app /app
COPY ./app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8008
CMD [ "/app/dist/main"]
# COPY . .
