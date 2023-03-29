import psycopg2


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
