# Team Perry (Sarar Aseer and Mohtasim Howlader)
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect
import os
app=Flask(__name__)
app.sceret_key=os.urandom(32)
# session["username"] = "perry"
# session["password"] = "thePlatypus"

@app.route('/')
def disp_login():
    if 'username' in session:
        username = session["username"]
        return render_template('LoggedIn.html', user = username)  #inputs are in this this file, which will be sent to auth
    return render_template("home.html")

@app.route('/logout')
def logout():
    session.pop()
    return redirect(url_for('/'))

@app.route('/auth', methods=["POST"])
def authenticate():
    print (url_for("disp_login")) # Should print out "/"
    print (url_for("authenticate")) # Should print out "/auth"
    

    #return redirect(url_for("disp_login")) # Redirects user to the url that is tied to the function "disp_login"
    # return render_template('auth.html',
    #                         user=username
    #                         )

if __name__ == "__main__":
    app.debug = True
    app.run()
