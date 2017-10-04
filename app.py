from flask import Flask, render_template, request, session
import os

master_username = "hello"
master_password = "password"

SESSION_KEY = "lol"

app = Flask(__name__)
app.secret_key = os.urandom(8)

@app.route("/", methods=["GET", "POST"])
def root():
	username = ""
	password = ""
	if request.method == "GET":
		if request.args:
			username = request.args["username"]
			password = request.args["password"]
		else:
			return render_template("index.html")

	elif request.method == "POST":
		if request.form:
			username = request.form["username"]
			password = request.form["password"]
		else:
			return render_template("index.html")
	
	if username == "" or username != master_username:
		return render_template("index.html", bad_username=True)
	
	if password == "" or password != master_password:
		return render_template("index.html", bad_password=True)
	
	session[SESSION_KEY] = username
	
	return render_template("index.html", 
				username=username)
	
	return render_template("index.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
