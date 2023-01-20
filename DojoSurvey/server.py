from flask import Flask, session, request, render_template, redirect

app = Flask(__name__)
app.secret_key = "a totally secure secret key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process ():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/result')

@app.route('/result')
def success():
    return render_template ('result.html')

if __name__ == "__main__":
    app.run(debug = True)