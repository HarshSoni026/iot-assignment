import dbconnt

conn = dbconnt.get_connection()

# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter department : ")
email = input("Enter email :")
salary = int(input("Enter salary : "))
doj = input("Enter date of joining : ")

query = f"insert into employees values({empid}, '{name}', '{department}', '{email}', {salary},'{doj}');"

# create a cursor
cursor = conn.cursor()

# execute the query
cursor.execute(query)

# commit the changes
conn.commit()

 # close cursor as well as connection
cursor.close()
conn.close()








