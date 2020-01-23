#war.py
import random
value = ["two","three","four","five","six","seven","eight","nine","ten","Jack","Queen","King","Ace"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
playing = True
wins = losses = hands = ties = 0
while playing and hands < 26:
    pCard = [value[random.randint(0,12)], suits[random.randint(0,3)]]
    print("Your card is the", pCard[0], "of", pCard[1])
    oCard = [value[random.randint(0,12)], suits[random.randint(0,3)]]
    while oCard == pCard:
        oCard = [value[random.randint(0,12)], suits[random.randint(0,3)]]
    print("The opponent's card is the", oCard[0], "of", oCard[1])
    if value.index(pCard[0]) > value.index(oCard[0]):
        print("You win!")
        wins += 1
    elif value.index(pCard[0]) == value.index(oCard[0]):
        print("It's a tie...")
        ties += 1
    else:
        print("You lose...")
        losses += 1
    hands += 1

    print("Current score is:", wins, "wins, to", losses, "losses, and", ties," ties")
    playing = (input("Press enter to keep playing or enter anything else to stop \n") == "")
