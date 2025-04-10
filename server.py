from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def form():
    with open("form.html") as f:
        return f.read()

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome'].strip()
    email = request.form['email'].strip()
    senha = request.form['senha']

    if len(nome) < 3:
        return "Erro: Nome deve ter pelo menos 3 caracteres."

    if not validar_email(email):
        return "Erro: E-mail inválido."

    if not validar_senha(senha):
        return "Erro: A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula e um número."

    return f"Cadastro realizado com sucesso, {nome}!"

def validar_email(email):
    import re
    return re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email)

def validar_senha(senha):
    import re
    return re.match(r'^(?=.*[A-Z])(?=.*\d).{8,}$', senha)

if __name__ == '__main__':
    app.run(debug=True)
