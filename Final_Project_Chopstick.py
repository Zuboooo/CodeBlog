#I created this code to play the game "sticks" or "chopsticks. Meant to be played with 2 players.

import time
import random
from datetime import datetime

print("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

start_time = time.time()
print("Timer started.")
def main():
    player1 = [1, 1]  
    player2 = [1, 1]  

    current_player = random.choice([1, 2])

    while True:
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")

        if sum(player1) == 0:
            print("Player 1 is out of the game! Player 2 wins!")
            break
        elif sum(player2) == 0:
            print("Player 2 is out of the game! Player 1 wins!")
            break

        print(f"Player {current_player}'s turn.")

      
        while True:
            try:
                move = input("Enter 'split' or 'attack': ").strip().lower()

                if move not in ['split', 'attack']:
                    raise ValueError("Invalid move. Please enter 'split' or 'attack'.")

                break
            except ValueError as e:
                print(e)

       
        if move == 'split':
            hand_index = int(input("Enter hand index (1 or 2): ")) - 1
            if current_player == 1:
                player1 = split(player1, hand_index)
            else:
                player2 = split(player2, hand_index)
        elif move == 'attack':
            attacking_hand = int(input("Enter attacking hand index (1 or 2): ")) - 1
            defending_hand = int(input("Enter defending hand index (1 or 2): ")) - 1
            if current_player == 1:
                player1, player2 = attack(player1, player2, attacking_hand, defending_hand)
            else:
                player2, player1 = attack(player2, player1, attacking_hand, defending_hand)

        
        current_player = 1 if current_player == 2 else 2

    print("Game over!")
    print("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def split(hand, hand_index):
    other_hand_index = 1 - hand_index
    total_fingers = hand[hand_index]
    hand[hand_index] = total_fingers // 2
    hand[other_hand_index] += total_fingers - hand[hand_index]
    return hand

def attack(attacker, defender, attacking_hand, defending_hand):
    defender[defending_hand] += attacker[attacking_hand]
    if defender[defending_hand] >= 5:
        defender[defending_hand] = 0
    return attacker, defender

if __name__ == "__main__":
    main()


time.sleep(5)  

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Game lasted {elapsed_time:.2f} seconds.")
