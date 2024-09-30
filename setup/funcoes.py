import random
import time
import os
import variaveis

#Limpar o Console
def clear_console():
    os.system('cls')

#Sistema de Loja
def loja():
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

                    if variaveis.inventario['Dinheiro'] < preco_total:
                        restante = preco_total - variaveis.inventario['Dinheiro']
                        clear_console()
                        print(f'Você só tem {variaveis.inventario["Dinheiro"]} moedas. Faltam {restante} moedas.')
                        time.sleep(2)
                        break

            elif opcao == 2:
                clear_console()
                print('Armas disponíveis:')
                for i, arma in enumerate(variaveis.armas, 1):
                    print(f'{i}. {arma["Nome"]} - {arma['Preco']} moedas')

                opcao_armas = int(input('Escolha uma arma para comprar: '))

                if 1 <= opcao_armas <= len(variaveis.armas):
                    arma = variaveis.armas[opcao_armas - 1]
                    if variaveis.inventario['Dinheiro'] >= arma['Preco']:
                        variaveis.inventario['Armas'][arma['Nome']] = arma['Dano']
                        variaveis.inventario['Dinheiro'] -= arma['Preco']
                        clear_console()
                        print(f'Você comprou a {arma["Nome"]}. Boa compra!')
                        time.sleep(3)
                        clear_console()
                    else:
                        clear_console()
                        restante = arma['Preco'] - variaveis.inventario['Dinheiro']
                        print(f'Dinheiro insuficiente. Faltam {restante} moedas.')
                        time.sleep(2)
                else:
                    clear_console()
                    print('Escolha Inválida.')
                    time.sleep(1.5)

        except ValueError:
            clear_console()
            print('Entrada errada, digite um número inteiro.')
            time.sleep(2)


#Randomizer de inimigo
inimigo = random.choice(variaveis.lista_monstros)

#Atualização de vida
def atualizar_vida():
    variaveis.vida_max = 100
    variaveis.vida_max += 10 * variaveis.nivel + 5 * variaveis.vitalidade
    variaveis.vida_max = variaveis.vida_perso

#Atualização de nível

def atualizar_nivel():
    nivel_atual = variaveis.nivel
    while variaveis.exp_perso > 0 and variaveis.exp_nece <= variaveis.exp_perso:
        variaveis.exp_perso -= variaveis.exp_nece
        variaveis.nivel += 1
        atualizar_vida()
        variaveis.exp_nece += 25
    if nivel_atual != variaveis.nivel:
        print(
            f'Parabéns você subiu de nível\n    -Seu level: {variaveis.nivel}'
        )
        print(f'Nível de experiência atual: {variaveis.exp_perso}\nExperiência necessária para o level {variaveis.nivel + 1}: {variaveis.exp_nece - variaveis.exp_perso}')

#Exibir os status
def exibir_status():
    print(f'Vida do jogador: {variaveis.vida_perso}\nVida do inimigo: {inimigo["Vida"]}')


#Calcular o tipo

def calcular_tipo(dano_base, tipo_arma, tipo_inimigo):
    multiplicador = variaveis.multi.get((tipo_arma, tipo_inimigo), 1.0)
    return dano_base * multiplicador

#Sistema de equipar armas

def equipar_arma():
    if not variaveis.inventario['Armas']:
        print('Você não tem armas para equipar.')
        time.sleep(1.5)
        return
    
    print('Armas no inventário:')
    for i, (arma, dano) in enumerate(variaveis.inventario['Armas'].items(), 1):
        print(f'{i}. {arma} - Dano: {dano}')

    opcao = int(input('Escolha uma arma para equipar:\n '))
    if 1 <= opcao <= len(variaveis.inventario['Armas']):
        arma_selecionada = list(variaveis.inventario['Armas'].keys())[opcao - 1]
        variaveis.inventario['Arma equipada'] = arma_selecionada  # Atualizar a arma equipada
        variaveis.atk_perso = variaveis.inventario['Armas'][arma_selecionada]  # Atualizar o ataque
        clear_console()
        print(f'Você equipou a {arma_selecionada}. Seu ataque agora é {variaveis.atk_perso}')
        time.sleep(2)
        clear_console()
    else:
        clear_console()
        print('Opção Inválida.')
        time.sleep(1.5)

        

