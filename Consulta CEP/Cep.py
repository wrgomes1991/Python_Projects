import requests
from tkinter import *
from tkinter import simpledialog

def main():
    while True:

        if len(input_cep.get()) != 8:
            erro_screen["text"] = "CEP não contém 8 caracteres, confirme o número e tente novamente"
            break
        
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(input_cep.get()))
        data = request.json()

        if 'erro' not in data:
            
            num_CEP = data['cep']
            nome_Rua = data['logradouro']
            nome_Bairro = data['bairro']
            num_DDD = data['ddd']
            uf = data['uf']

            info = f'''
            CEP: {num_CEP}
            Rua : {nome_Rua}
            Bairro : {nome_Bairro}
            DDD : {num_DDD}
            Estado: {uf}
            '''

            info_screen["text"] = info


        else:

            Erro = print('CEP inexistente na base, favor confirmar o número')
            erro_screen["text"] = Erro

        continuar = input('Deseja consultar outro CEP ?\n 1 Para SIM\n2 Para SAIR\n')
        if continuar != 1:
            print("Obrigado, até a próxima !")
            break

window = Tk()

window.title("Consulta CEP - BR")
main_screen = Label(window, text="Bem vindo ao sistema de Consulta de CEP")
main_screen.grid(column=0, row=0)

sec_screen = Label(window, text="Insira o CEP desejado:")
sec_screen.grid(column=0, row=1)

input_cep = Entry(window, width="8")
input_cep.grid(column=1, row=1)

Find_CEP = Button(window, text="BUSCAR", command=main)
Find_CEP.grid(column=2, row=1)

CEP = Label(window, text="")
CEP.grid(column=2, row=2)

info_screen = Label(window, text="")
info_screen.grid(column=2, row=3)

erro_screen = Label(window, text="")
erro_screen.grid(column=2, row=4)


window.mainloop()