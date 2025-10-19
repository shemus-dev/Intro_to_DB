
import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # change this to your MySQL username (e.g., 'shem' or 'navin')
            password="1234"       # change this to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection properly
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        except:
            pass

# Run the function
if __name__ == "__main__":
    create_database()
