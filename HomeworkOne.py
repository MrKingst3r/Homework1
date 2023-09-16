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
