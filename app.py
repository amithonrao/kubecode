from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Congrs!!!... We successfully finished the Project, TY!!!'
