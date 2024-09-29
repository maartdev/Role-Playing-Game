import random
import time
import os

#Limpar o Console
def clear_console():
    os.system('cls')

#Sistema de Loja
def loja():
    global armas
    while True:
        try:
            clear_console()
            print('Menu:\n1. Poção\n2. Armas\n3. Sair')
            opcao = int(input('Escolha uma opção: '))

            if opcao == 3:
                clear_console()
                print('Saindo da loja...')
                time.sleep(1.5)
                break

            elif opcao == 1:
                clear_console()
                print('O preço de uma poção de cura é de 5 moedas, é pegar ou largar.')
                time.sleep(1.5)

                while True:
                    qntd_pocao = int(input('Quantas poções deseja comprar? '))
                    if qntd_pocao <= 0:
                        clear_console()
                        print('Nenhuma? você é quem sabe.')
                        time.sleep(1)
                        print('Até mais.')
                        time.sleep(1)
                        break

                    preco_total = qntd_pocao * 5

                    if inventario['Dinheiro'] < preco_total:
                        restante =


        except ValueError:
            clear_console()
            print('Entrada errada, digite um número inteiro.')
            time.sleep(2)




#Atualização de vida

#Atualização de nível

#Exibir os status

#Sistema de Batalha