import mysql.connector

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'rakhi@123'
DB_NAME = 'smart_city'


def get_db_connection():
    """Connect directly to the smart_city database (used by app routes)."""
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


def init_db():
    """
    Automatically creates the database, tables, and sample data if they
    don't already exist. Safe to run every time the app starts.
    """
    # Step 1: connect to MySQL server WITHOUT selecting a database yet,
    # because the database might not exist yet.
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()

    # Step 2: create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    # Step 3: create tables if they don't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INT AUTO_INCREMENT PRIMARY KEY,
            problem_type VARCHAR(100),
            location VARCHAR(100),
            severity VARCHAR(30),
            description TEXT,
            status VARCHAR(30),
            detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            problem_type VARCHAR(100),
            location VARCHAR(100),
            probability FLOAT,
            prediction_time DATETIME,
            recommendation TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citizen_reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            location VARCHAR(100),
            problem_type VARCHAR(100),
            priority VARCHAR(30),
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Step 4: insert sample data ONLY if the problems table is empty
    cursor.execute("SELECT COUNT(*) FROM problems")
    row_count = cursor.fetchone()[0]

    if row_count == 0:
        cursor.execute("""
            INSERT INTO problems (problem_type, location, severity, description, status)
            VALUES
            ('Traffic Congestion', 'Hanamkonda', 'High', 'Heavy traffic detected', 'Active'),
            ('Air Pollution', 'Warangal', 'Critical', 'Air quality above safe threshold', 'Active'),
            ('Waste Overflow', 'Kazipet', 'Medium', 'Waste level is high', 'Pending')
        """)
        print("Sample data inserted into 'problems' table.")
    else:
        print(f"'problems' table already has {row_count} row(s) — skipping sample data insert.")

    connection.commit()
    cursor.close()
    connection.close()
    print("Database setup complete.")
