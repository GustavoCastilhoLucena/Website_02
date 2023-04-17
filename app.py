from flask import Flask, render_template
app = Flask ("__Name__")
@app.route('/')
def home():
    return render_template ("/home.html")

@app.route('/contato')
def contato():
    return render_template ("/contato.html")

@app.route('/quem_somos')
def quem_somos():
    return render_template ("/quem_somos.html")
