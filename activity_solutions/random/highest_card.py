import random
numbers = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split()
suits = "Diamonds Hearts Clubs Spades".split()
deck = ["Red Joker", "Black Joker"]

for n in numbers:
  for suit in suits:
    deck.append(n + " of "+ suit)
random.shuffle(deck)
print(deck)
while True:
  temp = input("Hit enter to get a card. Input anything to exit.")
  if temp != "":
    break
  print(deck.pop())