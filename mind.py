import random


def generatecards() :

#preare the random deck from 1-100
    cards = list(range(1,101))
    random.shuffle(cards)
    return cards

def drawlevel1 ():
    cards = generatecards()

    # level 1 : each player gets a card

    player1 = cards[random.randint(0, 100)]
    cards.remove(player1)

    player2 = cards[random.randint(0, 99)]
    cards.remove(player2)

    player3 = cards[random.randint(0, 98)]
    cards.remove(player3)

    player4 = cards[random.randint(0, 97)]
    cards.remove(player4)
    print(cards, player1, player2, player3,player4)
    print(len(cards))

    return player1,player2,player3,player4

def playlevel1 ():

    gamecards= list(drawlevel1())
    winner = sorted(gamecards)
    print(gamecards , winner)

    currentplayer1 = int(input('who plays ?(1,2,3,4):'))
    if currentplayer1 == 1:
        if gamecards[0] == winner [0]:
            gamestate = 'a1a'
            gamecards.remove(gamecards[0])
            winner.remove(gamecards[0])
            print(gamecards,winner,gamestate)
            currentplayer2 = int(input('who plays 2,3,4:'))
            if currentplayer2 == 2:
                if gamecards [0] == winner [0]:
                    gamestate = 'a1a'
                    gamecards.remove(gamecards[0])
                    winner.remove(gamecards[0])
                    print(gamecards, winner,gamestate)
                    currentplayer3 = int(input('who plays 3,4:'))
                    if currentplayer3 == 3:
                        if gamecards[0] == winner[0]:
                            gamestate = 'a1a'
                            gamecards.remove(gamecards[0])
                            winner.remove(gamecards[0])
                            print(gamecards, winner,gamestate,'level 1 complete')

        if gamecards[0] > winner [0] & gamecards [0] == winner[1] & gamecards[0] < winner[2]  & gamecards[0] < winner[3]:
            gamestate = 'a1b'
            gamecards.remove(gamecards[0]), gamecards.remove(gamecards[1])
            winner.remove(gamecards[0]), winner.remove(gamecards[1])
            print(gamecards, winner, gamestate)
            currentplayer1 = int(input('who plays 3,4:'))



        if gamecards[0] > winner [0] & gamecards [0] > winner[1] & gamecards[0] == winner[2] & gamecards[0] < winner[3]:
            gamestate = 'a1c'
            gamecards.remove(gamecards[0]), gamecards.remove(gamecards[1]), gamecards.remove(gamecards[2])
            winner.remove(gamecards[0]), winner.remove(gamecards[1]), gamecards.remove(gamecards[2])
            print(gamecards, winner, gamestate, 'you lost a life but pass the level')

        if gamecards[0] > winner [0] & gamecards[0] > winner[1] & gamecards [0] > winner[2] & gamecards[0] == winner[3]:
            gamestate = 'a1d'
            gamecards.remove(gamecards[1]) , gamecards.remove(gamecards[2]),gamecards.remove(gamecards[3])
            winner.remove(gamecards[0]) , winner.remove(gamecards[1]),gamecards.remove(gamecards[2])
            print(gamecards,winner,gamestate,'you lost a life but pass the level')


def main():
    playlevel1()

if __name__ == "__main__":
    main()


