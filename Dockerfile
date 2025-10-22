FROM python:3.12-alpine
COPY . /my-app
WORKDIR /my-app
RUN apk add --no-cache gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && apk del gcc python3-dev musl-dev
CMD python app.py