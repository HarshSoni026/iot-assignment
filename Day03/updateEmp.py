import dbconnt
def update_employees(empid,department):
    # get connection
    conn = dbconnt.get_connection()

    # form a query
    query = f"update employees SET department   = %s where empid = %s;"
    val = (department,empid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_employees(4,"MYSTIC_ARTS")












