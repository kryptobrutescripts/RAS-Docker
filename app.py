from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Início</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 80px;
            }
            h1 { color: #38bdf8; }
            a { color: #7dd3fc; margin: 0 10px; }
        </style>
    </head>
    <body>
        <h1>Bem-vindo ao Flask no Docker</h1>
        <p>Kali Linux - Trabalho RASI</p>
        <p>
            <a href="/sobre">Sobre</a>
            <a href="/contato">Contato</a>
        </p>
    </body>
    </html>
    '''


@app.route("/sobre")
def sobre():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Sobre</title>
        <style>
            body {
                font-family: Arial;
                background: #172554;
                color: white;
                text-align: center;
                padding-top: 80px;
            }
            h1 { color: #60a5fa; }
            a { color: #bfdbfe; }
        </style>
    </head>
    <body>
        <h1>Sobre o Projeto</h1>
        <p>Aplicação Python Flask executada em um container Docker.</p>
        <p><a href="/">Voltar</a></p>
    </body>
    </html>
    '''


@app.route("/contato")
def contato():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Contato</title>
        <style>
            body {
                font-family: Arial;
                background: #431407;
                color: white;
                text-align: center;
                padding-top: 80px;
            }
            h1 { color: #fb923c; }
            a { color: #fed7aa; }
        </style>
    </head>
    <body>
        <h1>Contato</h1>
        <p>Trabalho RASI - Docker com Python/Flask.</p>
        <p>Aluno: Bruno Henrryke Marcelino de Souza</p>
        <p><a href="/">Voltar</a></p>
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
