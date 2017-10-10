from flask import Flask, request, jsonify
import os
app = Flask(__name__)

var = []

@app.route("/", methods=['GET'])
def getFunc():
    return jsonify({"var": var})

@app.route("/", methods=['POST'])
def postFunc():
    post = request.get_json()
    var.append(post)
    return jsonify({"var": var})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

