FROM python:3.10-slim

RUN pip install pymodbus

WORKDIR /app
COPY servidor_modbus.py .

CMD ["python", "slave_modbus.py"]