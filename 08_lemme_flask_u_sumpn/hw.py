# Mohtasim Howlader
# SoftDev1 pd8
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home():
 return "Home sweet home. <h1> <a href=/login> Try logging in </a> </h1>"
 
@app.route('/login')
def login():
	return "oh no, you can't login. Click <a href=https://www.youtube.com/watch?v=dQw4w9WgXcQ>this</a> to find out how to log in. <br> <h1> <a href=/logout>LOGOUT </a></h1>"
 
@app.route('/logout')
def logout():
	return "No dummy, you can't log out if you're not even logged <i>in</i>. Smh, go back <a href=/>home</a>"
#app.debug = True
app.run()