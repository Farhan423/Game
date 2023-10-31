while True:
    # Get player choices
    player1 = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
    player2 = input("Player 2, enter your choice (rock, paper, scissors): ").lower()

                                                    
    valid_choices = ['rock', 'paper', 'scissors']  # Check if player2's choice is valid, if not, player2 wins
    if player2 not in valid_choices:
        print("Player 2 wins! (Invalid input from Player 2)")
    else:
        if player1 == player2:
            print("It's a tie!")
        elif (player1 == 'rock' and player2 == 'scissors') or \
             (player1 == 'scissors' and player2 == 'paper') or \
             (player1 == 'paper' and player2 == 'rock'):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
