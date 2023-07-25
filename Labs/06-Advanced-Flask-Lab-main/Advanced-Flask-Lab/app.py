from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aHVtYW58ZW58MHx8MHx8fDA%3D&w=1000&q=80"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."

posts = {
    "https://uploads-ssl.webflow.com/5dd64bd3a930f96c82bd137a/637278e457690911a769fd9e_2022%20Causematch%20-%20Website%20-%20News.png": "2021 cohort's Y3 Accelerator!",
    "https://news.mit.edu/sites/default/files/styles/news_article__image_gallery/public/images/201711/MEET-summer-2017-MIT-00.jpeg?itok=4Koi2yME": "MEET graduation!",
    "https://pbs.twimg.com/media/FPvsO6xVkAEcrBm?format=jpg&name=900x900": "#Throwback to one of our favorite #MEETsummer events: #BowlingNight!",
    "https://pbs.twimg.com/media/FI_UkcnVIAAUvWN?format=jpg&name=medium": "2020 cohort in their Y1 summer!"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', image_link = image_link, user_bio = user_bio, posts = posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
