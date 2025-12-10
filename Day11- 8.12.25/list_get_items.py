from flask import Flask, request, jsonify

app = Flask(__name__)

items = ["Apple", "Banana","Cherry"]

@app.route("/items", methods = ["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods = ["POST"])
def add_items():
    data = request.get_json()
    item = data.get("item")
    items.append(item)
    return "POST EXECUTED"

##PUT
@app.route("/items/<int:index>", methods = ["PUT"])
def update_item(index):
    data = request.get_json()
    new_value = data.get("item")
    items[index] = new_value
    return "PUT EXECUTED"

##DELETE
@app.route("/items/<int:index>", methods = ["DELETE"])
def delete_item(index):
    items.pop(index)
    return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug = True)