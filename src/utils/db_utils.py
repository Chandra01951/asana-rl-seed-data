def execute_many(conn, query, rows):
    cur = conn.cursor()
    cur.executemany(query, rows)
    conn.commit()
