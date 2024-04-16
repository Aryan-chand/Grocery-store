
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from um")
    cursor.execute(query)
    response = []
    for (um_id, um_name) in cursor:
        response.append({
            'um_id': um_id,
            'um_name': um_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_uoms(connection))