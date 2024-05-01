import poker
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import Entry
from PIL import Image
from PIL import ImageTk
from treys import Evaluator
from treys import Card
import random
import numpy as np
import math




# TODO: To fix the error for the gaame, just make the first thing a riase of a bet depending on the amount of money
#that the current bet is. For example, is the current bet is 5 and someone bets 8 then they have raised and 
# that boolean is marked true. 

deck = list(poker.Card)
random.shuffle(deck)
cards = []
board = []
image_listHand = []
image_listBoard = []
button_list = []
back_imageList = []
money = []
has_folded = []
handCount = 0
boardCount = 0
boardButtonPressCount = 0
#Getting the necessary card for the hand

def changeCardHand():
    card = deck.pop()
    return card

#Getting the necessary card for the board 
def changeCardBoard():
    global board 
    card = deck.pop()
    if len(board) < 5:
        board.append(card)
    return card

#Converting into the name for card searching
def convert_To_Words(suit):
    match suit:
        case "♣":
            return "clubs"
        case "♦":
            return"diamonds"
        case "♥":
            return "hearts"
        case "♠":
            return "spades"

#Converting into letter to use eval library 
def convert_to_Letter(suit):
    match suit:
        case "♣":
            return "c"
        case "♦":
            return "d"
        case "♥":
            return "h"
        case "♠":
            return "s" 

#displaying the card by finding the image
def showCard(suit, rank, width, height):
    '''Returns the necessary image '''
    suit = convert_To_Words(suit)
    image = Image.open(f"PNG-cards-1.3/{rank}_of_{suit}.png")
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image



#change spacing with the amount of people playing so it works better

#This deals the card to each of the players
def dealCard():
    '''Deals the Card to Each of the players'''
    global handCount, cards, cardSuit, cardRank, hand
    for i in range(amountOfPlayers):
        hand = []
        while handCount < 2:
            card = changeCardHand()
            cardSuit = str(card.suit)
            cardRank = str(card.rank)
            cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
            image_listHand.append(cardImage)
            backImage = Image.open(f"PNG-cards-1.3/card_back_black.png")
            backImage = backImage.resize((75, 100))
            backImage = ImageTk.PhotoImage(backImage)
            back_imageList.append(backImage)
            cardButton = tkinter.Button(canvas, image = backImage, text = getPlayerMoney(i), compound = "top", command = lambda index = image_listHand.index(cardImage): [flipImage(index)])
            button_list.append(cardButton)
            cardButton.place(x = (-16 * amountOfPlayers) + (55*(2*i+1) + 125*(i + 1)) + (handCount + 1)*80, y = (300))
            handCount = handCount + 1
            hand.append(card)
        cards.append(hand)
        handCount = 0



def setBoard():
    '''Method that sets the board'''
    global boardCount, board, cardSuit, cardRank, boardButtonPressCount
    while boardCount < 3 and boardButtonPressCount < 1:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_listBoard.append(cardImage)
        canvas.create_image(500 + boardCount*100, 130, image = cardImage)
        boardCount = boardCount + 1
    while boardCount < 4 and boardButtonPressCount < 2 and boardButtonPressCount >= 1:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_listBoard.append(cardImage)
        canvas.create_image(500 + boardCount*100, 130, image = cardImage)
        boardCount = boardCount + 1
    while boardCount < 5 and boardButtonPressCount < 3 and boardButtonPressCount >=2:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_listBoard.append(cardImage)
        canvas.create_image(500 + boardCount*100, 130, image = cardImage)
        boardCount = boardCount + 1
    boardButtonPressCount = boardButtonPressCount + 1
    

#Method that evaluates the hand and returns the highest value. Can go and find index then find winner
def evaluateHand():
    '''Method that evaluates the hand and returns the winner.'''
    global evalCard, evalBoard, scores
    eval = Evaluator()
    evalBoard = []
    scores = []
    if len(board) == 5 and len(cards)%amountOfPlayers == 0: 
        for card in board:
            a = str(card.rank) + convert_to_Letter(str(card.suit))
            card2 = Card.new(a)
            evalBoard.append(card2)
        for hands in cards:
            for card in hands:
                evalCard = []
                a = str(card.rank) + convert_to_Letter(str(card.suit))
                card2 = Card.new(a)
                evalCard.append(card2)
            scores.append(eval.evaluate(evalCard, evalBoard))
    message = messagebox.showinfo("showinfo", "Player number " + str(scores.index(np.min(scores))+ 1) + " was the winner with a " + eval.class_to_string(eval.get_rank_class(np.min(scores))))

def getAmountOfPlayers():
    '''Gets the global amount of players'''
    global amountOfPlayers
    amountOfPlayers = int(playerEntry.get())
    playerEntry.destroy()


