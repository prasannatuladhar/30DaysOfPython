"""

1) Write a generator that generates prime numbers in a specified range. You can make use of your solution to exercise 3 from day 8 as a starting point.

2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = map(lambda name: name.strip().title(), names)
3) Write a small program to deal cards for a game of Texas Hold'em. The order of the deal is as follows:

The deck is shuffled.
One card is handed to each player in order.
A second card is handed to each player order.
Then comes the more complicated part of the deal.

First, the top card of the deck is discarded. This is called the burn.
Three cards are then placed in the centre of the table, which is called the flop.
Another card is burned, meaning we discard another card from the top of the deck.
We add another card to the centre, which is called the turn.
We burn another card.
Finally, there's the river, where a fifth and final card is added to the centre.
The desired output for the program is something like this:

How many players are there? 2

Player 1 was dealt: (4, hearts), (4, clubs)
Player 2 was dealt: (9, clubs), (jack, diamonds)

The flop: (jack, clubs), (4, diamonds), (king, spades)
The turn: (8, hearts)
The river: (ace, hearts)
"""

# 1 Solutions
def prime_num_finder(limit):
    for num in range(2,limit+1):
        for divisor in range(2,num):
            if num % divisor == 0:
                break    
        else:
            yield num

p = prime_num_finder(10)
print(next(p))
print(next(p))

# 2 Solutions
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)
result = (name.strip().title() for name in names)
print(next(result))
print(next(result))

# 3 Solutions
import itertools
import random


def deal(cards, number_of_players):
	deck = shuffle_deck(cards)

	deal_to_players(deck, number_of_players)
	deal_to_table(deck)


def deal_to_players(deck, number_of_players):
	first_cards = [next(deck)  for _ in  range(number_of_players)]
	second_cards = [next(deck)  for _ in  range(number_of_players)]
	
	hands = zip(first_cards, second_cards)

	print()

	for i,  (first_card, second_card)  in  enumerate(hands, start=1):
		print(f"Player {i} was dealt: {first_card}, {second_card}")

	print()


def deal_to_table(deck):
	next(deck)  # burn
	flop = ', '.join(str(next(deck))  for _ in  range(3))
	print(f"The flop: {flop}")

	next(deck)  # burn
	print(f"The turn: {next(deck)}")

	next(deck)  # burn
	print(f"The river: {next(deck)}")
	print()


def get_players():
	while True:
		number_of_players = input("How many players are there? ").strip()
	
		try:
			number_of_players = int(number_of_players)
		except ValueError:
			print("You must enter an integer.")
		else:
			if number_of_players in range(2, 11):
				return number_of_players
			elif number_of_players < 2:
				print("You must have at least 2 players.")
			else:
				print("You can have a maximum of 10 players.")


def shuffle_deck(cards):
	deck = list(cards)
	random.shuffle(deck)

	return iter(deck)


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = list(itertools.product(ranks, suits))

deal(cards, get_players())





