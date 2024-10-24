from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import TextAreaField, IntegerField

app = Flask(__name__)

messages = [{'title': 'Register',
             'content': 'Add someone on the event allowed list.'},
            {'title': 'Remove',
             'content': 'Remove someone on the event allowed list.'}
            ]

@app.route('/')
def index():
    return render_template('/index.html', messages=messages)

# More powerful approach using WTForms
class RegistrationForm(Form):
    firstname = TextAreaField('First Name')
    lastname = TextAreaField('Last Name')
    last5cpf = IntegerField('Last 5 CPF digits')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        firstname = form.firstname.data
        lastname = form.lastname.data
        last5cpf = form.last5cpf.data

        if len(firstname) == 0 or len(lastname) == 0 or len(str(last5cpf)) == 0:
            error = "Please fill the form"

    return render_template('register.html', form=form, message=error)


@app.route('/auth/<firstname>/<lastname>/<last5cpf>', methods=['GET'])
#example: http://127.0.0.1:5000/auth/average/guy/88745
def api(firstname, lastname, last5cpf):
    return f'param1: {firstname}, param2: {lastname}, param3: {last5cpf}'


#app.run()

# http://127.0.0.1:5000/users