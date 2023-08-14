import random
# score history
# high score
# how many games have been played


class Game:
    '''We can keep all data and behavior related to a game together.
    A class is like a blueprint or pattern'''

    def __init__(self):
        # this gets called when we create a new instance of the class
        self.name = "Mystery Word"
        self.guesses_remaining = 8
        self.right_guesses = []
        self.wrong_guesses = []
        self.playing = True
        self.word = None
        # attributes
        # number of guesses left
        # right guesses
        # wrong guesses/guesses remaining
        # letters guessed

    def __str__(self):
        # we can override the built-in string method to make something
        # more readable to humans
        # built-in methods with dunders are known as 'magic methods'
        return self.name

    # behaviors - we will create our own methods
    # starting the game
    def start(self):
        print(f'Welcome to {self.name}')

    # choosing a word to guess
    def choose_word(self, file):
        # self is always the first argument for instance methods in a class
        with open(file) as f:
            word_list = f.read().strip().split()
        selected_word = random.choice(word_list)
        self.word = selected_word
    # action of player taking a guess
    # way to display word with empty spaces, right guesses to player
    # display intro instructions
    # display letters guessed
    # determine when game is won or lost & tell player


new_game = Game()
# writing the name of the class with () causes the __init__() method
# to be called and a new instance of game to be created
# using the blueprint provided in the class
# we can then call methods on that instance
new_game.start()
# don't have to pass self, that'w written in to the class structure
new_game.choose_word('words.txt')
print(f'The selected word is: {new_game.word}')
# __dict__ shows all the attributes of your instance in a dictionary format
print(new_game.__dict__)
