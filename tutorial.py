import base64
from flask import Flask, redirect, request
import os
import requests
from urllib.parse import urlencode

app = Flask(__name__)

# Credenciais da aplicação no Bling
CLIENT_ID = 'c4c47013a68b1d18b39683fa50a57defa11570ec'
CLIENT_SECRET = 'a3be2fe1d779a9bc270284d34f5c73c32c66bc1a43320ffa8159b3955ca0'
AUTHORIZATION_URL = 'https://bling.com.br/Api/v3/oauth/authorize'
TOKEN_URL = "https://bling.com.br/Api/v3/oauth/token"

# URL de redirecionamento (deve corresponder à configurada no Bling)
REDIRECT_URI = 'https://a5db-2804-2164-106f-b900-d9ba-3dc2-100b-7cc8.ngrok-free.app/oauth/bling'


@app.route('/', methods=['GET'])
def auth_bling():
    # Gera um estado aleatório para proteção contra CSRF
    state = os.urandom(16).hex()
    
    # Parâmetros para a URL de autorização
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'state': state,
        'redirect_uri': REDIRECT_URI
    }

    # https://www.bling.com.br/Api/v3/oauth/authorize?response_type=code&client_id=c4c47013a68b1d18b39683fa50a57defa11570ec&state=3385a9fad555857b966385f35de9517a
    # Redireciona o usuário para a página de autorização do Bling
    redirect_url = f'{AUTHORIZATION_URL}?{urlencode(params)}'
    return redirect(redirect_url)


@app.route('/oauth/bling', methods=['GET'])
def oauth_callback():
   
    code = request.args.get('code')
    if not code:
        return "Erro: Código de autorização não encontrado.", 400

    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        'Authorization': f"Basic {auth_header}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    # Faz a requisição para obter o token de acesso
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    token_data = response.json()
    access_token = token_data['access_token']
    if not access_token:
        return "Erro: Token de acesso não encontrado na resposta.", 400

    return f"Token de acesso: {access_token}", 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)