from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# simple storage
items = []
next_id = 1


# home
@app.route('/')
def home():
    return {"message": "API is working"}


# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# GET one item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_one_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "not found"}, 404


# ADD item
@app.route('/items', methods=['POST'])
def add_item():
    global next_id

    data = request.get_json()

    new_item = {
        "id": next_id,
        "name": data.get("name"),
        "brand": data.get("brand")
    }

    items.append(new_item)
    next_id += 1

    return jsonify(new_item)


# UPDATE item
@app.route('/items/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    data = request.get_json()

    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["brand"] = data.get("brand", item["brand"])
            return item

    return {"error": "not found"}, 404


# DELETE item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "deleted"}

    return {"error": "not found"}, 404


# FETCH + ADD from OpenFoodFacts
@app.route('/fetch/<barcode>', methods=['GET'])
def fetch_product(barcode):
    global next_id

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    res = requests.get(url)
    data = res.json()

    if data["status"] == 1:
        product = data["product"]

        new_item = {
            "id": next_id,
            "name": product.get("product_name"),
            "brand": product.get("brands")
        }

        items.append(new_item)
        next_id += 1

        return new_item

    return {"error": "not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)