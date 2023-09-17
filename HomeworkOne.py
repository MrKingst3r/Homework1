import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# Creating a connection to the MYSQL Database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

# Creates a table for sales
create_sales_table = """
CREATE TABLE IF NOT EXISTS sales(
sale_id INT AUTO_INCREMENT,
seller VARCHAR(255) NOT NULL,
product VARCHAR(255) NOT NULL,
quantity INT,
price FLOAT,
PRIMARY KEY (sale_id)
)"""
execute_query(conn, create_sales_table)

# Creates a table for Clients
create_clients_table = """
CREATE TABLE IF NOT EXISTS clients(
client_id INT AUTO_INCREMENT,
first_name VARCHAR(255) NOT NULL,
PRIMARY KEY (client_id)
)"""
execute_query(conn, create_clients_table)

# Now we insert James, John, Jack as new entries in the Clients table
query = "INSERT INTO clients (first_name) VALUES ('James'),('John'), ('Jack')"
execute_query(conn, query)

# Inserting rows into the sales table
query2 = """
INSERT INTO sales(sale_id,seller,product,quantity,price) VALUES
(1, "James", "Pen", 40, 1.99),
(2, "James", "Notebook", 23, 2.98),
(3, "Jack", "Pencil", 31, 0.79),
(4, "John", "Compass", 2, 5.99),
(5, "John", "Monitor", 1, 100.98),
(6, "Jack", "Sharpie", 5, 2.79),
(7, "James", "Brush", 3, 3.99),
(8, "John", "Ruler", 1, 1.98),
(9, "Jack", "Paper", 100, 5.79)
"""
execute_query(conn, query2)


