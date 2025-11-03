from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.todo_db
collection = db.todo_items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()
    todo_item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    result = collection.insert_one(todo_item)
    return jsonify({
        "message": "To-Do item saved successfully!",
        "id": str(result.inserted_id)
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

