from flask import Flask, jsonify
from services.postgres import get_data

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


if __name__ == '__main__':
    app.run()
