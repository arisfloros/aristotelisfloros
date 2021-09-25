import random

player_win = 0
pc_win = 0 

options = ["rock", "paper", "scissors"]


times_to_play = 0

min_amount_of_times_to_play = 0
times_to_play_input = int(input("Choose how many times you want to play (number must be 1 or more): "))

if times_to_play_input >= min_amount_of_times_to_play:
        print(f"You will now play: {times_to_play_input} amount of times.")
    
        for i in range(min_amount_of_times_to_play, times_to_play_input) : 
            player_input = input(f"Select: Rock / Paper / Scissors or Q to quite the game: ").lower()

            random_number = random.randrange(0,3)
            pc_input = options[random_number]

            
            if player_input not in options:
                print("You didn't choose one of the options. Please try again.")
            elif player_input == "q":
                print("You quit the game. Bye, Bye!")
                quit()
            elif player_input == "rock" and pc_input == "scissors":
                print(f"Pc choose --{pc_input}-- and You choose --{player_input}--")
                print("You win the round!")
                player_win += 1 
            elif player_input == "paper" and pc_input == "rock":
                print(f"Pc choose --{pc_input}-- and You choose --{player_input}--")
                print("You win the round!")
                player_win += 1 
            elif player_input == "scissors" and pc_input == "paper":
                print(f"Pc choose --{pc_input}-- and You choose --{player_input}--")
                print("You win the round!")
                player_win += 1 
            else:
                print(f"Pc choose --{pc_input}-- and You choose --{player_input}--")
                print("Pc wins the round. Hehe")
                pc_win += 1
        if player_win > pc_win:
            print("You won the game! Congrats!")
        elif pc_win > player_win:
            print("Pc won the game! Better luck next time!")
        else:
            print("IT'S A TIE!")

        print(f"Player won {player_win} times!")
        print(f"Pc won {pc_win} times!")
        
else:
    print("You typed something wrong. See you next time.")


