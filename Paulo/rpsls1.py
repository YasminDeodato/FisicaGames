import random


def name_to_number(player_choice):
    if player_choice == 'pedra':
        player_number = 0

    elif player_choice == 'spock':
        player_number = 1

    elif player_choice == 'papel':
        player_number = 2

    elif player_choice == 'lagarto':
        player_number = 3

    elif player_choice == 'tesoura':
        player_number = 4

    else:
        print('Valor inválido')

    return player_number


def number_to_name(comp_number):
    if comp_number == 0:
        comp_choice = "Pedra"
    else:
        if comp_number == 1:
            comp_choice = "Spock"
        else:
            if comp_number == 2:
                comp_choice = "Papel"
            else:
                if comp_number == 3:
                    comp_choice = "Lagarto"
                else:
                    if comp_number == 4:
                        comp_choice = "Tesoura"

    return comp_choice


def rpsls(player_choice):
    print()
    print('Jogador escolhe {}'.format(player_choice))

    player_number = name_to_number(player_choice)

    comp_number = int(random.randrange(0, 5))

    comp_choice = number_to_name(comp_number)
    print('Computador escolhe {}'.format(comp_choice))

    result = player_number - comp_number

    if result == 0:
        print('Empate!')

    else:
        if player_number == 0:
            if result == -4 or result == -3:
                print('Jogador Vence!')
            else:
                print('Computador Vence!')

        if player_number == 1:
            if result == 1 or result == -3:
                print('Jogador Vence!')
            else:
                print('Computador Vence!')

        if player_number == 2 or player_number == 3 or player_number == 4:
            if result == 1 or result == 2:
                print('Jogador Vence!')
            else:
                print('Computador Vence!')
    pass


# --- Codigo Principal ---
# Testes feitos - 5 Chamadas:

rpsls("pedra")
rpsls("spock")
rpsls("papel")
rpsls("lagarto")
rpsls("tesoura")
