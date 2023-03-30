from .manager import insert_many

QUERIES = {
    "employees": "INSERT INTO employees(id, name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s, %s)"
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
