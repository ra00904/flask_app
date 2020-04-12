from flask import Flask, render_template


app = Flask(__name__)

#Routes maps URLs to functions
@app.route('/')
def home() :
    return render_template('index.html') 

@app.route('/PM_Website')
def PM_Website() :
    return render_template('PM_Website.html') 


    app.run()
    