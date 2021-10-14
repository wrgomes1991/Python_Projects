import requests

def main():
    print("Bem vindo ao sistema de Consulta de CEP")

    cep = input("Qual CEP deseja buscar ? Utilizar apenas números.\n")

    if len(cep) != 8:

        print("Formato de CEP inválido, o CEP deve conter 8 caracteres e somente números !")

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    data = request.json()

    #print(data)
    if 'erro' not in data:
        print('CEP:{}'.format(data['cep']))
        print('Rua:{}'.format(data['logradouro']))
        print('Bairro: {}'.format(data['bairro']))
        print('DDD:{}'.format(data['ddd']))
    else:
        print('CEP inexistente na base, favor confirmar o número')

main()


