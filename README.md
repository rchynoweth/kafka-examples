# Kafka Connect and Snowflake 

This repository is forked from: https://github.com/entechlog/kafka-examples. There is also a [blog](https://www.entechlog.com/blog/kafka/integrating-kafka-connect-with-msk/) related to the code. 


This repository is the source code related to a [blog]() that I wrote on how to create a streaming solution with Kafka (AWS MSK) and Snowflake. In this solution I deploy a provisioned MSK cluster and an EC2 instance that share a VPC and Security group. On the EC2 machine there is a process I outline in the blog that shows how to deploy the Kafka Connector for Snowflake as a docker container. 

The solution architecture looks like the following: 
![](./img)


For instructions on how to run the repository please reference the blog linked above. 


