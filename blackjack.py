import random


# create a func that uses list to return a random card
# 11 is the Ace
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# create a func that takes a list of cards as input and returns the score
def calculate_score(cards):
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
    # the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an 11 (ace). if the score is already over 21, remove the 11 and replace it
    # with a 1. 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# create a func that pass in the user and computer scores. If the computer and user both
# have same score, then it is draw. if the computer has blackjack, then user loses. if
# the user has blackjack, then user wins. if the user score is over 21, then user loses.
# if computer score is over 21, then computer loses. if none of the above, then player
# with the highest score wins 
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, the opponent has Blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    # deal the user and computer 2 cards each
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # call calculate_score() and if the computer or user has blackjack (0) or if the 
        # user's score is over 21, then the game ends!
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card()) 
            else:
                is_game_over = True

    # once user is done, it is time to let the computer play. The computer should keep
    # drawing cards as long as it has a score less than 17
    while computer_score <= 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()



