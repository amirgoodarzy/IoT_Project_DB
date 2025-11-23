# IoT_Project_DB 
#Project: Environmental Monitoring

This project uses MQTT to monitor environmental sensors. MQTT is a lightweight messaging protocol for publishing and subscribing messages in IoT applications and real-time data exchange.

Project Overview

My goal with this project is to demonstrate how you can retrieve data from environmental sensors and publish them or subscribe in order to receive the sensor information, whether it is a temperature, air, or CO2 sensor.

Main Features

It connects to an MQTT broker in order to exchange information.

Publishes messages with the information of the sensors.

Subscribes to the MQTT server and actively listens for messages.

Different data are saved into different databases using SQLite3, PyMongo, and Neo4j based on their sensor types.

After some information is inserted into the databases, the data could be viewed on the according platform; for instance, Neo4j data can be viewed on Neo4j Desktop.

Libraries Used

Paho-mqtt: Used in order to connect to the MQTT server.

sqlite3: Used for the SQL database and its queries.

pymongo: Used to connect and maintain the information related to air sensors.

neo4j: GraphDatabase is imported from the neo4j library in order to connect to the database and execute Neo4j queries.

Prerequisites

MQTT Broker:
For local development, the Mosquitto broker is recommended.

Download: https://mosquitto.org/download/

Python 3+:
Make sure you have Python 3+ installed on your device.

Python Libraries:
Install the required libraries using pip:

pip install paho-mqtt pymongo neo4j


Project Files

Subscriber (subscriber.py):
Open a new terminal window and run the subscriber. It will start listening for messages:

python subscriber.py


Publisher (publisher.py):
Open a second, separate terminal window and run the publisher to start sending data:

python publisher.py


mongodb.py:
This file saves the information related to air sensors to the MongoDB database via the function save_to_mongodb() imported to subscriber.py.

sqlidb.py:
This file saves the information related to temperature sensors to the SQL database via the function save_to_sqlite() imported to subscriber.py.

neo4jdb.py:
This file saves the information related to CO2 sensors to the Neo4j database using the function save_to_neo4j() imported to subscriber.py.


How to Run the Application

Run the subscriber file so it starts listening for information.

Then you can run the publisher.py to actually publish sensors data.

In each database file (sqlidb.py, mongodb.py, neo4jdb.py), there is a function commented out for printing out the results saved in them. In order to see the results directly in the terminal, you would have to remove the commenting code and run the file.
