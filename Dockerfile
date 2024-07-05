FROM python:3.10-slim

WORKDIR /usr/app

COPY requirments.txt ./
COPY ./src ./src

RUN pip install -r requirments.txt

VOLUME /usr/app/config

EXPOSE 8000

ENV EMAIL_HOST=""
ENV EMAIL_SMTP_PORT="465"
ENV EMAIL_IMAP_PORT="993"
ENV EMAIL_USERNAME=""
ENV EMAIL_PASSWORD=""
ENV CORS=""

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

