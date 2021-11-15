import random

def generatecards() :

#preare the random deck from 1-100
    cards = list(range(1,101))
    random.shuffle(cards)
    return cards

def drawlevel1 ():
    cards = generatecards()
    # level 1 : each player gets a card
    dplayer1,player2,player3,player4 = cards[random.randint(0, 100)]
    print(cards, player1, player2, player3,player4)
    print(len(cards))

    return player1,player2,player3,player4

def checkmind():
    gamecards = list(drawlevel1())
    winner = sorted(gamecards)
    print(gamecards, winner)


def playlevel1():



def main():
    playlevel1()

if __name__ == "__main__":
    main()


