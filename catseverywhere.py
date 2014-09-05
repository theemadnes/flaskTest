from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():

	author = 'Alex'
	name = 'Alex in another state'
	return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    
    name = request.form['name']
    print("The name is '" + name + "'")

    email = request.form['email']
    print("The email address is '" + email + "'")

    # spam = 0
    # spam = request.form['spam']
    # want_spam = False
    if 'spam' in request.form:
    	print("dog")
    else:
    	print("cat")

    return redirect('/')

if __name__ == '__main__':

	app.run()
