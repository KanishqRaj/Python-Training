from flask import Flask, request, jsonify

app = Flask(__name__)
employee = ["Kanishq" , "Anto" , "Bob" , "Charlie" , "Daniel"]

@app.route("/employee",methods = ["GET"])
def get_employee():
    return jsonify(employee)

@app.route("/employee",methods = ["POST"])
def add_employee():
    data = request.get_json()
    new_emp = data.get("employee")
    employee.append(new_emp)
    return "POST EXECUTED"

@app.route("/employee/<int:index>",methods = ["PUT"])
def update_employee(index):
    data = request.get_json()
    modify_emp = data.get("employee")
    employee[index] = modify_emp
    return "PUT EXECUTED"

@app.route("/employee/<int:index>",methods = ["DELETE"])
def delete_employee(index):
    employee.pop(index)
    return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug = True)


