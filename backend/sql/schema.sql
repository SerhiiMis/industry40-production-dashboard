CREATE TABLE production_line (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE machine (
    id SERIAL PRIMARY KEY,
    line_id INT REFERENCES production_line(id),
    name VARCHAR(100) NOT NULL,
    machine_type VARCHAR(50),
    ideal_cycle_time_sec INT
);

CREATE TABLE machine_status (
    id SERIAL PRIMARY KEY,
    machine_id INT REFERENCES machine(id),
    timestamp TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE production_event (
    id SERIAL PRIMARY KEY,
    machine_id INT REFERENCES machine(id),
    timestamp TIMESTAMP NOT NULL,
    produced_units INT,
    scrap_units INT,
    cycle_time_sec INT
);
