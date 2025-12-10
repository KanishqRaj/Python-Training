
from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database connection
DB = {
    "host": "localhost",
    "user": "root",
    "password": "Kanishq@0610",
    "database": "employee_flask",
    # "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True
}

def get_conn():
    return pymysql.connect(**DB)

@app.route('/employee', methods=['GET'])
def get_all():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employee")
            return jsonify(cur.fetchall())

@app.route('/employee/<int:emp_id>', methods=['GET'])
def get_one(emp_id):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employee WHERE emp_id=%s", (emp_id,))
            row = cur.fetchone()
            return jsonify(row if row else {"error": "Not found"})

@app.route('/employee', methods=['POST'])
def create():
    data = request.get_json()
    emp_id, name, city, dept = data.get('emp_id'), data.get('name'), data.get('city'), data.get('dept')
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employee VALUES (%s,%s,%s,%s)", (emp_id, name, city, dept))
            return jsonify({"message": "Created", "emp_id": emp_id}), 201

@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update(emp_id):
    data = request.get_json()
    name, city, dept = data.get('name'), data.get('city'), data.get('dept')
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE employee SET name=%s, city=%s, dept=%s WHERE emp_id=%s", (name, city, dept, emp_id))
            return jsonify({"message": "Updated"})

@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete(emp_id):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employee WHERE emp_id=%s", (emp_id,))
            return jsonify({"message": "Deleted"})

# ----------- Run App -----------
if __name__ == '__main__':
    app.run(debug=True)
