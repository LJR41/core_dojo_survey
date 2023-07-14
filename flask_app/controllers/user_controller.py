from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users_model import Dojo
from flask_app import DATABASE



# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
# # we redirect to the template with the form.
#         return redirect('/')
# # ... do other things
#     return redirect('/dashboard')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not Dojo.validate_user(request.form):
        return redirect('/')
    id = Dojo.create_user(request.form)
    return redirect(f'/dojo/{id}/show')

@app.route('/dojo/<int:id>/show')
def results(id):
    data = {
        'id': id
    }
    one_dojo = Dojo.show_dojo(data)
    return render_template('results.html', one_dojo=one_dojo)

@app.route('/reset')
def eat_cookies():
    session.clear()
    return redirect('/')