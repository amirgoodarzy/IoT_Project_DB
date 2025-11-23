from neo4j import GraphDatabase

# Connection details
uri = "bolt://localhost:7687"
user = "neo4j"
password = "amir1384"

# Initialize the driver
driver = GraphDatabase.driver(uri, auth=(user, password))

def save_to_neo4j(payload):
    try:
        with driver.session() as session:
            # FIX 1: Changed 'write_transaction' to 'execute_write' for newer Neo4j drivers
            session.execute_write(_create_sensor_and_reading, payload)
        print("Data saved successfully to Neo4j")
    except Exception as e:
        print(f"Error saving to Neo4j: {e}")

def _create_sensor_and_reading(tx, payload):
    # Ensure sensor_id is an integer
    sensor_id = int(payload.get("sensor_id"))
    sensor_type = payload["type"]
    value = payload["value"]
    unit = payload["unit"]
    timestamp = payload["timestamp"]
    
    sensor_name = f"Sensor {sensor_id}"

    # FIX 2: Added the actual tx.run() command to execute the Cypher query
    tx.run("""
        MERGE (s:Sensor {id: $sensor_id})
        ON CREATE SET 
            s.name = $sensor_name,
            s.type = $sensor_type
        ON MATCH SET 
            s.last_value = $value,
            s.last_unit = $unit,
            s.last_timestamp = $timestamp

        CREATE (r:Reading {
            name: toString($value) + " " + $unit,
            value: $value,
            unit: $unit,
            timestamp: $timestamp,
            type: $sensor_type
        })

        MERGE (s)-[:REPORTED]->(r)
    """, 
    sensor_id=sensor_id,
    sensor_name=sensor_name,
    sensor_type=sensor_type,
    value=value,
    unit=unit,
    timestamp=timestamp
    )

def reset_neo4j():
    """Helper to wipe the database clean."""
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("Neo4j reset complete.")

def test_db():
    """Helper to check connection."""
    try:
        with driver.session() as session:
            result = session.run("RETURN 1 AS test")
            for record in result:
                print("Neo4j Connection Check: OK", record["test"])
    except Exception as e:
        print("Neo4j Connection Error:", e)

def test_insert_data():
    """Helper to test inserting dummy data."""
    test_payload = {
        "sensor_id": 1,         # Passed as integer
        "value": 420,
        "unit": "ppm",
        "timestamp": "2023-11-15T12:00:00",
        "type": "CO2"
    }
    save_to_neo4j(test_payload)
    print("Test data function finished.")

# --- EXECUTION AREA ---
# You can uncomment these lines to test this file directly.
# When running via publisher.py, keep them commented out.

# test_db()
test_insert_data()
# reset_neo4j()