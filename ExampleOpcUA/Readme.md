docker build -t opcua-server-image .
docker run --name opcua_server -p 4840:4840 opcua-server-image