from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Block9 - Fase 5 by: Jonathan"

if __name__ == '__main__':
    app.run()