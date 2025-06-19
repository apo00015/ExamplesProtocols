FROM python:3.10-slim

RUN pip install opcua

WORKDIR /app
COPY server_opc.py .

CMD ["python", "server_opc.py"]