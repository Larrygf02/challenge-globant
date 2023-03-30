from jsonschema import validate

SCHEMAS = {
    "employees": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "datetime": {"type": "string", "format": "date-time"},
            "department_id": {"type": "integer"},
            "job_id": {"type": "integer"}
        },
        "required": ["id", "name", "datetime", "department_id", "job_id"]
    },
    "departments": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "department": {"type": "string"},
        },
        "required": ["id", "department"]
    },
    "jobs": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "job": {"type": "string"},
        },
        "required": ["id", "job"]
    }
}


def validate_body(body, table_name):
    schema = SCHEMAS[table_name]
    for item in body:
        try:
            validate(instance=item, schema=schema)
        except Exception as e:
            return (False, f"{item} is not valid, error: {e}")
    return (True, None)


def transform_results(query_result, columns):
    transformed_data = []

    for item_result in query_result:
        record = {}
        for i in range(len(columns)):
            record[columns[i]] = item_result[i]
        transformed_data.append(record)

    #transformed_data = json.loads(record)
    return transformed_data