#Inventário
def abrir_inventario():
  print('Inventário\n')
  for item, quantia in variaveis.inventario.items():
    if item == 'Armas':
      print('Armas:')
      for arma, dano in quantia.items():
        print(f'  {arma} - Dano: {dano}')
    else:
      print(f'{item}: {quantia}')
  print('')
  print('=' * 10)
  print('')
  print(f'-{variaveis.nick_perso}\n  Dano: {variaveis.atk_perso}\n  Level: {variaveis.nivel}\n  Defesa: {variaveis.defesa}')

  equipar = input('Deseja equipar uma arma? (s/n)\n').lower()
  if equipar in ['s', 'sim']:
    clear_console()
    equipar_arma()

#Sistema de Nickname

def nick():

  variaveis.nick_perso = input('insira o seu nick: ')
  while len(variaveis.nick_perso) < 3:
    clear_console()
    print('O seu nick deve ter pelo menos 3 caracteres.')
    time.sleep(2.5)
    clear_console()
    variaveis.nick_perso = input('Insira o seu nick: ')

#Sistema de Batalha

def dano_perso(inimigo):
    dano = 0
    tipo_arma = variaveis.inventario.get('Arma equipada')

    if tipo_arma:
        arma = next((arma for arma in variaveis.armas if arma["Nome"] == tipo_arma), None)
        if arma:
            dano_base = arma["Dano"] - inimigo.get("Defesa", 0)  
            tipo_inimigo = inimigo.get("Tipo", 'Neutro')  
            dano = calcular_tipo(dano_base, arma["Tipo"], tipo_inimigo)
        else:
            dano = variaveis.atk_perso - inimigo.get("Defesa", 0)

    dano = max(dano, 0)  

    exibir_status()
    time.sleep(1.5)
    escolha = int(input(f'-Você está contra: {inimigo["Nome"]}\n  1.Atacar\n  2.Curar\n'))


    if escolha == 1:
        if dano > 0:
            inimigo["Vida"] -= dano
            print(f'Você atacou e causou {dano:.1f} de dano ao {inimigo["Nome"]}.')
            time.sleep(2)
            clear_console()
        else:
            clear_console()
            print(f'Seu ataque foi ineficaz contra {inimigo["Nome"]}.')
            time.sleep(2)
            clear_console()
    elif escolha == 2:
        if variaveis.vida_perso >= variaveis.vida_max:
            print('Sua vida já está cheia.')
        elif variaveis.inventario['Pocao'] == 0:
            print('Você não tem poções para utilizar.')
        else:
            variaveis.inventario['Pocao'] -= 1
            variaveis.vida_perso += 35
            if variaveis.vida_perso > variaveis.vida_max:
                variaveis.vida_perso = variaveis.vida_max
            print('Você utilizou 1 poção.\n')


def dano_monstro(inimigo):
    global vida_perso
    dano_inimigo = random.randint(inimigo['DanoMin'], inimigo['DanoMax'])

    chance_bloqueio = 0.3
    if random.random() < chance_bloqueio:
        print(f'Você teve sucesso em bloquear o ataque de {inimigo["Nome"]}!')
        return 

    dano = dano_inimigo - variaveis.defesa
    if dano > 0:
        variaveis.vida_perso -= dano
        print(f'O {inimigo["Nome"]} atacou e causou {dano} de dano a você.')
    else:
        print(f'O ataque de {inimigo["Nome"]} foi ineficaz.')

def batalha():
    inimigo = random.choice(variaveis.lista_monstros)  
    inimigo['Vida'] *= variaveis.nivel  

    clear_console()
    print(f'Você está lutando contra: {inimigo["Nome"]}')

    time.sleep(2)
    clear_console()

    while variaveis.vida_perso > 0 and inimigo['Vida'] > 0:
        dano_perso(inimigo)

        if inimigo['Vida'] <= 0:
            print(f'Você derrotou o {inimigo["Nome"]}!')
            variaveis.exp_perso += inimigo['Exp']
            atualizar_nivel()
            variaveis.inventario['Dinheiro'] += 10  
            break

        dano_monstro(inimigo)

        if variaveis.vida_perso <= 0:
            print('Você foi derrotado...')

