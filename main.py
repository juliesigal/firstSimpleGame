import random

def print_card(card):
    if card <= 10:
        print(card)
    elif card == 11:
        print('J')
    elif card == 12:
        print('Q')
    elif card == 13:
        print('K')
    else: # card == 14:
        print('A')

my_score = 0
computer_score = 0
for i in range(3):
  # i draw a card
    card1 = random.randint(2, 14)
    print_card(card1)

    card2 = random.randint(2, 14)
    print_card(card2)

    if card1 == card2:
        print("this round it's draw")
    elif card1 < card2:
        computer_score += 1
        print("this round won computer")
    else:
        my_score += 1
        print("this round i won")

if my_score > computer_score:
    print("i won with the result: ", my_score, ":", computer_score)
elif computer_score > my_score:
    print("the computer won with the result: ", computer_score,":", my_score)
else:
    print("it's a draw")
