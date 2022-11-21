FROM python:3-alpine

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]