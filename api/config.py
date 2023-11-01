import os
import mysql.connector
from mysql.connector import Error

# Each Flask web application contains a secret key which used to sign session
# cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = os.getenv('DEBUG', "True")

# Connect to the MYSQL database
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PASS = os.getenv('MYSQL_ROOT_PASSWORD', '')
MYSQL_NAME = os.getenv('MYSQL_DATABASE', 'bookings')
def get_db():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            database=MYSQL_NAME,
            user='root',
            password=MYSQL_PASS
        )

        return connection
    except Error as e:
        print(f"ERROR: Database connection failed: {e}")
        return None
  