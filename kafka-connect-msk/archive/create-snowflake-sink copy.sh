#!/bin/sh

cd / .
echo "===> Installing connector plugins"
confluent-hub install --no-prompt snowflakeinc/snowflake-kafka-connector:${KAFKA_SNOWFLAKE_CONNECT_VERSION}

echo "===> Launching Kafka Connect worker"
/etc/confluent/docker/run & 
echo "===> Waiting for Kafka Connect to start listening on kafka-connect ⏳"
while [ $$(curl -s -o /dev/null -w %{http_code} http://kafka-connect:8083/connectors) -eq 000 ] ; do
echo -e $$(date) " Kafka Connect listener HTTP state: " $$(curl -s -o /dev/null -w %{http_code} http://kafka-connect:8083/connectors) " (waiting for 200)"
sleep 5
done
nc -vz kafka-connect 8083
sleep 5
echo -e "\n ===> Creating Kafka Connector To Sink Data from Kafka to Snowflake"






curl -i -X PUT -H  "Content-Type:application/json" \
    http://kafka-connect:8083/connectors/ryan_chynoweth_kafka_test/config \
    -d '{
        "connector.class":"com.snowflake.kafka.connector.SnowflakeSinkConnector",
        "tasks.max":1,
        "topics":"ryan_chynoweth_kafka_test",
        "snowflake.url.name":"<SNOWFLAKE URL>",
        "snowflake.user.name":"<USER NAME>",
        "snowflake.user.role":"ACCOUNTADMIN",
        "snowflake.private.key":"<YOUR PRIVATE KEY>",
        "snowflake.private.key.passcode":"<PRIVATE KEY PASSCODE>",
        "snowflake.database.name":"DEMO",
        "snowflake.schema.name":"RAC_SCHEMA",
        "key.converter":"org.apache.kafka.connect.storage.StringConverter",
        "value.converter.schemas.enable": "false",
        "value.converter":"org.apache.kafka.connect.json.JsonConverter"
    }'


sleep infinity
