from sqlite3 import *
import os

db_name = "airline2.db"

def create_database():
    global db_name

    if not os.path.exists(db_name):
        print(f"Database {db_name} does not exist, creating database")

        connection = connect(database=db_name)
        db = connection.cursor()

        with open("airline.sql", "r") as sqlfile:
            sql_script = sqlfile.read()
            db.executescript(sql_script)
        
        db.close()
        connection.close()
        return
    else:
        print(f"Database {db_name} already exists")
        return

def insert_aircraft(aircraft_type, aircraft_desc, seating_cap):
    global db_name

    create_database()


    connection = connect(database=db_name)
    airline_db = connection.cursor()

    airline_db.execute(f'INSERT INTO aircraft (AircraftType, AircraftDescription, SeatingCapacity) VALUES ("{aircraft_type}", "{aircraft_desc}", "{seating_cap}")')
    connection.commit()


    airline_db.execute("SELECT * FROM aircraft")

    rows = airline_db.fetchall()

    for row in rows:
        print(row)

    airline_db.close()
    connection.close()

def delete_aircraft(aircraft_type):
    global db_name

    connection = connect(database=db_name)
    airline_db = connection.cursor()

    airline_db.execute(f'DELETE FROM aircraft WHERE AircraftType = "{aircraft_type}"')
    connection.commit()


    airline_db.execute("SELECT * FROM aircraft")

    rows = airline_db.fetchall()

    for row in rows:
        print(row)

    airline_db.close()
    connection.close()

def display_flight_info(flight_num):
    global db_name

    connection = connect(database=db_name)
    airline_db = connection.cursor()

    airline_db.execute(f'SELECT * FROM flights WHERE FlightNum = "{flight_num}"')
    rows = airline_db.fetchall()

    for row in rows:
        print(row)
    
    airline_db.close()
    connection.close()

def sell_seats_flight(flight_num, seats_to_sell):
    global db_name

    connection = connect(database=db_name)
    airline_db = connection.cursor()

    airline_db.execute(f'SELECT * FROM flights WHERE FlightNum = "{flight_num}"')
    rows = airline_db.fetchall()

    for row in rows:
        print(row)
    
    if len(rows) == 0:
        print("Flight does not exist")
        airline_db.close()
        connection.close()
        return
    
    seats_remaining = rows[0][3]

    if seats_remaining < seats_to_sell:
        print(f"Flight {flight_num} does not have enough seats")
        airline_db.close()
        connection.close()
        return
    
    seats_remaining -= seats_to_sell

    airline_db.execute(f'UPDATE flights SET SeatsRemaining = "{seats_remaining}" WHERE FlightNum = "{flight_num}"')
    connection.commit()

    display_flight_info(flight_num)
    
    airline_db.close()
    connection.close()

if __name__ == "__main__":
    #insert_aircraft("DC3","Old Plane", "33")
    #delete_aircraft("B717")
    sell_seats_flight(2,3)