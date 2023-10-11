import pandas as pd
import csv
import sqlite3
import mysql.connector


# uncomment each task to see the output

# create a local database , connect to it , make a cursor
connection = sqlite3.connect("FinalDB")
cursor = connection.cursor()

# read from csv data files convert it to panda dataframes then add to local database
df = pd.read_csv("ChicagoCensusData.csv")
df.to_sql("CENSUS_DATA", connection, if_exists='replace', index=False, method="multi")

df = pd.read_csv("ChicagoCrimeData.csv")
df.to_sql("CHICAGO_CRIME_DATA", connection, if_exists='replace', index=False, method="multi")

df = pd.read_csv("ChicagoPublicSchools.csv")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", connection, if_exists='replace', index=False, method="multi")

# run some sql queries

'''
cursor.execute("SELECT COUNT(*) FROM CHICAGO_CRIME_DATA")           # problem 1 completed
result1 = cursor.fetchall()
print("total number of crimes = " + str(result1))'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME < 11000")
result2 = cursor.fetchall()                                         # problem 2 completed
print(result2)'''


cursor.execute("SELECT DISTINCT CASE_NUMBER FROM CHICAGO_CRIME_DATA WHERE DESCRIPTION LIKE '%MINOR%'")
result3 = cursor.fetchall()                                         # problem 3 completed
print(result3)

'''
cursor.execute("SELECT * FROM CHICAGO_CRIME_DATA WHERE PRIMARY_TYPE LIKE '%kidnap%'")
result4 = cursor.fetchall()                                         # problem 4 completed
print(result4)'''

'''
cursor.execute("SELECT DISTINCT(PRIMARY_TYPE) FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION LIKE '%school%'")
result5 = cursor.fetchall()
for x in result5:                                                   # problem 5 completed
    print(x)'''

'''
cursor.execute("SELECT AVG(SAFETY_SCORE) , `Elementary, Middle, or High School` FROM CHICAGO_PUBLIC_SCHOOLS_DATA "
               "GROUP BY `Elementary, Middle, or High School`")
result6 = cursor.fetchall()                                         # problem 6 completed
for x in result6:
    print(x)
'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME , PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CENSUS_DATA ORDER BY "
               "PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5")
result7 = cursor.fetchall()                                         # problem 7 completed
for x in result7:
    print(x)'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NUMBER , COUNT(COMMUNITY_AREA_NUMBER) AS NUMBER FROM CHICAGO_CRIME_DATA GROUP BY NUMBER ORDER BY NUMBER DESC LIMIT 1")
result8 = cursor.fetchall()                                         # problem 8 completed
print(result8)'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM CENSUS_DATA)")
result9 = cursor.fetchall()                                         # problem 9 completed
print(result9)'''

'''
cursor.execute("SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE COMMUNITY_AREA_NUMBER = (SELECT "
               "COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT("
               "COMMUNITY_AREA_NUMBER) DESC LIMIT 1)")
result10 = cursor.fetchall()                                        # problem 10 completed
print(result10)'''


