from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "something-from-os.urandom(24)"
 
 
@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True
 
@app.route("/")
def index():
    # reset the session data
    session.clear()
    session["foo"] = "Foo"
    return render_template("indexsam.html")
 
@app.route("/foo")
def foo():
    # retrieve "Foo" from the persistent session object
    foo = session["foo"]
    return render_template("404.html")

if __name__=="__main__":
	app.run()