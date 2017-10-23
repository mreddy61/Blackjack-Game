import random

balance=1000
list_of_transactions=['Welcome','Initial balance is 1000']
play_again=1
balance_counter=1
class Cards(object):
    cardset=[1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    def __init__(self):
        pass
    def card_select(self):
        return random.choice(self.cardset)
    def card_value(self,card):
        for i in range(14):
            if card==self.cardset[i]:
                cardvalue=int(card)
                break
            elif card=='A':
                cardvalue=11
                break
            elif (card=='J' or card=='Q' or card=='K'):
                cardvalue=10
                break
            else:
                continue
        return cardvalue
card=Cards()
class Player(Cards):
    def __init__(self):
        pass
    def player1(self):
        card=Cards()
        player1_card1=card.card_select()
        player1_card2=card.card_select()
        return player1_card1,player1_card2
    def player2(self):
        card=Cards()
        player2_card1=card.card_select()
        player2_card2=card.card_select()
        return player2_card1,player2_card2
class Bet(object):
    global balance
    bet_amount=0
    def __init__(self):
        pass
    def bet_value(self):
        self.bet_amount=int(input("Enter the Bet Amount: ",))
        if self.bet_amount>balance:
            print("Your bet is higher than you balance,Please enter bet amount less than balance")
            self.bet_amount=int(input("Enter the Bet Amount: ",))
    def update_balance(self,win):
        global balance
        global play_again
        global list_of_transactions
        global balance_counter
        if balance_counter==1:
            print(list_of_transactions)
        else:
            if balance<self.bet_amount:
                print("Your Bet amount is higher than your balance. Your Balance is:",balance)
                play_again=0
            else:
                if win==1:
                    balance=balance+self.bet_amount
                    list_of_transactions.append([self.bet_amount,'won'])
                    balance_counter+=1
                elif win==0:
                    balance=balance-self.bet_amount
                    list_of_transactions.append([self.bet_amount,'Lost'])
                    balance_counter+=1
                elif win==3:
                    balance=balance+(self.bet_amount*1.5)
                    list_of_transactions.append([self.bet_amount,'BlackJack'])
                    balance_counter+=1
                else:
                    balance=balance
                    list_of_transactions.append([self.bet_amount,'Push'])
                    balance_counter+=1
            print("Your Transaction History is:\n",list_of_transactions)
            print("Balance remaining is: ",balance)
player=Player()
player1_cards=player.player1()
player2_cards=player.player2()		
bet=Bet()  
def add_values(player_num,position,sumofplayer):
    global player1_cards
    global player2_cards
    global card
    if player_num==1:
        sumofplayer1=sumofplayer
        value=card.card_value(player1_cards[position])
        sumofplayer1=sumofplayer+value
        for i in player1_cards:
            counter=0
            if i=='A':
                counter+=1
        for j in range(10):
            if (j<=counter and sumofplayer1>21):
                sumofplayer1=sumofplayer1-j*10
            else:
                break
        return sumofplayer1
    elif player_num==2:
        sumofplayer2=sumofplayer
        value=card.card_value(player2_cards[position])
        sumofplayer2=sumofplayer+value
        for i in player2_cards:
            counter=0
            if i=='A':
                counter+=1
        for j in range(10):
            if (j<=counter and sumofplayer2>21):
                sumofplayer2=sumofplayer2-j*10
            else:
                break
        return sumofplayer2
        
def player_choice(value1,value2):
    global sumofplayer
    global player1_cards
    global player2_cards
    global card
    global bet
    global balance_counter
    player_num=1
    position=1
    sumofplayer1=value1
    sumofplayer2=value2
    if sumofplayer1<=21:
        while sumofplayer1<=21:
            if player_num!=2:
                player_num=int(input('Enter 1 to HIT and 2 to STAND:'))
            if player_num==1:
                position+=1
                newcard=card.card_select()
                player1_cards=list(player1_cards)
                player1_cards.insert(position,newcard)
                player1_cards=tuple(player1_cards)
                print("Your Cards:",player1_cards)
                sumofplayer1=add_values(player_num,position,sumofplayer1)
                print("Sum of player1 is: ",sumofplayer1)
                if sumofplayer1==21:
                    player_num=2
            elif player_num==2:
                print("System Cards:",player2_cards)
                position=1
                sumofplayer2=value2
                print("sum of player2 is:",sumofplayer2)
                while sumofplayer2<=21:
                    if sumofplayer2<17:
                        position+=1
                        newcard=card.card_select()
                        player2_cards=list(player2_cards)
                        player2_cards.insert(position,newcard)
                        player2_cards=tuple(player2_cards)
                        print("System Cards:",player2_cards)
                        sumofplayer2=add_values(player_num,position,sumofplayer2)
                        print("sum of player2 is: ",sumofplayer2)
                    elif (sumofplayer2>=17 and sumofplayer2<=21):
                        if (sumofplayer1>sumofplayer2):
                            print("You Won")
                            balance_counter+=1
                            win=1
                            bet.update_balance(win)
                            break
                        elif(sumofplayer1==sumofplayer2):
                            win=2
                            print("Push")
                            balance_counter+=1
                            bet.update_balance(win)
                            break
                        else:
                            win=0
                            print("System Won")
                            balance_counter+=1
                            bet.update_balance(win)
                            break
                else:
                    print("System player Bust, You won")
                    win=1
                    balance_counter+=1
                    bet.update_balance(win)
                    break
        else:
            print("Bust, You Lost")
            win=0
            balance_counter+=1
            bet.update_balance(win)
def play_game():
    global player1_cards
    global player2_cards
    global card
    global bet
    global play_again
    global balance_counter
    bet.update_balance(1)
    bet.bet_value()
    print("Your Cards:",player1_cards)
    print("System first card:",player2_cards[0])
    value1=card.card_value(player1_cards[0])+card.card_value(player1_cards[1])
    value2=card.card_value(player2_cards[0])+card.card_value(player2_cards[1])
    if value1>21:
        value1=value1-10
    print("Sum of player is:",value1)
    if value2>21:
        value2=value2-10
    if (value1==21 and value2!=21):
        print("Black Jack,You Won")
        balance_counter+=1
        bet.update_balance(3)
    elif (value2==21 and value1!=21):
        print("System Cards are:",player1_cards)
        print("Black Jack,System Won")
        balance_counter+=1
        bet.update_balance(0)
    elif (value1==21 and value2==21):
        print("Push")
        balance_counter+=1
    else:
        player_choice(value1,value2)
    if balance>0:
        play_again=int(input("Enter 1 to play again and 0 to exit:",))
    else:
        print("Low balance")
        play_again=0
play_game()
while True:
    if play_again==1:
        balance_counter=1
        player=Player()
        player1_cards=player.player1()
        player2_cards=player.player2()
        play_game() 
    else:
        print("Game EXIT")
        break
