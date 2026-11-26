from flask import Flask, jsonify, request
app = Flask(__name__)
items = []

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/items")
def list_items():
    return jsonify(items)

@app.post("/api/items")
def add_item():
    items.append(request.get_json())
    return jsonify(ok=True), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
