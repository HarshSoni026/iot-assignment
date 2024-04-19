import dbconnt

def delete_employees(empid):
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query = f"delete from employees where empid = %s;"
    val = (empid,)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



delete_employees(3)