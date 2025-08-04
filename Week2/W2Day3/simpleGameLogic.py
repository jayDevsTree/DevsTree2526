def game():
    print("1: Stone  2: Paper  3: Scissor")
    u1 = int(input("User 1: "))
    u2 = int(input("User 2: "))
    
    result = u1 - u2
    
    # simple --> player1 - player 2 == 1 or -2 --> player 1 wins
    #           player2 - player 1 == 1 or 2 --> player 2 wins
    
    # complicated --> (player 1 - player 2) %3 ==1 this have -2% 3 ==1 true and 1== 1 for player 1
    #                                                   and -1% 3 == 2 true and 2 == 1 for player 2
    
    if result == 0:
        print("Tie")
    elif result in [1, -2]:
        print("User 1 Wins")
    else:
        print("User 2 Wins ")

game()
