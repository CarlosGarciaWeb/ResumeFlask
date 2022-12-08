from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_address = os.getenv("MONGODB_ADDRESS")

client = MongoClient(mongo_address)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True)
