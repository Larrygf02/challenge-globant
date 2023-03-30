from .manager import insert_many, execute, read_query

QUERIES = {
    "employees": "INSERT INTO employees(id, name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s, %s)",
    "departments": "INSERT INTO departments(id, department) VALUES (%s, %s)",
    "jobs": "INSERT INTO jobs(id,job) VALUES (%s, %s)"
}


def insert_data(body, table_name):
    try:
        query = QUERIES[table_name]
        data = []
        for item in body:
            values = tuple(item.values())
            data.append(values)
        insert_many(query, data)
        return (True, None)
    except Exception as e:
        return (False, str(e))


def backup_data(table_name):
    try:
        query = f"""
            DROP TABLE IF EXISTS backup_{table_name};
            CREATE TABLE backup_{table_name} AS
            select * from {table_name};
        """
        print(query)
        execute(query)
    except Exception as e:
        return (False, str(e))
    return (True, None)


def restore_data(table_name):
    # verify if exist table
    query = f"select * from backup_{table_name}"
    exists_backup = execute(query)
    if exists_backup:
        query = f"""
            DROP TABLE IF EXISTS {table_name};
            CREATE TABLE {table_name} AS
            select * from backup_{table_name};
        """
        execute(query)
    else:
        return (False, f"No existe backup {table_name}")
    return (True, None)


def group_by_quarter():
    query = """
        SELECT
            d.department,
            j.job,
            COUNT(*) FILTER (WHERE date_trunc('quarter', datetime::timestamp) >= '2021-01-01' AND date_trunc('quarter', datetime::timestamp) < '2021-04-01') AS Q1,
            COUNT(*) FILTER (WHERE date_trunc('quarter', datetime::timestamp) >= '2021-04-01' AND date_trunc('quarter', datetime::timestamp) < '2021-07-01') AS Q2,
            COUNT(*) FILTER (WHERE date_trunc('quarter', datetime::timestamp) >= '2021-07-01' AND date_trunc('quarter', datetime::timestamp) < '2021-10-01') AS Q3,
            COUNT(*) FILTER (WHERE date_trunc('quarter', datetime::timestamp) >= '2021-10-01' AND date_trunc('quarter', datetime::timestamp) < '2022-01-01') AS Q4
        FROM
            employees e
        INNER JOIN departments d
        ON d.id = e.department_id
        INNER JOIN jobs j
        ON j.id = e.job_id
        GROUP BY
            d.department,
            j.job
        ORDER BY
            d.department,
            j.job;
    """

    results = read_query(query)
    return results
