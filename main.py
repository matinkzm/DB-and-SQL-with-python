import pandas as pd
import csv
import sqlite3
import mysql.connector
    
    
# uncomment each task to see the output
    
# first connect to the database and make a cursor 
connection = sqlite3.connect("FinalDB")
cursor = connection.cursor()

# read csv data files and make a local database
df = pd.read_csv("ChicagoCensusData.csv")
df.to_sql("CENSUS_DATA", connection, if_exists='replace', index=False, method="multi")

df = pd.read_csv("ChicagoCrimeData.csv")
df.to_sql("CHICAGO_CRIME_DATA", connection, if_exists='replace', index=False, method="multi")

df = pd.read_csv("ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", connection, if_exists='replace', index=False, method="multi")

# some sql queries
'''
cursor.execute("SELECT COUNT(*) FROM CHICAGO_CRIME_DATA")           # problem 1
result1 = cursor.fetchall()
print("total number of crimes = " + str(result1))'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME < 11000")
result2 = cursor.fetchall()                                         # problem 2
print(result2)'''

'''
result3 = cursor.execute("SELECT * FROM CHICAGO_CRIME_DATA")
print(result3.description)                                          # problem 3
result3 = cursor.execute("SELECT * FROM CENSUS_DATA")
print(result3.description)'''

'''
cursor.execute("SELECT * FROM CHICAGO_CRIME_DATA WHERE PRIMARY_TYPE LIKE '%kidnap%'")
result4 = cursor.fetchall()                                         # problem 4
print(result4)'''

'''
cursor.execute("SELECT DISTINCT(PRIMARY_TYPE) FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION LIKE '%school%'")
result5 = cursor.fetchall()
for x in result5:                                                   # problem 5
    print(x)'''

'''
cursor.execute("SELECT AVG(SAFETY_SCORE) , `Elementary, Middle, or High School` FROM CHICAGO_PUBLIC_SCHOOLS_DATA "
               "GROUP BY `Elementary, Middle, or High School`")
result6 = cursor.fetchall()                                         # problem 6
for x in result6:
    print(x)
'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME , PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CENSUS_DATA ORDER BY "
               "PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5")
result7 = cursor.fetchall()                                         # problem 7 
for x in result7:
    print(x)'''


result8 = cursor.execute("SELECT * FROM CENSUS_DATA")
print(result8.description)
result8 = cursor.execute("SELECT * FROM CHICAGO_CRIME_DATA")
print(result8.description)

