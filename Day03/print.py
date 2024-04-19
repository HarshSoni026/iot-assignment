import dbconnt

def print_employees():
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query = "select * from employees;"

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    for rec in records:

        print(rec)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



print_employees()


def employees_given_department(department):
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query = f"select name from employees where department = %s;"
    val = (department,)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query,val)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    for rec in records:

        print(rec)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

employees_given_department("VLSI_DESIGNING")

def employees_highest_salary():
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query1 = f"select *from employees order by salary DESC LIMIT 1;"
     
    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query1,)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    for rec in records:

        print(rec)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

employees_highest_salary()

def employees_lowest_salary():
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query = f"select *from employees order by salary ASC LIMIT 1;"
     
    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query,)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    for rec in records:

        print(rec)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()

employees_lowest_salary()
