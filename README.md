<div allign: "left">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdc3f" alt="Python">
<img src="https://img.shields.io/badge/Flask-000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</div>

# Sistema de Cadastro

Este repositório faz parte da resolução de um desafio de Sistema de Cadastro com etapas de autenticação e validação de campos para maior segurança.

### ⚙️ Requisitos

- Python 3 instalado
- Flask
- Docker instalado


### 🐳 Executando a aplicação com Docker

Siga os passos abaixo para executar a aplicação Flask em um container Docker:

### 📥 1. Clone o repositório

```bash
git clone https://github.com/joaogldn/sistema-cadastro.git
```

### 🛠 2. Construa a imagem Docker

No diretório, onde estão os arquivos do projeto, execute o comando abaixo para construir a imagem Docker:

```bash
docker build -t cadastro-app-flask .
```

### ▶️ 3. Execute o container

```bash
docker run -p 5000:5000 cadastro-app-flask
```

### 🌐 4. Acesse a aplicação

```bash
http://localhost:5000
```



