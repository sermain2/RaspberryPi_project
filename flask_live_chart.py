import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from flask_restful import reqparse
from ServerData import ServerData

app = Flask(__name__)
server_Data = ServerData(None)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/send-data", methods=["POST"])
def send_data():
    parser = reqparse.RequestParser()
    parser.add_argument("temperature", type=str)
    args = parser.parse_args()

    server_Data.insert_data(args["temperature"])
    print(args["temperature"])
    return {"send": args["temperature"]}


@app.route("/live-data")
def live_data():
    data = [time() * 1000, float(server_Data.get_data()), random() * 100]
    print(data)
    response = make_response(json.dumps(data))
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="192.168.25.26", port=5000)
