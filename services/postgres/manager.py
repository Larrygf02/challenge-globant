import psycopg2


def get_connection():
    conn = psycopg2.connect("dbname=globant user=postgres password=admin")
    return conn


def bulk_data(path):
    conn = get_connection()
    cursor = conn.cursor()
    with open(path, 'r') as f:
        cursor.copy_from(f, 'employees', sep=',', null='')
        conn.commit()
    conn.close()
