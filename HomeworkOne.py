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

# Creates a table for sellers
create_sellers_table = """
CREATE TABLE IF NOT EXISTS sellers(
seller VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULl,
PRIMARY KEY (seller)
)"""
execute_query(conn, create_sellers_table)

# Now we insert James, John, Jack as new entries in the sellers table
query = "INSERT INTO sellers (seller, last_name) VALUES ('James','Deer'),('John','Doe'), ('Jack','Reaper')"
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

# Show user list of all available sellers
select_seller_data = "SELECT seller FROM sellers"
select_sellers = execute_read_query(conn, select_seller_data)
print(f"Available Sellers:")
for x in select_sellers:
    print(x)

userInput = input("Enter the seller's name: ")
print("Sales Report for " + userInput + ":")

# Select/fetch all data in the sales table where the seller is equal to the user's input
select_sales_data = "SELECT * FROM sales WHERE seller = '%s'" % userInput
sales_data = execute_read_query(conn, select_sales_data)
for x in sales_data:
    print(x)


