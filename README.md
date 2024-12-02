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

1. **Obtenha sua chave de API da CoinMarketCap**:
    - Acesse o [site da CoinMarketCap](https://coinmarketcap.com/api/) e crie uma conta.
    - Após o login, você obterá uma chave de API (API Key).

2. **Configure a variável de ambiente `API_KEY`**:

    - No **Linux/macOS**:
      Você pode exportar a variável diretamente no terminal:

      ```bash
      export API_KEY="sua-chave-da-api-aqui"
      ```

      Para garantir que a variável de ambiente seja carregada automaticamente, adicione a linha acima ao seu arquivo `~/.bashrc` ou `~/.zshrc`.

    - No **Windows**:
      No **PowerShell**, você pode definir a variável da seguinte maneira:

      ```powershell
      $env:API_KEY="sua-chave-da-api-aqui"
      ```

      Para definir permanentemente, você pode usar as configurações do sistema ou definir isso em um arquivo de inicialização, como o `$PROFILE` do PowerShell.

## Como Rodar o Script

Depois de configurar o ambiente e a API Key, você pode rodar o script da seguinte maneira:

1. Salve o código Python em um arquivo, por exemplo `bitcoin_price_tracker.py`.

2. Execute o script:

    ```bash
    python bitcoin_price_tracker.py
    ```

O script irá buscar o preço atual do Bitcoin e depois calcular a variação após 2 minutos, exibindo o preço inicial, o preço após 2 minutos e a variação entre eles.

## Exemplo de Saída

```bash
O preço inicial do Bitcoin é: $30000.00
O preço do Bitcoin após 2 minutos é: $30050.00
A variação do preço do Bitcoin em 2 minutos foi: $50.00