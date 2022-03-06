from tkinter import *
import pyodbc 
import pandas

# Refer to GetStarted.txt if needed

def sql(query):
    """ Connects to the local running database and runs the query passed in as a parameter. Returns the results as an array. """
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\SQLEXPRESS;'
                      'Database=NymptonFoodHub;'
                      'Trusted_Connection=yes;')
    cursor = connection.cursor()
    results = cursor.execute(query).fetchall()
    # dataFrame = pandas.read_sql_query(query, connection) # Used to create a pandas dataframe from the data (unknown if needed)
    connection.close()
    return results

def sqlStoredProcedure(storedProcedure, parameters):
    """ Connects to the local running database and runs the stored procedure passed in, uses the parameters given ( use () if no parameters needed ). Returns the results as an array. """
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\SQLEXPRESS;'
                      'Database=NymptonFoodHub;'
                      'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute( storedProcedure, parameters )
    results = cursor.fetchall()
    connection.close()
    return results

def sqlLogin(username, password):
    """ Receives a username and password then tries to login to SQL Server via SQL Server authentication. """
    try:
        connection = pyodbc.connect('Driver={SQL Server};'
                        'Server=.\SQLEXPRESS;'
                        'Database=NymptonFoodHub;'
                        'UID='+username+';'
                        'PWD='+password+';'
                        'Trusted_Connection=no;')
        connection.close()
        return True
    except:
        return False