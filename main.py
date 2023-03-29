from flask import Flask, jsonify
from services.postgres import get_data

app = Flask(__name__)


@app.route("/employee")
def get_employee():
    data = get_data('employees')
    return jsonify(data)


if __name__ == '__main__':
    app.run()
