import mysql.connector

def get_cliente_by_id(cliente_id):
    conn = mysql.connector.connect(
        host='db-clientes',
        user='root',
        password='root',
        database='clientesdb'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
    result = cursor.fetchone()
    conn.close()
    return result
