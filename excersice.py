from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/') #127.0.0.1.5000
def index():
	return "<h1>puppy name excercise</h1>"

@app.route('/information') #127.0.0.1.5000/info
def info():
	return "<h1>Thomas is my friend</h1>"

@app.route('/puppy/<name>')
def puppylatin(name):

	pupname=''
	if name[-1]=='y':
		pupname=name[:-1]+'iful'
	else:
		pupname=name+'y'
	return "Puppy name is : {}".format(pupname)

if __name__=='__main__':
	app.run(debug=True) 