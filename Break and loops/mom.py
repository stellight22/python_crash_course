class Mom:
    def __init__(self, favorite_word):
        self.favorite_word = favorite_word
    
    def say_favorite_word(self):
        print(self.favorite_word)

class m(Mom):
    def __init__(self, favorite_word):
        super().__init__(favorite_word)
        self.favorite_word = favorite_word
    
    def say_it(self):
        print(self.favorite_word)