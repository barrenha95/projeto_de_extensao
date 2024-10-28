from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import Form
from wtforms import TextAreaField, IntegerField
import modules.json_module
import modules.qr_operations

app = Flask(__name__)
app.secret_key = "auth"


messages = [{'title': 'Register',
             'content': 'Add someone on the event allowed list.'},
            {'title': 'Remove',
             'content': 'Remove someone on the event allowed list.'}
            ]

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['pass'] != app.secret_key:
            error = "Invalid Password"
        else:
            flash("You are successfully login into the Flask Application")
            return redirect(url_for('row'))

    return render_template("login.html", error=error)

# row function for profile.html
@app.route("/profile")
def row():
    return render_template("profile.html")

@app.route('/')
def index():
    return render_template('/index.html', messages=messages)

# More powerful approach using WTForms
class RegistrationForm(Form):
    firstname = TextAreaField('First Name')
    lastname = TextAreaField('Last Name')
    last5cpf = IntegerField('Last 5 CPF digits')
    email = TextAreaField('Email')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    formulary = RegistrationForm(request.form)

    if request.method == 'POST':
        firstname = formulary.firstname.data
        lastname = formulary.lastname.data
        last5cpf = formulary.last5cpf.data
        email = formulary.email.data

        if len(firstname) == 0 or len(lastname) == 0 or len(str(last5cpf)) == 0:
            error = "Please fill the form"
        else:
            jsonoperations = modules.json_module.JsonOperations()
            jsonoperations.add_user(first = firstname, last=lastname, id5 = last5cpf)

            qroperations = modules.qr_operations.QrOperations()
            qroperations.generating_qr(first = firstname, last=lastname, id5 = last5cpf)
            qroperations.sending_qr(first = firstname, email = email)

            error='User registered in the list!'
            return redirect(url_for('index'))

    return render_template('register.html', form=formulary, message=error)


@app.route('/auth/<firstname>/<lastname>/<last5cpf>', methods=['GET'])
def api(firstname, lastname, last5cpf):
    jsonoperations = modules.json_module.JsonOperations()
    check_response = jsonoperations.check_user(first = firstname, last=lastname, id5 = last5cpf)
    
    if check_response == 0:
        return f'param1: {firstname}, param2: {lastname}, param3: {last5cpf} is not registerd.'
    if check_response == 1:
        return f'param1: {firstname}, param2: {lastname}, param3: {last5cpf} is registerd.'
    


#flask run --debug
#example: http://127.0.0.1:5000/auth/average/guy/88745
# http://127.0.0.1:5000/users