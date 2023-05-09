from sqlite3 import *
from os.path import exists

db_name = "demo_db.db"

def create_database(db_name):
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute("CREATE TABLE Users(UserId INTEGER UNIQUE primary key AUTOINCREMENT, UserName TEXT UNIQUE, UserPassword TEXT(200), Name TEXT, UserAddress TEXT);")

    connection.commit()
    db.close()
    connection.close()

def add_user_to_db(db_name, user_name, password, name, address):

    if not exists(db_name):
        create_database(db_name)

    try:    
        connection = connect(database=db_name)
        db = connection.cursor()
        db.execute(f"INSERT INTO Users(UserName, UserPassword, name, UserAddress) VALUES ('{user_name}', '{password}', '{name}', '{address}') ")
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        db.close()
        connection.close()

def get_user_from_db(db_name, user_name):

    try:    
        connection = connect(database=db_name)
        db = connection.cursor()
        db.execute(f"SELECT * FROM Users WHERE UserName = '{user_name}' ")
        result = db.fetchall()
        print(result[0])

        connection.commit()


    except Exception as e:
        print(e)
    finally:
        db.close()
        connection.close()



#add_user_to_db(db_name, "james@test.com", "password", "james", "123 house street")
get_user_from_db(db_name,"james@test.com")


    

