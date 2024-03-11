import random

def dice_roll():
    score1 = 0
    score2 = 0
    round = 0
    
    while score1 < 100 and score2 < 100:
        round=round+1
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        
        # print("Player 1 choice:", player1)
        # print("Player 2 choice:", player2)
        
        score1 += player1
        score2 += player2
        
    print("Player 1 total score:", score1)
    print("Player 2 total score:", score2)
    print()
    
    if score1 > score2:
        print("Player 1 wins in", round, "rounds!")
    elif score2 > score1:
        print("Player 2 wins in", round, "rounds!")
    else:
        print("It's a tie!")

dice_roll()
