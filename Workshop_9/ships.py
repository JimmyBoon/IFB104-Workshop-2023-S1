
from sqlite3 import *

connection = connect('airline2.db')
db = connection.cursor()

# db.execute("DROP TABLE ships")
# connection.commit()

db.execute("CREATE TABLE ships (ShipId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, capacity INTEGER, age INTEGER)")
connection.commit()

db.close()
connection.close()
