from flask import Flask, jsonify
import requests

app = Flask(__name__)

BOUTIQUE_API = "https://vitrina.hstn.me/api/boutiques"

@app.route("/boutiques")
def boutiques():
    try:
        response = requests.get(BOUTIQUE_API, timeout=10)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=5000)