# This Applcation uses the Flask Web Framework. It has a User interface, login function, Configuration and assest
# management function, and Project Management Website.
#
#@author Ralph49
#Date Modified: April 22 6, 2016
#

from flask import *
from functools import wraps


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

#Reset session to default value after user logout
@app.route('/logout')
def logout():
	session.pop ('logged_in', None)
	flash('You were logged out')
	return redirect(url_for ('log'))

@app.route('/Config_Mngt')
def Config_Mngt() :
	return render_template('Config_Mngt')
	
@app.route('/log', methods=['GET', 'POST'])
def log():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'WBITuser' or request.form ['password'] != '!QAZ2wsx':
			error = 'Invalid Credentials. Please try again.'
	else:
#Determine if user is logged_in
		session['logged_in'] = True
		return redirect(url_for('Config_Mngt'))
	return render_template('log.html', error=error)
	
#Log info: Home link and Project Management Webisite link works.
# 127.0.0.1 - - [22/Apr/2020 05:52:52] "?[35m?[1mGET /log HTTP/1.1?[0m" 500 -
#127.0.0.1 - - [22/Apr/2020 05:53:04] "?[37mGET /PM_Website HTTP/1.1?[0m" 200 -
#127.0.0.1 - - [22/Apr/2020 05:53:04] "?[33mGET /js/vendor/modernizr-2.8.3-respond-1.4.2.min.js HTTP/1.1?[0m" 404 -
#127.0.0.1 - - [22/Apr/2020 05:53:04] "?[33mGET /js/main.js HTTP/1.1?[0m" 404 -
#127.0.0.1 - - [22/Apr/2020 05:53:20] "?[37mGET /index HTTP/1.1?[0m" 200 -
#127.0.0.1 - - [22/Apr/2020 05:53:20] "?[33mGET /js/vendor/modernizr-2.8.3-respond-1.4.2.min.js HTTP/1.1?[0m" 404 -
#127.0.0.1 - - [22/Apr/2020 05:53:20] "?[33mGET /js/main.js HTTP/1.1?[0m" 404 -
#127.0.0.1 - - [22/Apr/2020 05:53:30] "?[37mGET /index HTTP/1.1?[0m" 200 -
#127.0.0.1 - - [22/Apr/2020 05:53:30] "?[33mGET /js/vendor/modernizr-2.8.3-respond-1.4.2.min.js HTTP/1.1?[0m" 404 -
#127.0.0.1 - - [22/Apr/2020 05:53:30] "?[33mGET /js/main.js HTTP/1.1?[0m" 404 - 
#
#
#
#However Login link is still not working. I think the problem has something do with a route in the app. py file
# See error message below: 
# 
#

#[2020-04-22 05:59:30,694] ERROR in app: Exception on /log [GET]
#Traceback (most recent call last):
#File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 2447, in wsgi_app
#  response = self.full_dispatch_request()
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 1952, in full_dispatch_request
#   rv = self.handle_user_exception(e)
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 1821, in handle_user_exception
#    reraise(exc_type, exc_value, tb)
# File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\_compat.py", line 39, in reraise
#   raise value
# File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 1950, in full_dispatch_request
#   rv = self.dispatch_request()
# File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 1936, in dispatch_request
#   return self.view_functions[rule.endpoint](**req.view_args)
# File "c:/Users/Ralph49/flask_app/app.py", line 41, in log
#    error = None
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\helpers.py", line 370, in url_for
#    return appctx.app.handle_url_build_error(error, endpoint, values)
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\app.py", line 2216, in handle_url_build_error
#    reraise(exc_type, exc_value, tb)
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\_compat.py", line 39, in reraise
#    raise value
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\flask\helpers.py", line 358, in url_for
#    endpoint, values, method=method, force_external=external
#  File "C:\Users\Ralph49\flask_app\flaskenv\lib\site-packages\werkzeug\routing.py", line 2179, in build
#    raise BuildError(endpoint, values, method, self)
#werkzeug.routing.BuildError: Could not build url for endpoint 'Config_Mngt'. Did you mean 'Config_Mgnt' instead?
#127.0.0.1 - - [22/Apr/2020 05:59:30] "?[35m?[1mGET /log HTTP/1.1?[0m" 500 -






















	

app.run()
    