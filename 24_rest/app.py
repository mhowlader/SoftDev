# Mohtasim Howlader
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-14

from flask import Flask, render_template, request, session, url_for, redirect, flash
from urllib import request, parse
import json

app=Flask(__name__)

@app.route("/")
def home():
    nasa_in = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=9kjFb1X6GKVUdknUZKkyNvCaIiioetBM8ug3I6gj")
    nasa_in = nasa_in.read()
    nDict = json.loads(nasa_in)

    return render_template("home.html", img=nDict['url'], expl=nDict['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
