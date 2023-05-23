#--------------------------------------------------------------------#
#
# Staff Directory Back-End
#
# This is where you will develop the back-end function for returning
# employee details that match the given first/last-name prefix. Given
# a character string you must return details of all employees whose
# first-name, last-name or both match the string.  You will need to
# confer with the front-end team to agree on the format in which the
# results are returned, but for each matching employee they must
# contain at least the (1) employee number, (2) first name, (3) last
# name and (4) date of birth.
#
# The employee data can be extracted from either the SQLite database
# or the CSV file provided.  Both contain the same employee data.
# Three solutions are possible:
#
# 1) Write a Python function which iterates over the lines of text
# in the CSV file to find matching employees using character string
# operations.  In this case recall that it's easy to iterate over
# each line in a text file using a "for" loop in Python.  Your
# solution will need to use the built-in file "open" function, the
# character string "split" method to extract the individual fields
# from each line (splitting the text on commas), and the string
# "startswith" predicate to determine if a first-name or last-name
# begins with the prefix entered by the user.
#
# 2) Write a Python function which uses the regular expression
# "findall" function to find and return all employee records with
# a first-name or last-name that begins with the prefix entered
# by the user.  In this case you will need the built-in "open" function
# and "read" method to get the contents of the CSV file as a single
# character string, and the "findall" method to find matching employee
# data.  You will find this quite easy if you use findall's MULTILINE
# option (as a third argument in the call) which allows you to
# use ^ and $ to match the beginning and end of each line of text
# in the string, respectively.
#
# 3) Write a Python function which accesses the SQLite database copy
# of the employee data.  In this case you will need to use the
# usual SQLite methods for opening and closing the database,
# executing a query on its contents, and fetching the result set.
# The query in this case can use the "C LIKE 'P%'" Boolean
# expression to match rows in which a text-valued column C begins
# with text pattern P.
#

# Import the findall function and the MULTILINE constant
# so that we can use ^ and $ in our regular expression to
# match the beginning and end of each line of text, if
# desired
from re import findall, MULTILINE, IGNORECASE

# Import the SQLite database functions
from sqlite3 import *
from os.path import exists

# Define your back-end function here
def search_by_loop(search):
    
    with open('employees.csv') as file:
        lines = file.readlines()

    lines.pop(0)

    results = []

    for line in lines:
        emp_no, birth_date, first_name, last_name, gender, hire_date = line.split(',')
        if first_name.lower().startswith(search.lower()) or last_name.lower().startswith(search.lower()):
            results.append((emp_no, first_name, last_name, birth_date))

    return results

def search_by_regex(search):

    with open('employees.csv') as file:
        content = file.read()

    regex = f"(.+\\b{search}.+)"

    content = findall(regex, content, IGNORECASE)

    return content

#Make a connection to the db
def search_by_db(search):
    db_name = "employees.db"
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute(f'SELECT ALL * FROM employees WHERE first_name LIKE "{search}%" or last_name LIKE "{search}%"')

    result = db.fetchall()

    db.close()
    connection.close()

    return result

def create_database():
    db_name = "employees.db"
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute("CREATE TABLE Ratings(RatingID INTEGER UNIQUE primary key AUTOINCREMENT, EmpId INTEGER, Rating INTEGER);")

    connection.commit()
    db.close()
    connection.close()

def add_employee_rating(emp_ID, rating):
    # if not exists(db_name):
    #     create_database(db_name)
    

    db_name = "employees.db"
    connection = connect(database=db_name)
    db = connection.cursor()

    db.execute(f'INSERT INTO Ratings (EmpId,Rating) VALUES ("{emp_ID}","{rating}");')

    connection.commit()
    db.close()
    connection.close()

if __name__ == "__main__":
    #test_list = search_by_loop("jon")
    # print(test_list)
    #search_by_regex("Jon")
    #create_database()
    #print(search_by_db("Parto"))
    add_employee_rating(900, 5)
