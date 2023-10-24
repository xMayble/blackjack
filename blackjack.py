import random

# card values we are dealing with
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ask user if they want to play
intro = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# if the user wants to play, we show interface and give them a set of 2 cards!
if intro == 'y':
    # -insert blackjack logo here-

    # randomize first two cards
    card1, card2 = random.choice(cards), random.choice(cards)
    # if the first two cards sum to over 21, we randomize again
    while card1 + card2 > 21:
        card1 = random.choice(cards)
        card2 = random.choice(cards)
    # create an empty list for the cards
    user_cards = []
    # append the randomized cards to list
    user_cards.append(card1)
    user_cards.append(card2)
    # show user their new set of cards
    print(f"Your cards are: {user_cards}")



