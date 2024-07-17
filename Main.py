from Card import Card
from Deck import Deck
class Main:


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
                


    def turn_handler(players_hands, curr_hand_index):
        while(find_count(players_cards[0]) < 21) or splits_finished:
            print("make an action")
            action = input()
            if action == 'h':
                players_cards[0].append(deck.pop_card())
                print(players_cards[-1])
                print(find_count(players_cards[0]))
            elif action == 's':
                print(f"Stayed on {find_count(players_cards)}")
                break
            elif action == "d":
                print("Double")
                players_money -= money_put_in_hand
                money_put_in_hand *= 2
                players_cards.append(deck.pop_card())
                print(players_cards[-1])
                print(find_count(players_cards))
                break
            elif action == "ss" and split_allowed:
                splits_finished = True
    

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
            if(money_put_in_hand < players_money):
                players_money -= money_put_in_hand
                break
            else:
                print("not enough money in stack")
        gameOn = True
        while(gameOn):     
            # player and dealer recieve 2 cards.
            players_cards = []
            dealer_cards = []

            split_allowed = True
            splits_finished = False

            deck = Deck(cards)
            deck.shuffle_cards()
            players_cards.append([deck.pop_card()])
            dealer_cards.append(deck.pop_card())
            players_cards[0].append(deck.pop_card())
            dealer_cards.append(deck.pop_card())

            print("Players Cards :")
            print(players_cards[0][0], "|", players_cards[0][1])
            print(find_count(players_cards[0]))
            print("\n\nDealer face up card:")
            print(dealer_cards[0], "|")
            print(dealer_cards[0].get_value_of_card())

            #players turn






        


            if find_count(players_cards[0]) > 21:
                # player busted
                print("player busted")
            else:
                print("dealer has", dealer_cards[0], "|", dealer_cards[1], "\nCount is", find_count(dealer_cards))
                while(find_count(dealer_cards) < 17):
                    dealer_cards.append(deck.pop_card())
                    print(dealer_cards[-1])
                    print(find_count(dealer_cards))
                if find_count(dealer_cards) > 21 or find_count(dealer_cards) < find_count(players_cards):
                    print("player won")
                    players_money += money_put_in_hand * 2
                elif find_count(dealer_cards[0]) > find_count(players_cards[0]):
                    print("dealer won")
                else:
                    print("push")
                    players_money += money_put_in_hand
            
            print("player has ", players_money)


            gameOn = False


        