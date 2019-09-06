from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = '' //Please add database name from mlab
app.config['MONGO_URI'] = '' //Please add mongodb URI from mlab

mongo = PyMongo(app)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    pizzaList = mongo.db.pizza.find()
    return dumps(pizzaList)

if __name__ == '__main__':
    app.run(debug=True)
