import sqlite3

conn = sqlite3.connect('customer.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE CUSTOMER
         (CustomerID   REAL PRIMARY KEY NOT NULL,
         CompanyISIN   REAL NOT NULL,
         Holding       REAL NOT NULL);''')
print("Table created successfully")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (100, 1, 20000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (200, 2, 20000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (300, 3, 10000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (400, 4, 5000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (500, 1, 12000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (600, 2, 12000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (700, 2, 12000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (800, 8, 12000.00 )")

conn.execute("INSERT INTO CUSTOMER (CustomerID,CompanyISIN,Holding) \
      VALUES (900, 10, 12000.00 )")

conn.commit()

print ("Records created successfully")

conn.close()
