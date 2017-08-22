from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('base.html')


@app.route("/hello/<name>")
def say_hi(name):
	return render_template('hello.html', name=name)
	
	
@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
	three_last_name = last[0:3]
	two_first_name = first[0:2]
	return render_template('jedi.html', first=three_last_name, last=two_first_name)
	
	
if __name__ == "__main__":
	app.run(debug=True, host=environ['IP'], port=int(environ['PORT']))