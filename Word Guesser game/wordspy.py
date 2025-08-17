print("WELCOME TO WORD SPY!!!")

number_of_players = int(input("Enter the number of players:"))
players = []

for i in range(number_of_players):
    player_name = input(f"Enter name of player {i+1}:")
    players.append(player_name)
    
