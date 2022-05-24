from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Block9 - Fase 5 by: Jonathan"

if __name__ == '__main__':
    app.run()
    
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run()