import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_cards(cardsList):
    if cardsList == []:
        no_of_cards = 2
    else:
        no_of_cards = 1
    while no_of_cards != 0:
        cardsList.append(random.choice(cards))
        no_of_cards -= 1


def get_total(cardsList):
    total = 0
    for card in cardsList:
        total += card
    return total


def restart():
    response = input("Do you want to play again? Type 'y' or 'n': ")
    if response.lower() == "y":
        blackjack()


def drawCard(myCards, myTotal, dealerCards, dealerTotal, response):
    if response.lower() == "y":
        get_cards(myCards)
        if dealerTotal < 17:
            get_cards(dealerCards)
        myTotal = get_total(myCards)
        if myTotal > 21:
            if 11 in myCards:
                index = myCards.index(11)
                myCards[index] = 1
                myTotal = get_total(myCards)
        dealerTotal = get_total(dealerCards)
        if dealerTotal > 21:
            if 11 in dealerCards:
                index = dealerCards.index(11)
                dealerCards[index] = 1
                dealerTotal = get_total(dealerCards)
        if myTotal == 21 and dealerTotal != 21:
            print("You got 21! You Win!!")
            finalHand(myCards, myTotal, dealerCards, dealerTotal)
        elif dealerTotal == 21:
            print("Dealer got 21. You lose.")
            finalHand(myCards, myTotal, dealerCards, dealerTotal)
        elif myTotal > 21:
            print("You went over 21. You lose")
            finalHand(myCards, myTotal, dealerCards, dealerTotal)
        else:
            print(f"Your cards {myCards}, current score: {myTotal}")
            print(f"Computer's first card: {dealerCards[0]}")
            response = input("Type 'y' to get another card, type 'n' to pass: ")
            if response.lower() == "y":
                drawCard(myCards, myTotal, dealerCards, dealerTotal, response)
            else:
                endGame(myCards, myTotal, dealerCards, dealerTotal)
    else:
        endGame(myCards, myTotal, dealerCards, dealerTotal)


def endGame(myCards, myTotal, dealerCards, dealerTotal):
    while dealerTotal < 17:
        get_cards(dealerCards)
        dealerTotal = get_total(dealerCards)
    if dealerTotal > 21:
        print("You win!.")
        finalHand(myCards, myTotal, dealerCards, dealerTotal)
    elif myTotal == dealerTotal:
        print("It's a draw.")
        finalHand(myCards, myTotal, dealerCards, dealerTotal)
    elif myTotal > 21 and dealerTotal > 21:
        print("It's a draw. You both went over 21.")
        finalHand(myCards, myTotal, dealerCards, dealerTotal)
    elif myTotal < dealerTotal:
        print("You lose.")
        finalHand(myCards, myTotal, dealerCards, dealerTotal)
    else:
        print("You win!")
        finalHand(myCards, myTotal, dealerCards, dealerTotal)


def finalHand(myCards, myTotal, dealerCards, dealerTotal):
    print(f"Your final hand: {myCards}, final score: {myTotal}")
    print(f"Computer's final hand: {dealerCards}, final score {dealerTotal}")
    restart()
    gameContinue = False


def blackjack():
    gameContinue = True
    while gameContinue:
        myCards = []
        dealerCards = []
        get_cards(myCards)
        get_cards(dealerCards)

        myTotal = get_total(myCards)
        dealerTotal = get_total(dealerCards)
        if myTotal == 21 and dealerTotal == 21:
            print("It's a draw.")
            finalHand(myCards, myTotal, dealerCards, dealerTotal)
        if myTotal == 21:
            print("You win!")
            finalHand(myCards, myTotal, dealerCards, dealerTotal)

        print(f"Your cards {myCards}, current score: {myTotal}")
        print(f"Computer's first card: {dealerCards[0]}")
        response = input("Type 'y' to get another card, type 'n' to pass: ")

        drawCard(myCards, myTotal, dealerCards, dealerTotal, response)
        gameContinue = False


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    blackjack()
