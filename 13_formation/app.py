# Mohtasim Howlader
# SoftDev1 pd8
# K13 -- Echo Echo Echo
# 2018-09-27

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('echo.html')  #inputs are in this this file, which will be sent to auth


@app.route('/auth')
def authorize():
    username=request.form['username']
    password=request.form['password']

    

if __name__ == "__main__":
    app.debug = True
    app.run()
