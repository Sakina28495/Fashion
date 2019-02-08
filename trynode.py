from flask import Flask, render_template
import requests
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def index():
	output = [1,2,3]
	r = requests.post('http://127.0.0.1:4000/api/message', json={"foo": output, "ka": "Mathew is not"})
	return dumps(r)


if __name__ == '__main__':
	app.run()



