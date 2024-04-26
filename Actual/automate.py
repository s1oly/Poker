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

deck = list(poker.Card)
random.shuffle(deck)
cards = []
board = []
image_listHand = []
image_listBoard = []
button_list = []
back_imageList = []
handCount = 0
boardCount = 0
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
            cardButton = tkinter.Button(canvas, image = backImage, command = lambda index = image_listHand.index(cardImage): [flipImage(index)])
            button_list.append(cardButton)
            cardButton.place(x = (-25 * amountOfPlayers) + (50*(2*i+1) + 120*(i + 1)) + (handCount + 1)*80, y = (300))
            handCount = handCount + 1
            hand.append(card)
        cards.append(hand)
        handCount = 0



def setBoard():
    '''Method that sets the board'''
    global boardCount, board, cardSuit, cardRank
    while boardCount < 5:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_listBoard.append(cardImage)
        canvas.create_image(340 + boardCount*100, 130, image = cardImage)
        boardCount = boardCount + 1

#Method that evaluates the hand and returns the highest value. Can go and find index then find winner
def evaluateHand():
    '''Method that evaluates the hand and returns the winner.'''
    global evalCard, evalBoard
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
    message = messagebox.showinfo("showinfo", "Player number " + str(scores.index(np.min(scores)) % amountOfPlayers + 1) + " was the winner with a " + eval.class_to_string(eval.get_rank_class(np.min(scores))))

#gets the global amount of players
def getAmountOfPlayers():
    '''Gets the global amount of players'''
    global amountOfPlayers 
    amountOfPlayers = int(playerEntry.get())
    playerEntry.destroy() 




def flipImage(index):
    global backImage
    '''Flips the Image from backside to rightside'''
    if button_list[index].cget('image') != str(image_listHand[index]):
        # backImage = Image.open(f"PNG-cards-1.3/card_back_black.png")
        # backImage = backImage.resize((75, 100))
        # backImage = ImageTk.PhotoImage(backImage)
        # back_imageList.append(backImage)
        button_list[index].config(image = image_listHand[index])
    else:
        button_list[index].config(image = back_imageList[index])


   

root = tkinter.Tk()
root.geometry("1500x1700")
root.title("Poker Game")

deckOfCardImage = Image.open(f"PNG-cards-1.3/card_back_red.png")
deckOfCardImage = deckOfCardImage.resize((100,150))
deckOfCardImage = ImageTk.PhotoImage(deckOfCardImage)
deckOfCardButton = tkinter.Button(root, image=deckOfCardImage, command= lambda: [dealCard()])
deckOfCardButton.pack()

dealBoardButton = tkinter.Button(root, text= "Place the board", command = lambda: [setBoard()])
dealBoardButton.pack()

handEvaluationButton = tkinter.Button(root, text = "Evaluate your Hand", command =  lambda : [evaluateHand()])
handEvaluationButton.pack()

playerEntry = Entry(root)
playerEntry.pack()

deleteEntryButton= tkinter.Button(root, text = "Entry how many players you want", command = lambda : [getAmountOfPlayers(), deleteEntryButton.destroy()])
deleteEntryButton.pack()



canvas = tkinter.Canvas(root, width= 1100, height= 1500)

canvas.pack()



root.mainloop()