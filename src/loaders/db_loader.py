def load(conn, dest_table, data):
    cur = conn.cursor()
    if isinstance(data, list):
        # insert batch of records
        placeholders = ', '.join(['?' for i in data[0]])
        insert_query = f"insert into {dest_table} values ({placeholders}) "
        cur.executemany(insert_query, data)
    else:
        # insert single record
        placeholders = ', '.join(['?' for i in data])
        insert_query = f"insert into {dest_table} values ({placeholders}) "
        cur.execute(insert_query, data)
    conn.commit()
