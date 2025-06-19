docker build -t modbus-server .
docker run --name modbus_slave -p 5020:5020 modbus-server