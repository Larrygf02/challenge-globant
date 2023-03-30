from flask import Flask, jsonify, request
from services.postgres import get_data, insert_data, backup_data, restore_data, group_by_quarter, group_employee
from services.data import validate_body

app = Flask(__name__)


@app.route("/employees")
def get_employee():
    data = get_data('employees')
    return jsonify(data)


@app.route("/jobs")
def get_jobs():
    data = get_data('jobs')
    return jsonify(data)


@app.route("/departments")
def get_departments():
    data = get_data('departments')
    return jsonify(data)


@app.route("/employee", methods=['POST'])
def post_employee():
    body = request.get_json()
    validated, message = validate_body(body, 'employees')
    if validated:
        _, error = insert_data(body, 'employees')
        if error:
            return jsonify({"status": False, "message": error})
        return jsonify({"status": True})
    else:
        return jsonify({"status": False, "message": message})


@app.route("/department", methods=['POST'])
def post_department():
    body = request.get_json()
    validated, message = validate_body(body, 'departments')
    if validated:
        _, error = insert_data(body, 'departments')
        if error:
            return jsonify({"status": False, "message": error})
        return jsonify({"status": True})
    else:
        return jsonify({"status": False, "message": message})


@app.route("/job", methods=['POST'])
def post_job():
    body = request.get_json()
    validated, message = validate_body(body, 'jobs')
    if validated:
        _, error = insert_data(body, 'jobs')
        if error:
            return jsonify({"status": False, "message": error})
        return jsonify({"status": True})
    else:
        return jsonify({"status": False, "message": message})


@app.route("/backup", methods=["POST"])
def do_backup():
    body = request.get_json()
    table_name = body['table_name']
    _, error = backup_data(table_name)
    if error:
        return jsonify({"status": True, "message": error})
    return jsonify({"status": True})


@app.route("/restore", methods=["POST"])
def do_restore():
    body = request.get_json()
    table_name = body['table_name']
    _, error = restore_data(table_name)
    if error:
        return jsonify({"status": False, "message": error})
    return jsonify({"status": True})


@app.route("/group_quarter")
def group_quarter():
    results = group_by_quarter()
    return jsonify({"response": results})


@app.route("/group_employees")
def group_employees():
    results = group_employee()
    return jsonify({"response": results})


if __name__ == '__main__':
    app.run()
