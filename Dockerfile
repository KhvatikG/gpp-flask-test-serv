FROM python:3.11 AS builder
COPY https://raw.githubusercontent.com/KhvatikG/gpp-flask-test-serv/main/requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /code

COPY --from=builder /root/.local /root/.local
COPY https://raw.githubusercontent.com/KhvatikG/gpp-flask-test-serv/main/gpp-flask-test-server.py .

EXPOSE 5000:5000

CMD ["python", "gpp-flask-test-server.py"]
