# Team Perry (Mohtasim Howlader and Sarar Aseer)
# SoftDev1 pd8
# K15 -- Oh yes, perhaps I do...
# 2018-10-03

from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
app=Flask(__name__)
app.secret_key=os.urandom(32)# 32 bits of random data as a string


@app.route('/')
def disp_login():
    if 'username' in session: #checks if logged in
        username = session["username"]
        return render_template('LoggedIn.html', user = username)  #inputs are in this this file, which will be sent to auth
    return render_template("home.html")


@app.route('/logout')
def logout():
    session.pop('username') #ends session
    return redirect(url_for('disp_login')) #goes to home, where you can login

@app.route('/auth', methods=["POST"])
def authenticate():
    invalid=None #variable for invalid flash message
    username=request.form['username'] #gets username from form
    password=request.form['password'] #gets password from form
    if username == "perry": #checks if username is correct
        if password == "thePlatypus": #checks if password is correct
            session["username"] = "perry" # sets the username as perry in session
            return redirect(url_for('disp_login')) #calls disp_login, which now sees that you logged in and renders the logged in template
        invalid = "Incorrect Password"   #sets the flash message invalud to this
    else:
        invalid = "Incorrect Username" #sets the flash message invalid to this
    flash(invalid)
    flash("Try Again")
    return redirect(url_for('disp_login'))


if __name__ == "__main__":
    app.debug = True
    app.run()
