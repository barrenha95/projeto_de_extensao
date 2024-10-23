from flask import Flask, render_template#, jsonify

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('/index.html', messages=messages)

#@app.route('/auth/<firstname>/<lastname>/<last5cpf>', methods=['GET'])
##example: http://127.0.0.1:5000/auth/average/guy/88745
#def api(firstname, lastname, last5cpf):
#    return f'param1: {firstname}, param2: {lastname}, param3: {last5cpf}'


#app.run()

# http://127.0.0.1:5000/users