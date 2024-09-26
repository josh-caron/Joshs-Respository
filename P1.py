# Blackjack
from p1_random import P1Random
rng = P1Random()  # create a P1Random variable

game_number = 1
print(f"START GAME #{game_number}", end="\n\n")

option = 1
hand = 0
player_wins = 0
dealer_wins = 0
tie_games = 0
while option != 4:
    if option == 1:
        card = rng.next_int(13) + 1
        value = card
        if card == 1:
            dealt_card = 'ACE'
        elif card == 2:
            dealt_card = '2'
        elif card == 3:
            dealt_card = '3'
        elif card == 4:
            dealt_card = '4'
        elif card == 5:
            dealt_card = '5'
        elif card == 6:
            dealt_card = '6'
        elif card == 7:
            dealt_card = '7'
        elif card == 8:
            dealt_card = '8'
        elif card == 9:
            dealt_card = '9'
        elif card == 10:
            dealt_card = '10'
        elif card == 11:
            dealt_card = 'JACK'
            value = 10
        elif card == 12:
            dealt_card = 'QUEEN'
            value = 10
        elif card == 13:
            dealt_card = 'KING'
            value = 10
        print(f"Your card is a {dealt_card}!")
        hand += value
        print(f"Your hand is: {hand}", end="\n\n")
        if hand == 21:
            print("BLACKJACK! You win!", end="\n\n")
            game_number += 1
            player_wins += 1
            print(f"START GAME #{game_number}", end="\n\n")
            hand = 0
            continue
        elif hand > 21:
            print("You exceeded 21! You lose.", end="\n\n")
            game_number += 1
            dealer_wins += 1
            print(f"START GAME #{game_number}", end="\n\n")
            hand = 0
            continue
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit", end="\n\n")
        option = int(input("Choose an option: "))
        while option not in [1, 2, 3, 4]:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.", end = "\n\n")
            print("1. Get another card")
            print("2. Hold hand")
            print("3. Print statistics")
            print("4. Exit", end="\n\n")
            option = int(input("Choose an option: "))

    elif option == 2:
        dealers_hand = rng.next_int(11) + 16
        print(f"Dealer's hand: {dealers_hand}")
        print(f"Your hand is: {hand}", end="\n\n")
        if hand == dealers_hand:
            print("It's a tie! No one wins!", end="\n\n")
            tie_games += 1
        elif hand > dealers_hand or dealers_hand > 21:
            print("You win!", end = "\n\n")
            player_wins += 1
        elif hand < dealers_hand:
            print("Dealer wins!", end = "\n\n")
            dealer_wins += 1
        game_number += 1
        print(f"START GAME #{game_number}", end="\n\n")
        option = 1
        hand = 0
        continue

    elif option == 3:
        print(f"Number of Player wins: {player_wins}")
        print(f"Number of Dealer wins: {dealer_wins}")
        print(f"Number of tie games: {tie_games}")
        print(f"Total # of games played is: {game_number-1}")
        percent_player_wins = (player_wins / (game_number-1)) * 100
        print(f"Percentage of Player wins: {percent_player_wins:.1f}%", end = "\n\n")
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit", end="\n\n")
        option = int(input("Choose an option: "))
        while option not in [1,2,3,4]     :
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.", end = "\n\n")
            print("1. Get another card")
            print("2. Hold hand")
            print("3. Print statistics")
            print("4. Exit", end="\n\n")
            option = int(input("Choose an option: "))