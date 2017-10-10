from flask import Flask, request, jsonify
import urllib2
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
    app.run()

