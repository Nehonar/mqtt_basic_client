# MQTT Basic client
Basic MQTT Client with Python and Handle various types of messages


## Starting broke HiveMQ
```bash
docker run --network=host --rm -p 8080:8080 -p 1883:1883 hivemq/hivemq4
```

## Run Dockerfile
```bash
docker build -t mqtt_client_app .
docker run --network=host mqtt_client_app
```

## Run node and gateway messages to test
```bash
python3 tests/nodo_test.py
```
```bash
python3 tests/gateway_test.py
```

### TODO:
- Unittest
- Improve error handling
- Security improvements (python-dotenv)
- Quality of service