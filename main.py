from flask import Flask, jsonify, request
from services.postgres import get_data, insert_data
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
        print("Error", error)
        if error:
            return jsonify({"status": False, "message": error})
        return jsonify({"status": True})
    else:
        return jsonify({"status": False, "message": message})


if __name__ == '__main__':
    app.run()
