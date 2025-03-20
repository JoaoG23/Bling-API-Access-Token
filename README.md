# Bling OAuth Example

Este repositório contém um exemplo de integração com a API OAuth do Bling. Inclui um servidor Flask para autenticação e obtenção do token de acesso. Certifique-se de configurar corretamente as credenciais (Client ID, Client Secret) e a URL de redirecionamento antes de executar.

**Como usar:**
1. Configure as credenciais no código:
    - **Client ID**: Identificador único da aplicação.
    - **Client Secret**: Chave secreta usada para autenticação.
2. Execute o servidor Flask.
3. Acesse a URL gerada pelo servidor e siga o fluxo de autenticação:
    - Você será redirecionado para a página de login do Bling.
    - Após autenticar, será redirecionado para a URL configurada com o código de autorização.
    - O servidor trocará o código pelo token de acesso.

O token de acesso pode ser usado para realizar chamadas autenticadas à API do Bling.
