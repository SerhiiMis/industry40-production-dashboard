import psycopg2
from datetime import datetime
import random

conn = psycopg2.connect(
    host="localhost",
    database="i40_monitoring",
    user="postgres",
    password="postgres" 
)

cur = conn.cursor()

# Insert production line
cur.execute("""
    INSERT INTO production_line (name, location)
    VALUES (%s, %s) RETURNING id
""", ("Line 1", "Factory A"))

line_id = cur.fetchone()[0]

# Insert machines
machines = [
    ("Machine A", "Processing", 5),
    ("Machine B", "Assembly", 7),
    ("Machine C", "Quality", 3)
]

machine_ids = []

for name, mtype, cycle in machines:
    cur.execute("""
        INSERT INTO machine (line_id, name, machine_type, ideal_cycle_time_sec)
        VALUES (%s, %s, %s, %s) RETURNING id
    """, (line_id, name, mtype, cycle))
    machine_ids.append(cur.fetchone()[0])


# Insert production events
for machine_id in machine_ids:
    for _ in range(20):
        cur.execute("""
            INSERT INTO production_event
            (machine_id, timestamp, produced_units, scrap_units, cycle_time_sec)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            machine_id,
            datetime.now(),
            random.randint(1, 5),
            random.randint(0, 1),
            random.randint(3, 8)
        ))

conn.commit()
cur.close()
conn.close()

print("Data generated successfully.")

