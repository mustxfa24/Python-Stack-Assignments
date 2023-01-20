from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "1000 percent a secret key for sure"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/2')
def two():
    if "count" not in session:
        session['count'] = 0
    else:
        session['count'] += 2
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)