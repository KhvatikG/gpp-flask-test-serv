FROM python:3.11 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /code

COPY --from=builder /root/.local /root/.local
COPY ./ .

EXPOSE 5000:5000

CMD ["python", "gpp-flask-test-server.py"]