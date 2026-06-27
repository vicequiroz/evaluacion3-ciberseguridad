from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Evaluacion 3</title>
        </head>
        <body>
            <h1>Hola Mundo con Flask</h1>
            <p>Aplicacion web para pruebas automatizadas de seguridad con OWASP ZAP.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
