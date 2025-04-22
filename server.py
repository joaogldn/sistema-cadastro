from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

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
        return "Erro: A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiuscula e um numero."

    return f"Cadastro realizado com sucesso, {nome}!"

def validar_email(email):
    import re
    return re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email)

def validar_senha(senha):
    import re
    return re.match(r'^(?=.*[A-Z])(?=.*\d).{8,}$', senha)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
