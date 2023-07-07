from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'vinland saga'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    print(session)
    if 'key' in session:
        print("Got one")
    else:
        session['key'] = 1
        print("There is now")
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/reset')
def eat_cookies():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)