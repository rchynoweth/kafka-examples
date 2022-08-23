#!/bin/sh

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
