from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://username:password@cluster0.v70j0.mongodb.net/helthtaker'
mongo = PyMongo(app)



