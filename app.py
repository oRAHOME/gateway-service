from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

# Microservice endpoint URLs
services = {
    "auth": "http://localhost:5001",
    "user": "http://localhost:5002",
}


@app.route("/api/v1/<service_name>/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def route_request(service_name, path):
    # Route requests to the appropriate microservice.
    if service_name not in services:
        return jsonify({"error": "Service not found."}), 404

    service_url = f"{services[service_name]}/{path}"
    try:
        response = requests.request(
            method=request.method,
            url=service_url,
            headers={key: value for key, value in request.headers if key != "Host"},
            json=request.get_json(),
            params=request.args
        )
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Service unreachable.", "details": str(e)}), 500


@app.route("/")
def home():
    return jsonify({"message": "Success!"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
