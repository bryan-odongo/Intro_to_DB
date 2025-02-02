import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your MySQL host
            user='root',               # Replace with your MySQL username
            password='your_password'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Explicitly handle mysql.connector.Error
        # Handle errors when connecting to the database
        print(f"Error: {e}")

    finally:
        # Ensure the connection is closed properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
