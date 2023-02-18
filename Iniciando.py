
import requests as nb

#link = "https://projeto2semestre-1f235-default-rtdb.firebaseio.com/"

#requisição = nb.get(f'{link}/Veiculo/.json')
#print(requisição)
#dic_requisição = requisição.json()
#for id_veiculo in dic_requisição:
    #Placa = dic_requisição[id_veiculo]['Placa']
    #Pesquisa = input('Qual é a placa?')
    #if Placa == Pesquisa:
        #print('Placa')

estoque_de_carros = []1

def cadastrar():
    #cadastrando veículo
    veiculo = {
        'Placa': "",
        'Montadora': "",
        'Modelo': "",
        'Ano': 0,
    }

    print("Digite os campos abaixo para cadastrar um veículo:")
    for indice in veiculo:
        veiculo[indice] = input(indice + ": ")

    estoque_de_carros.append(veiculo)
    print("veiculo cadastrado com sucesso.")
    
    return

def pesquisar():
    print('pesquisando carro')
    return

def imprimir():
    #imprimindo lista de carros
    print('Estoque de Carros')
    print("Placa".center(14), end='')
    print("Montadora".center(18),end='')
    print("Modelo".center(12))
    print("Ano".center(8))

    for veiculo in estoque_de_carros:
        print(str(veiculo['Placa']).center(14), end='')
        print(str(veiculo['Montadora']).center(18), end='')
        print(str(veiculo['Modelo']).center(12), end='')
        print(str(veiculo['Ano']).center(20), end='')
    return
def remover():
    print('removendo carro')
    return

def atualizar():
    print('atualizando carro')
    return
    
def exibe_menu():
    print("Menu")
    print("1 - cadastrar veiculo")
    print("2 - pesquisar veiculo")
    print("3 - imprimir veiculos cadastrados")
    print("4 - remover veiculo")
    print("5 - atualizar veiculo")
    print("0 - sair")

exibe_menu()    
opcao = int(input())


while 0 <= opcao <=5:

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        imprimir()
    elif opcao == 4:
        remover()   
    elif opcao == 5:
        atualizar()    
    elif opcao == 0:
        print('Programa encerrado') 
        exit()

    exibe_menu()
    opcao = int(input())

else:
    print('Opção inválida, programa encerrado')
