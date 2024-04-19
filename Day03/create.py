import dbconnt

conn = dbconnt.get_connection()


query = "create table employees(empid INT, name VARCHAR(20), department VARCHAR(20) , email VARCHAR(30), salary INT, date_of_joining VARCHAR(30));"

# create a cursor
cursor = conn.cursor()

# execute the query
cursor.execute(query)

# commit the changes
conn.commit()

 # close cursor as well as connection
cursor.close()
conn.close()








