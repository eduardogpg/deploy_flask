from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo desde PyWombat'

app.run()
