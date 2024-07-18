from Main import find_count
class Ai:
    def getMove(players_hand : list, dealer_face_card: int ):
        blackjack_strategy_hard = [
            # Dealer's upcard: 2   3   4   5   6   7   8   9  10   A
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
            ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,2 13
            ['H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,3 14
            ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,4 15
            ['H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,5 16
            ['H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],  # Player's total: A,6 17 
            ['H', 'DS', 'DS', 'DS', 'DS', 'S', 'H', 'H', 'S', 'S'],  # Player's total: A,7 18 
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],  # Player's total: A,8 19 
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']   # Player's total: A,9 20
        ]

        if len(players_hand) == 2:
            # initial hand
            card1 = players_hand[0]
            card2 = players_hand[1]
            value = find_count(players_hand)

            if(card1.num == 1 or card2.num == 1):
                #soft
                return blackjack_strategy_soft[value - 13][dealer_face_card - 1]
            if(card1.num == card2.num):
                #splitable
                pass
            else:
                if(value > 17): return 'S'
                if(value < 7): return 'H'
                return blackjack_strategy_hard[value - 7][dealer_face_card - 1]