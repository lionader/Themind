def initialize ():
    player1 = [10,30]
    player2 = [20,90]
    player3 = [32,15]
    player4 = [45,99]

    game = [player1,player2,player3,player4]
    return game

def selectcard (game):
    card = int(input('who will play ?1,2,3,4: '))
    if card == 1:
        print('which card to play from 0 ',len(game[0])-1,game[0])
        sel = int(input('select card: '))
        gamecard = game[0][sel]
    if card == 2:
        print('which card to play from 0 ', len(game[1]) - 1, game[1])
        sel = int(input('select card: '))
        gamecard = game[1][sel]
    if card == 3:
        print('which card to play from 0 ', len(game[2]) - 1, game[2])
        sel = int(input('select card: '))
        gamecard = game[2][sel]
    if card == 4:
        print('which card to play from 0 ', len(game[3]) - 1, game[3])
        sel = int(input('select card: '))
        gamecard = game[3][sel]
    return (gamecard)

def check (card,game):
    looselife = 0
    for i in range(len(game)):
        for j in range(len(game[i])):
            print(i, j, game, card)
            if card >= game[i][j]:
                game[i][j] = 0
                print(game[0][0])
                print(card, 'i', i, 'j', j, game)
                looselife +=1
    print(game)
    return (looselife,game)

def main():
    life = 4
    game = initialize()
    card = selectcard(game)
    print('game1',game)

    while life >= 0 :
        game,looselife = check(card, game)
        card = selectcard(game)
        print('game', game, 'life:', life)
        if looselife >0:
            life -=1
            print('life',life)
if __name__ == "__main__":
    main()




