#!/usr/bin/env python
# coding: utf-8

# # bet=int(input("How much money would you like to bet?"))
# 
# a=1 or 11
# k=10
# q=10
# j=10
# 
# money=100
# if win:
#     money=money+bet
#     print("You won!if  You have $", money)
# elif push: 
#     money=money
#     print("Push. You have $", money)
# else: 
#     money=money-bet*0
#     print("You lost! You have $", money)
# 
# while True:
#     data=input("Would you like to play again? If not, press enter to quit")
#     if data=="":
#         break
#     print("Thank you for playing!",s)
#     
#     
#     
# def game():
#     choice=0
#     clear()21
#     dealer_hand=deal(deck)
#     player_hand=deal(deck)
#     print("The dealer is showing a "+ str(dealer_hand[0]))
#     print("You have a"+ str(player_hand)+"for a total of"+ str(total(player_hand))
#     while choice!="q":
#         choice= input("Do you want to Hit (h) or stand(s)").lower()
#         clear()
#         if choice=="h":
#               hit(player_hand)
#               score(dealer_hand,player_hand)
#         elif choice=="s":
#               while total(dealer_hand)<17:
#                   hit(dealer_hand)
#               score(dealer_hand, player_hand)

# In[ ]:





# In[ ]:


#we worked on every part of the project together Jess&Sydney

name=input("What is your name? ")
print("WELCOME", name, "TO BLACKJACK, YOU HAVE $100 TO START WITH!")

file1=open("Blackjack_output","w")
L=[name,' '"played Blackjack"]
file1.writelines(L)
file1.close()


import random
suits=('♥hearts♥', '♦diamonds♦', '♠spades♠', '♣clubs♣')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values={'Two':2, 'Three':3, 'Four':4,'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing=True

class Card:
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+'of'+self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+ card.__str__()
        return 'the deck has:' +deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
        

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self, card):
        self.cards.append(card)
        self.value+=values[card.rank]
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How much are ya puttin on the table?"))
        except ValueError:
            print('Sorry the bet must be a number')
        else:
            if chips.bet>chips.total:
                print("Sorry your bet can't exceed:", chips.total)
            else:
                break
                
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("Press 'h' for hit or 's' for stand ")
        if x[0]=='h':
            hit(deck,hand)
        elif x[0]=='s':
            print(name," stands. Dealer is playing")
            playing=False
        else:
            print("press h or s stupid")
            continue
        break

def show_some(player, dealer):
    print('\n'"---Dealer's hand---")
    print("?????")
    print('', dealer.cards[1])
    print('\n', name, "----hand----", *player.cards, sep='\n')

def show_all(player, dealer):
    print('\n'"Dealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand=", dealer.value)
    print('\n', name, "Hand:", *player.cards, sep='\n')
    print('\n',name, "hand=", player.value)
    
def player_busts(player, dealer, chips):
    print(name, "busts")
    chips.lose_bet()
    
def player_wins(player, dealer, chips):
    print(name, "won!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("Dealer busts")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer won')
    chips.lose_bet()
    
def push(player,dealer):
    print("Tie!")
    
while True:
    print("Let the game begin......")
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_chips=Chips()
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        if dealer_hand.value>21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    print("Your total profits are:", player_chips.total)
    new_game=input("Another: y for yes and n for no??")
    if new_game[0]=='y':
        playing=True
        continue
    else:
        print("Goodbye see ya again sometime!")
        break

        













# In[ ]:





# In[ ]:





# In[ ]:




