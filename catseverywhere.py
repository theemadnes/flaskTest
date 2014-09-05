from flask import Flask, render_template
from flask import request, redirect

email_addresses = []

app = Flask(__name__)

@app.route('/')
def hello_world():

	author = 'Alex'
	name = 'Alex in another state'
	return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    

    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == '__main__':

	app.run()
