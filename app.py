from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuração de E-mail (Para você receber os dados)
def enviar_email(dados):
    msg = MIMEText(f"Nova Clínica Cadastrada:\n\n{dados}")
    msg['Subject'] = f"Novo Onboarding: {dados.get('nome_clinica')}"
    msg['From'] = "sistema@sistemasnewscreen.com.br"
    msg['To'] = "SEU_EMAIL_AQUI"
    # Aqui configuraríamos o servidor SMTP (Gmail, Outlook, etc)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/onboarding')
def onboarding():
    return render_template('onboarding.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    dados = request.form.to_dict()
    # Enviar email ou salvar no banco de dados aqui
    return redirect(url_for('sucesso'))

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == "__main__":
    app.run()