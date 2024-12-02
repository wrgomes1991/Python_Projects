# Python_Projects
Some python projects used to study the language that can be usefull.

# Bitcoin Price Tracker

Este script Python utiliza a API da CoinMarketCap para obter o preço atual do Bitcoin e calcular sua variação em 2 minutos. A API Key é necessária para autenticar a solicitação, e a variável de ambiente deve ser configurada para que o script funcione corretamente.

## Pré-requisitos

Antes de executar o script, você precisa garantir que tenha as bibliotecas necessárias instaladas e que a variável de ambiente da chave da API esteja configurada.

### Instalando as dependências

Este script usa a biblioteca `requests` para fazer as requisições HTTP à API da CoinMarketCap. Para instalar as dependências, siga os passos abaixo:

1. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    - No **Windows**:

      ```bash
      .\venv\Scripts\activate
      ```

    - No **Linux/macOS**:

      ```bash
      source venv/bin/activate
      ```

3. Instale a biblioteca `requests`:

    ```bash
    pip install requests
    ```

### Configurando a API Key

A chave da API da CoinMarketCap é necessária para fazer as requisições à API. Siga os passos abaixo para configurá-la:

1. **Obtenha sua chave de API da CoinMark
