import random

wins = int(input('Cuantas rondas gana el ganador?'))

def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera ---').lower()

  if user_option not in options:
    print('Dale pa, elegi bien')
    # continue
    return None, None

  computer_option = random.choice(options)  #Elije random dentro de la tupla/lista

  print('User option ==', user_option)
  print('Pc option ==', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, pc_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
      if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('Ganaste User')
        user_wins += 1
      else:
        print('Papel gana a piedra')
        print('Gano la PC')
        pc_wins += 1
  elif user_option == 'papel':
      if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('Ganaste User')
        user_wins += 1
      else:
        print('Tijera gana a papel')
        print('Gano la PC')
        pc_wins += 1
  elif user_option == 'tijera':
      if computer_option == 'papel':
        print('Tijera gana a papel')
        print('Ganaste User')
        user_wins += 1
      else:
        print('Piedra gana a tijera')
        print('Gano la PC')
        pc_wins += 1
  return user_wins, pc_wins

def check_winner(user_wins, pc_wins, wins):

  if user_wins == wins:
      print('🎖️ El ganador es User 🎖️')
      exit()

  if pc_wins == wins:
      print('🎖️ El ganador es Computer 🎖️')
      exit()


def run_game():
  user_wins = 0
  pc_wins = 0
  rounds= 1
  
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
  
    print('User wins: ', user_wins)
    print('Pc wins: ', pc_wins)
    rounds += 1
    
    user_option, computer_option = choose_options()
    user_wins, pc_wins =check_rules(user_option, computer_option, user_wins, pc_wins)
    check_winner(user_wins, pc_wins, wins)
run_game()