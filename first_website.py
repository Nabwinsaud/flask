from flask import Flask,redirect,url_for
app=Flask(__name__)


@app.route("/")
def home():
	return "<h1>hello this is code with nabin</h1>"



@app.route("/<name>")
def user(name):
	return f"Hello {name}"
	
@app.route("/home")
def admin():
	return redirect(url_for('home'))


if __name__=='__main__':
	app.run()