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
    # create an empty list for the user cards
    user_cards = []
    # if the first two cards sum to over 21, we randomize again
    while card1 + card2 > 21:
        card1 = random.choice(cards)
        card2 = random.choice(cards)
    # append the randomized cards to list
    user_cards.append(card1)
    user_cards.append(card2)

    #randomize computer two cards
    card3, card4 = random.choice(cards), random.choice(cards)
    #create an empty list for computer cards
    computer_cards = []
    # if the first two cards sum to over 21, we randomize again
    while card3 + card4 > 21:
        card3 = random.choice(cards)
        card4 = random.choice(cards)
    # append the randomized cards to list
    computer_cards.append(card3)
    computer_cards.append(card4)

    # show user their cards
    print(f"Your cards: {user_cards}")

    # show computer's first card of two cards
    print(f"Computer's first card: {computer_cards}")

    







