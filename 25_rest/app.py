# Mohtasim Howlader
# SoftDev1 pd8
# K25 -- Getting More REST
# 2018-11-15

from flask import Flask, render_template, request, session, url_for, redirect, flash
from urllib import request, parse
import json

app=Flask(__name__)

@app.route("/")
def home():
    apiData = request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=London&APPID=1d18700111907e62e27adc5fa89fad1a")
    apiData = apiData.read()
    dict = json.loads(apiData)
    icon = dict["weather"][0]["icon"]
    iconUrl="http://openweathermap.org/img/w/" + icon + ".png"

    #return "Hello"
    return render_template("home.html", img = iconUrl,  expl = dict["weather"][0]["description"])


if __name__ == "__main__":
    app.debug = True
    app.run()
