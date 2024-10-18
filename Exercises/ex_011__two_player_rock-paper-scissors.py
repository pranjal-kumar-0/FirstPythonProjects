# Make a two-player Rock-Paper-Scissors game.

user1_name = input("Player 1 Name: ")
user2_name = input("Player 2 Name: ")
result = False
while not result:
    print()
    user1_input = input(f'''{user1_name} choose:
Rock (R)
Paper (P)
Scissor (S)
>>> ''').lower()
    print()
    user2_input = input(f'''{user2_name} choose :
Rock (R)
Paper (P)
Scissor (S)
>>> ''').lower()
    if user1_input == user2_input:
        print()
        print("Draw! Go again!")
        print()
    elif (user1_input == 'r' and user2_input == 's') or (user1_input == 'p' and user2_input == 'r') or (user1_input=='s' and user2_input == 'p'):
        print(f'{user1_name} wins! ')
        result = True
    elif (user2_input == 'r' and user1_input == 's') or (user2_input == 'p' and user1_input == 'r') or (user2_input=='s' and user1_input == 'p'):
        print(f'{user2_name} wins! ')
        result = True

