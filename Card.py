
class Card:
    def __init__(self, num : int, suit: str):
        self.num = num
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.num} , {self.suit}"
    
    def get_value_of_card(self):
        count = 0
        got_an_ace = False
        if 2 <= self.num <= 10:
            count += self.num
        elif self.num > 10:
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
