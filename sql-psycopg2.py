import psycopg2

#connect to "chinook" database
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

#query1 - select all records from the "artist" table
#cursor.execute('SELECT * FROM "Artist"')

#query2 - select 'Name' column from the 'Artist' table
#cursor.execute('SELECT "Name" FROM "Artist"')

#query3 - select only Queen from 'Artist' table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#query4 - select only by artistid 51 from the 'Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#query5 - select albums with artist id of 51 from Album table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#query6 - select all tracks with composer of Queen from "Track" table
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

#Challenge 1
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Green Day"])

#Challenge 2
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

#fetch the results ( multiple)
results = cursor.fetchall()

#fetch a single result
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)