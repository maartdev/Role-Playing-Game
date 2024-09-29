#Personagem

nick_perso = ''
inventario = {'Pocao': 0, 'Dinheiro': 0, 'Armas': {}}
vida_max = 100
vida_perso = vida_max
atk_perso = 1
nivel = 1
exp_perso = 0
exp_nece = 25
vitalidade = 1



#Multiplicadores de Dano
    # Luz > Sombra, Sombra > Vento, Vento > Luz

multi = {
    {'Luz', 'Sombra'}: 2,
    {'Sombra', 'Luz'}: 0.5,
    {'Sombra', 'Vento'}: 2,
    {'Vento', 'Sombra'}: 0.5,
    {'Vento', 'Luz'}: 2,
    {'Luz', 'Vento'}: 0.5
}



#Armas
armas = [
    {'Nome': 'Espada de Luz', 'Dano': 15, 'Preco': 35, 'Tipo': 'Luz', 'Descricao': 'Uma espada que brilha como a luz da manhã.'},
    {'Nome': 'Espada de Sombra', 'Dano': 15, 'Preco': 35, 'Tipo': 'Sombra', 'Descricao': 'Uma espada que emana a escuridão da noite.'},
    {'Nome': 'Espada de Vento', 'Dano': 15, 'Preco': 35, 'Tipo': 'Vento', 'Descricao': 'Uma espada afiada como o vento cortante.'},
]



#Inimigos
lista_monstros = [
    {'Nome': 'Inimigo da Luz', 'Tipo': 'Luz', 'Level': 1, 'Vida': 50, 'DanoMin': 15, 'DanoMax': 25, 'Defesa': 5, 'Exp': 25},
    {'Nome': 'Inimigo da Sombra', 'Tipo': 'Sombra', 'Level': 1, 'Vida': 50, 'DanoMin': 15, 'DanoMax': 25, 'Defesa': 5, 'Exp': 25},
    {'Nome': 'Inimigo do Vento', 'Tipo': 'Vento', 'Level': 1, 'Vida': 50, 'DanoMin': 15, 'DanoMax': 25, 'Defesa': 5, 'Exp': 25},
]