def flipImage(index):
    '''Flips the Image from backside to rightside'''
    if button_list[index].cget('image') != str(image_listHand[index]):
        button_list[index].config(image = image_listHand[index])
    else:
        button_list[index].config(image = back_imageList[index])

def loadMoney():
    '''Loads the money into each of the players hands'''
    global potValue
    potValue = int(potEntry.get())
    for i in range(amountOfPlayers):
        money.append(potValue)
    potEntry.destroy()

#Fix this method by making the entries with one button, and then button spawns under and creates new buttons and stuff like that
def startBetting():
    '''Counts the money in the pot and the money for each player'''
    global currentPot, currentBets, hasRaised, entry
    currentPot = 0
    currentBets = []
    hasRaised = []
    bet_entryList = []
    bet_buttonList = []
    for i in range(len(cards)):
        hasRaised.append(False)
        has_folded.append(False)
        currentBets.append(0)
    for i in range(len(cards)):
        if has_folded[i]:
            continue
        else:
            if not hasRaised[i]:
                entry = Entry(canvas)
                entry.place(x = button_list[i * 2].winfo_x(), y = button_list[i*2].winfo_y() + 200)
                bet_entryList.append(entry)
                button = tkinter.Button(canvas, text = "Submit a Raise, Call or Fold", command = lambda index = i: [trackMoney(bet_entryList[index].get(), index), bet_entryList[index].destroy(), bet_buttonList[index].destroy()])
                bet_buttonList.append(button)
                button.place(x = button_list[i*2].winfo_x(), y = button_list[i*2].winfo_y() + 275)
            else:
                entry = Entry(canvas)
                entry.place(x = button_list[i * 2].winfo_x(), y = button_list[i*2].winfo_y() + 200)
                bet_entryList.append(entry)
                button = tkinter.Button(canvas, text = "Submit a Call or Fold", command = lambda index = i: [trackMoney(bet_entryList[index].get(), index), bet_entryList[index].destroy(), bet_buttonList[index].destroy()])
                bet_buttonList.append(button)
                button.place(x = button_list[i*2].winfo_x(), y = button_list[i*2].winfo_y() + 275)



#Need to fix the trackMoney Method, make new entries and buttons for raise and other stuff 
def trackMoney(action, index):
    global currentPot, currentBets, hasRaised
    ''' This method causes the amount of money to be given and collected'''
    if action == "Fold":
        has_folded[index] = True
    else:
        if int(action) > currentPot: # Raise
            hasRaised[index] = True
            currentPot = int(action)
            currentBets[index] = currentPot
            money[index] = money[index] - (currentBets[index])
        elif int(action) + currentBets[index] == currentPot: # Call
            money[index] = money[index] - (int(action))
            currentBets[index] = currentPot
    
    for index in range(len(image_listHand)):
        button_list[index].config(text = getPlayerMoney(index//2))
    currentMoneyLabel.config(text = "Current Bet " + str(currentPot))
    
    


def getPlayerMoney(index):
    return str(money[index])



#Need to show each money value with a lambda, 
#as well as show ways to transfer money and have continous games

   

root = tkinter.Tk()
root.geometry("1500x1700")
root.title("Poker Game")

deckOfCardImage = Image.open(f"PNG-cards-1.3/card_back_red.png")
deckOfCardImage = deckOfCardImage.resize((100,150))
deckOfCardImage = ImageTk.PhotoImage(deckOfCardImage)
deckOfCardButton = tkinter.Button(root, image=deckOfCardImage, command= lambda: [dealCard()])
deckOfCardButton.pack()

dealBoardButton = tkinter.Button(root, text= "Place the board", command = lambda: [setBoard()])
dealBoardButton.place(x = 1000, y = 10)

handEvaluationButton = tkinter.Button(root, text = "Evaluate your Hand", command =  lambda : [evaluateHand()])
handEvaluationButton.place(x = 1170, y = 10)

playerEntry = Entry(root)
playerEntry.pack()

entryButton= tkinter.Button(root, text = "Entry how many players you want", command = lambda : [getAmountOfPlayers(), entryButton.destroy()])
entryButton.pack()

potEntry = Entry(root)
potEntry.pack()

potButton = tkinter.Button(root, text = "What is the pot value?", command= lambda :[loadMoney(), potButton.destroy()])
potButton.pack()

betButton = tkinter.Button(root, text = "Bets for the round", command= lambda:[startBetting()])
betButton.place(x = 75, y = 10)

currentMoneyLabel = tkinter.Label(root, text= "Current Bet: " + str(0), padx= 5, pady= 5)
currentMoneyLabel.place(x = 250, y = 10)


canvas = tkinter.Canvas(root, width= 1500, height= 1500)

canvas.pack()



root.mainloop()
