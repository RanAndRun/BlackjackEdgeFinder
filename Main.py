from Card import Card
from Deck import Deck

def find_count(cards_list : list[Card]):
    count = 0
    got_an_ace = False
    for card in cards_list:
        if 2 <= card.num <= 10:
            count += card.num
        elif card.num > 10:
            count += 10
        else:
            # ace
            if count <= 10:
                got_an_ace = True
                count += 11
            else:
                count += 1
        if got_an_ace and count > 21:
            count -= 10
            got_an_ace = False
    
    return count

def is_split_possible(hand : list):
    return len(hand) == 2 and hand[0].num == hand[1].num

def is_double_possible(hand : list):
    return len(hand) == 2

def getMove(players_hand : list, dealer_face_card: int ):
    blackjack_strategy_hard = [
        # Dealer's upcard: 2   3   4   5   6   7   8   9  10  A
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 5-7
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 8
        ['H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 9
        ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],  # Player's total: 10
        ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H'],  # Player's total: 11
        ['H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 12
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 13
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 14
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 15
        ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 16
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']   # Player's total: 17
    ]


    blackjack_strategy_soft = [
    # Dealer's upcard: 2   3   4   5   6   7   8   9  10   A
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,2
    ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,3
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,4
    ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,5
    ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,6
    ['H', 'DS', 'DS', 'DS', 'DS', 'S', 'H', 'H', 'S', 'S'],  # Player's total: A,7
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Player's total: A,8
    ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']   # Player's total: A,9
]   
    blackjack_strategy_splitable = [
        # Dealer's upcard: 2   3   4   5   6   7   8   9  10  A
        ['H', 'H', 'SP', 'SP', 'SP', 'SP', 'H', 'H', 'H', 'H'],  # Player's total: 2,2
        ['H', 'H', 'SP', 'SP', 'SP', 'SP', 'H', 'H', 'H', 'H'],  # Player's total: 3,3
        ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 4,4
        ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],  # Player's total: 5,5
        ['SP', 'SP', 'SP', 'SP', 'SP', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 6,6 
        ['SP', 'SP', 'SP', 'SP', 'SP', 'H', 'H', 'H', 'H', 'H'],  # Player's total: 7,7 
        ['SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP'],  # Player's total: 8,8
        ['SP', 'SP', 'SP', 'SP', 'SP', 'S', 'SP', 'SP', 'S', 'S'],   # Player's total: 9,9
        ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],   # Player's total: T,T
        ['SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP']   # Player's total: A,A
    ]


    if len(players_hand) == 2:
        # initial hand
        card1 = players_hand[0]
        card2 = players_hand[1]
        value = find_count(players_hand)

        if(card1.num == 1 or card2.num == 1):
            #soft
            return blackjack_strategy_soft[value - 11][dealer_face_card.get_value_of_card() - 1]
        if(card1.num == card2.num):
            #splitable
            print("aaaaaaa", card1.num - 1, dealer_face_card.get_value_of_card() - 1)
            return blackjack_strategy_splitable[(card1.get_value_of_card()) - 2][dealer_face_card.get_value_of_card() - 1]
        else:
            if(value >= 17): return 'S'
            if(value <= 7): return 'H'
            print("ggggg", value - 7, dealer_face_card.get_value_of_card() - 1)
            return blackjack_strategy_hard[value - 7][dealer_face_card.get_value_of_card() - 1]

def turn_handler(players_hands : list, deck : Deck, players_money: int, money_put_in_hand: int, dealers_face_card):
    curr_hand_index = 0
    split_allowed = True
    while len(players_hands) > curr_hand_index:
        if(find_count(players_hands[curr_hand_index]) > 21):
            curr_hand_index += 1
            continue
        print("make an action")
        print("best move is", getMove(players_hands[curr_hand_index], dealers_face_card))
        action = input()
        if action == 'h':
            split_allowed = False
            players_hands[curr_hand_index].append(deck.pop_card())
            print(players_hands[curr_hand_index][-1])
            print(find_count(players_hands[curr_hand_index]))
        elif action == 's':
            print(f"Stayed on {find_count(players_hands[curr_hand_index])}")
            curr_hand_index +=1
        elif action == "d" and is_double_possible(players_hands[curr_hand_index]):
            print("Double")
            players_money -= money_put_in_hand
            money_put_in_hand *= 2
            players_hands[curr_hand_index].append(deck.pop_card())
            print(players_hands[-1])
            print(find_count(players_hands[curr_hand_index]))
            curr_hand_index +=1
        elif action == "ss" and is_split_possible(players_hands[curr_hand_index]) and money_put_in_hand <= players_money:
            players_money -= money_put_in_hand
            players_hands.append([players_hands[curr_hand_index].pop()])
            players_hands[curr_hand_index].append(deck.pop_card())
            players_hands[-1].append(deck.pop_card())

            print(players_hands)

    return players_money


class Main:
    cards = []
    for i in range(1, 14):
        for j in range(4):
            suit = ""
            if j == 0:
                suit = "heart"
            elif j == 1:
                suit = "diamond"
            elif j == 2:
                suit = "spade"
            elif j == 3:
                suit = "club"
            temp = Card(i, suit)
            cards.append(temp)


    players_money = 1000
    gameOn = True
    while True:
        while True:
            print("player has ", players_money)
            money_put_in_hand = int(input("how much money on hand"))
            if(money_put_in_hand <= players_money):
                players_money -= money_put_in_hand
                break
            else:
                print("not enough money in stack")
        gameOn = True
        while(gameOn):     
            # player and dealer recieve 2 cards.
            players_hands = []
            dealer_cards = []

            split_allowed = True
            splits_finished = False

            deck = Deck(cards)
            deck.shuffle_cards()
            players_hands.append([deck.pop_card()])
            dealer_cards.append(deck.pop_card())
            players_hands[0].append(deck.pop_card())
            dealer_cards.append(deck.pop_card())

            print("Players Cards :")
            print(players_hands[0][0], "|", players_hands[0][1])
            print(find_count(players_hands[0]))
            print("\n\nDealer face up card:")
            print(dealer_cards[0], "|")
            print(dealer_cards[0].get_value_of_card())

            #players turn
            players_money = turn_handler(players_hands, deck, players_money, money_put_in_hand, dealer_cards[0])

            for hand in players_hands:
                if find_count(hand) > 21:
                    # player busted
                    print("player busted")
                else:
                    print("dealer has", dealer_cards[0], "|", dealer_cards[1], "\nCount is", find_count(dealer_cards))
                    while(find_count(dealer_cards) < 17):
                        dealer_cards.append(deck.pop_card())
                        print(dealer_cards[-1])
                        print(find_count(dealer_cards))
                    if find_count(dealer_cards) > 21 or find_count(dealer_cards) < find_count(hand):
                        print("player won")
                        players_money += money_put_in_hand * 2
                    elif find_count(dealer_cards) > find_count(hand):
                        print("dealer won")
                    else:
                        print("push")
                        players_money += money_put_in_hand
                
                print("player has ", players_money)


                gameOn = False


        