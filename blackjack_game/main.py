from art import logo
import random
import os

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card
players_deck = [deal(),deal()]
computers_deck = [deal(),deal()]

def check_burst(whom):
    if sum(whom) > 21 and 11 not in whom:
            return True
    elif 11 in whom:
        if whom == players_deck:
            players_deck.remove(11)
            players_deck.append(1)
        elif whom == computers_deck:
            computers_deck.remove(11)
            computers_deck.append(1)       
    return False

def natural():
    if sum(players_deck) == 21 and sum(computers_deck) == 21:
        print_result()
        print("It's a push. you win")
    elif sum(players_deck) == 21:
        print_result()
        print("You hit a blackjack!. You won")


def print_result():
    print(f"Your final hand: {players_deck}, final score: {sum(players_deck)}")
    print(f"Computer's final hand: {computers_deck}, final score: {sum(computers_deck)}")
    natural()

def check_results():
    print_result()
    if sum(players_deck) > sum(computers_deck) :
        print("You win!")
    elif sum(players_deck) == sum(computers_deck):
        print("Its a draw.")
    else:
        print("You lose.")

    
def play():
    print(f"\tYour cards: {players_deck}, current score: {sum(players_deck)}")
    print(f"\tComputer's first card: {computers_deck[0]}")
    
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        add_card(players_deck)
        if check_burst(players_deck):
            print_result()
            print("You went over. You lose.")
        else:
            play()
    else:
        while sum(computers_deck) < 17:
            add_card(computers_deck)
        if check_burst(computers_deck):
            print_result()
            print("Computer went over. You won.")
        check_results()
    

# def prompt():
#     ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if ask == 'y':
#         os.system('cls')
#         print(logo)
#         global players_deck
#         global computers_deck
#         players_deck = [deal(),deal()]
#         computers_deck = [deal(),deal()]
#         play()

def add_card(to_whom):
    next_card = deal()
    if next_card == 11 and sum(to_whom)>10:
        computers_deck.append(1)
    else:    
        computers_deck.append(next_card)

# prompt()
check = False
while check:
    ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask == 'y':
        os.system('cls')
        print(logo)
        players_deck = [deal(),deal()]
        computers_deck = [deal(),deal()]
        natural()
        play()
    else:
        check = False