from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("mars_index.html", listings=listings)

@app.route("/scrape")
def scraper():
    # create mongo db named mars
    listings = mongo.db.listings
    # call scrape.py and assign returned dict to variable mars_data
    listings_data = scrape.scrape()
    # update mars 
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)