from flask import Flask
app = Flask(__name__) #create instance of class Flask


@app.route("/")
def being():
    return "<a href='/static/text.html'> Go here </a>"

@app.route("/static")
def hello_world(): #assign fxn to route
    return text.html



app.debug = True

if __name__ == "__main__":
    app.debug = True
    app.run()
