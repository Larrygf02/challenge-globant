from .manager import insert_many, execute

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
