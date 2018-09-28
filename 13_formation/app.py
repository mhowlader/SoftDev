from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    #request.headers()
    return render_template('echo.html')

@app.route('/auth')
def authorize():
    username=request.args['username']
    meth = request.method
    return render_template('auth.html',
                            user=username
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
