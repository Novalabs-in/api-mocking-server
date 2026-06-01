from flask import Flask, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route("/api/v1/users", methods=["GET"])
def mock_users():
    """
    Dynamic API Mock Endpoints
    Uses Faker to build synthetic response datasets for developers.
    """
    users = []
    for _ in range(5):
        users.append({
            "id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "company": "Novalabs.in"
        })
    return jsonify(users)

if __name__ == "__main__":
    print("Starting Mock API Server on local port 5000...")
    # In a real run: app.run(port=5000)
