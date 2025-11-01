#import the requied things to be use
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from datetime import datetime
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
  
# Load environment variables
load_dotenv()

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client.dummydb
collection = db['dummydb']

# Flask app
app = Flask(__name__)

# Home route with form
@app.route('/')
def home():
    
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data Submitted Successfully'
if __name__ == "__main__":
    app.run(debug=True)