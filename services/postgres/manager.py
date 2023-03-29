import psycopg2
from services.data import transform_results


def get_connection():
    conn = psycopg2.connect("dbname=globant user=postgres password=admin")
    return conn


def bulk_data(path, table_name):
    conn = get_connection()
    cursor = conn.cursor()
    with open(path, 'r') as f:
        cursor.copy_from(f, table_name, sep=',', null='')
        conn.commit()
    conn.close()


def get_data(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'select * from {table_name}')
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    result = transform_results(rows, columns)
    cursor.close()
    conn.close()
    return result
