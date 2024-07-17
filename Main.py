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

def turn_handler(players_hands : list, deck : Deck, players_money: int, money_put_in_hand: int):
    curr_hand_index = 0
    split_allowed = True
    while len(players_hands) > curr_hand_index:
        if(find_count(players_hands[curr_hand_index]) > 21):
            curr_hand_index += 1
            continue
        print("make an action")
        print("player has ", find_count(players_hands[curr_hand_index]))
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
            players_hands.append(deck.pop_card())
            print(players_hands[-1])
            print(find_count(players_hands[curr_hand_index]))
            curr_hand_index +=1
        elif action == "ss" and is_split_possible(players_hands[curr_hand_index]) and money_put_in_hand <= players_money:
            players_money -= money_put_in_hand
            players_hands.append([players_hands[curr_hand_index].pop()])
            players_hands[curr_hand_index].append(deck.pop_card())
            players_hands[curr_hand_index + 1].append(deck.pop_card())

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
            players_money = turn_handler(players_hands, deck, players_money, money_put_in_hand)

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


        