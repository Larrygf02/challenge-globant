import json


def transform_results(query_result, columns):
    transformed_data = []

    for item_result in query_result:
        record = {}
        for i in range(len(columns)):
            record[columns[i]] = item_result[i]
        transformed_data.append(record)

    #transformed_data = json.loads(record)
    return transformed_data
