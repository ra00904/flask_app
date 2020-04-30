# This Applcation uses the Flask Web Framework. It has a User interface, login function, Configuration and assest
# management function, and Project Management Website.
#
#@author Ralph49
#Date Modified: April 22 6, 2016
#

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from functools import wraps
from mock_data import lists


app = Flask(__name__)

#Add secret key to protect session files
app.secret_key = 'V2K9tAOL6853601w'


#Routes map URLs to functions
@app.route('/')
@app.route('/index')
def index() :
    return render_template('index.html') 

@app.route('/PM_Website')
def PM_Website() :
    return render_template('PM_Website.html') 
#Routes to PM_Website documents




@app.route('/PM_Website/PCharter')
def PC() :
    return render_template('PC.html') 

@app.route('/PM_Website/PPlan')
def PPL() :
    return render_template('PPlan.html')

@app.route('/PM_Website/WLog')
def WR() :
    return render_template('WR.html')

@app.route('/Config_Mngt')
def Config_Mngt() :
	return render_template('Config_Mngt.html')

#route to handle displaying the lists of assets

@app.route("/lists", methods=['GET'])
def get_lists():
    return jsonify({'lists': lists})



#route for login page
@app.route('/log', methods=['GET', 'POST'])
def log():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'WBITuser' or request.form ['password'] != '!QAZ2wsx':
			error = 'Invalid Credentials. Please try again.'
	else:
#Determine if user is logged_in
		session['logged_in'] = True
		flash('You are logged in')
		return redirect(url_for('Config_Mngt'))
	return render_template('log.html', error=error)

#Reset session to default value after user logout
@app.route('/logout')
def logout():
	session.pop ('logged_in', None)
	flash('You were logged out')
	return redirect(url_for ('index'))


	
if __name__ == '__main__':
	app.run()
    