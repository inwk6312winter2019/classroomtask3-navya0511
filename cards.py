rank=[1,2,3,4,5,6,7,8,9,10,11,12,13]
suite=["H","S","D","C"]

cards=list(zip(rank,suite))
print(cards)

class card():
    suite_names=['clubs','diamonds','hearts','spades']
    rank_names=[None,'ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    
    def __init__(self,rank=0,suite=2):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return f"the rank is {card.rank_names[self.rank]} and the suite is {card.suite_names[self.suite]}"


ace_of_spades = card(1,3)

print(ace_of_spades)
