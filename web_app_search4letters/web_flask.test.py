from flask import Flask, request, render_template
from vsearch import search_letters, print_die_login_daten

# ein Object der Klasse Flask instanziiren:
app = Flask(__name__)

class A:
    def __init__(self, parameter1, parameter2):
        self.name=parameter1
        self.age=parameter2

a = A('John', 12)

# startseite anlegen:
# startseite:
# , methods=['GET', 'POST', 'PUT']
@app.route('/') # decorator - für den Würzelverzeichnis
def index():
    # return "Hello World!"
    return render_template("index.html")

@app.route('/search4') # decorator - für den Würzelverzeichnis
def search4():
        return str(search_letters("sdfsdf", "xdfgsdf"))

@app.route('/login', methods=['GET', 'POST', 'PUT'])
def login():
    username = request.args.get('username', default = 'admin', type = str)
    password = request.args.get('password', default = 'admin', type = str)
    return print_die_login_daten(username, password)

@app.route('/main')
def main():
    return 'main'

app.run()
