# Kafka Connect and Snowflake 

This repository is forked from: https://github.com/entechlog/kafka-examples. There is also a [blog](https://www.entechlog.com/blog/kafka/integrating-kafka-connect-with-msk/) related to the code. 


This repository is the source code related to a [blog]() that I wrote on how to create a streaming solution with Kafka (AWS MSK) and Snowflake. In this solution I deploy a provisioned MSK cluster and an EC2 instance that share a VPC and Security group. On the EC2 machine there is a process I outline in the blog that shows how to deploy the Kafka Connector for Snowflake as a docker container. 

The solution architecture looks like the following: 
![](./img)


For instructions on how to run the repository please reference the blog linked above. 









# MISC Notes: 

curl http://localhost:8083/connectors/ryan_chynoweth_kafka_test/status | jq



./bin/kafka-topics.sh --bootstrap-server $BS --create --topic ryan_chynoweth_kafka_test --partitions 2

--command-config client.properties



export BS=b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092


./bin/kafka-topics.sh --create --bootstrap-server b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092 --replication-factor 3 --partitions 1 --topic ryan_chynoweth_kafka_test

./bin/kafka-topics.sh --delete --bootstrap-server b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092 --topic ryan_chynoweth_kafka_test


./bin/kafka-topics.sh --list --bootstrap-server b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092



ssh to ec2 machine:
```
ssh -i "rac_ec2_pair.cer" ec2-user@54.161.101.147
```




./bin/kafka-topics.sh --create --bootstrap-server <BOOTSTRAP SERVER> --replication-factor 3 --partitions 1 --topic <TOPIC NAME>


./bin/kafka-console-producer.sh --broker-list b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092 --topic ryan_chynoweth_kafka_test


{"eventId": "21312-213213-213213-2333", "action": "Open", "time": 123444023}


python3 publish_data.py "ryan_chynoweth_kafka_test" "b-2.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-1.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092,b-3.racmskcluster.s8a80k.c25.kafka.us-east-1.amazonaws.com:9092"






===> Listing Directory
/home/appuser