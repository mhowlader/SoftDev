# Mohtasim Howlader
# SoftDev1 pd8
# K25 -- Getting More REST
# 2018-11-15

import json
from urllib import request, parse


from flask import Flask, render_template, request, session, url_for, redirect, flash


app=Flask(__name__)

@app.route("/")
def home():


    #return "Hello"
    return render_template("home.html")

@app.route("/countries")
def restcountry():
    countryName= "Japan"
    cApi=request.urlopen("https://restcountries.eu/rest/v2/name/" + countryName)
    cApi = cApi.read()
    dict = json.loads(cApi)

    return render_template("countries.html",name = dict[0]["name"], region = dict[0]["region"], pop = dict[0]["population"], gini = dict[0]["gini"], mainLang = dict[0]["languages"][0]["name"], flag = dict[0]["flag"])

@app.route("/got")
def got():
    rApi=request.urlopen("https://api.got.show/api/characters/jon%20snow")
    rApi= rApi.read()
    dict = json.loads(rApi)

    return render_template("got.html", name = dict["data"]["name"], pic = "https://api.got.show/" + dict["data"]["imageLink"], cult = dict["data"]["culture"], male = dict["data"]["male"], house = dict["data"]["house"])

@app.route("/crime")
def crime():
    cdapi=request.urlopen("https://api.usa.gov/crime/fbi/sapi/api/estimates/states/ny?api_key=rUS6xtPNirs00gqsZjQEOjU5PTh9oc1gRm7rPVD6")
    cdapi = cdapi.read()
    dict= json.loads(cdapi)

    return render_template("crime.html",year = dict["results"][0]["year"], pop = dict["results"][0]["population"], vcrime = dict["results"][0]["violent_crime"], homicide = dict["results"][0]["homicide"], arson = dict["results"][0]["arson"])

if __name__ == "__main__":
    app.debug = True
    app.run()
