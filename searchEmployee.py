# Terminal

# CREATE DATABASE beadb;
# \c beadb

# CREATE TABLE employees (
#     oa_id VARCHAR(4) PRIMARY KEY,
#     name TEXT NOT NULL,
#     phone VARCHAR(15),
#     department TEXT,
#     supervisor_oa_id VARCHAR(4) REFERENCES employees(oa_id)
# );

# INSERT INTO employees VALUES ('LEAE001', 'John Doe', '130xxx09999', 'LOD', NULL);
# INSERT INTO employees VALUES ('LEAE002', 'Jane Smith', '130xxx09919', 'CLS', 'LEAE001');
# INSERT INTO employees VALUES ('LEAE003', 'Alice Johnson', '130xxx09860', 'HR', 'LEAE001');

import psycopg2

def connect():
    return psycopg2.connect(
        dbname="beadb",
        user="postgres",    
        password="password", # replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )

def search_employee():
    search_field = input("Enter search field (department, name, phone, oa_id): ")
    search_value = input(f"Enter value for {search_field}: ")

    conn = connect()
    cursor = conn.cursor()

    query = f"SELECT * FROM employees WHERE {search_field} = %s"
    cursor.execute(query, (search_value,))
    employees = cursor.fetchall()

    for employee in employees:
        oa_id, name, phone, department, supervisor_oa_id = employee

        # Get supervisor info
        cursor.execute("SELECT name, phone FROM employees WHERE oa_id = %s", (supervisor_oa_id,))
        supervisor_info = cursor.fetchone()

        # Get subordinates info
        cursor.execute("SELECT name, phone FROM employees WHERE supervisor_oa_id = %s", (oa_id,))
        subordinates_info = cursor.fetchall()

        print("\nEmployee Info:")
        print(f"OA ID: {oa_id}, Name: {name}, Phone: {phone}, Department: {department}")
        if supervisor_info:
            print(f"Supervisor: {supervisor_info[0]}, Phone: {supervisor_info[1]}")
        if subordinates_info:
            print("Subordinates:")
            for s in subordinates_info:
                print(f"Name: {s[0]}, Phone: {s[1]}")

    cursor.close()
    conn.close()

search_employee()


# Output

# Enter search field (department, name, phone, oa_id): department
# Enter value for department: LOD

# Employee Info:
# OA ID: LEAE001, Name: John Doe, Phone: 1234, Department: LOD
# Subordinates:
# Name: Jane Smith, Phone: 4365
# Name: Alice Johnson, Phone: 7892

