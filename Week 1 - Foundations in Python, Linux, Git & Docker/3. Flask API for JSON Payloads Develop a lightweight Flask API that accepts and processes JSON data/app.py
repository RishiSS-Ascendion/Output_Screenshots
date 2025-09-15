from flask import Flask, request, jsonify

app = Flask(__name__)

# Example route to accept JSON
@app.route('/process', methods=['POST'])
def process_json():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()  # Parse JSON payload

    # Example processing: echo back data with modifications
    name = data.get("name", "Guest")
    age = data.get("age", None)

    response = {
        "message": f"Hello, {name}!",
        "age": age,
        "status": "Processed successfully"
    }

    return jsonify(response), 200


# A GET route to test API is running
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask JSON API is running!"})


if __name__ == '__main__':
    app.run(debug=True)
