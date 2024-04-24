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

deck = list(poker.Card)
random.shuffle(deck)
cards = []
board = []
image_list = []
handCount = 0
boardCount = 0

#Getting the necessary card

def changeCardHand():
    card = deck.pop()
    return card

def changeCardBoard():
    global board 
    card = deck.pop()
    if len(board) < 5:
        board.append(card)
    return card

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

def showCard(suit, rank, width, height):
    suit = convert_To_Words(suit)
    image = Image.open(f"PNG-cards-1.3/{rank}_of_{suit}.png")
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image


def dealCard():
    global handCount, cards, cardSuit, cardRank, hand
    for i in range(amountOfPlayers):
        while handCount < 2:
            print(i)
            hand = []
            card = changeCardHand()
            cardSuit = str(card.suit)
            cardRank = str(card.rank)
            cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
            image_list.append(cardImage)
            canvas.create_image((50 + 350*i) + handCount*160, (350 + 100*(i % 2)), image = cardImage)
            handCount = handCount + 1
            hand.append(card)
        cards.append(hand)
        handCount = 0
    print(cards)



def setBoard():
    global boardCount, board, cardSuit, cardRank
    while boardCount < 5:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(300 + boardCount*100, 130, image = cardImage)
        boardCount = boardCount + 1


def evaluateHand():
    global evalCard, evalBoard
    eval = Evaluator()
    evalBoard = []
    max = 0
    if len(board) == 5 and len(cards) == amountOfPlayers:
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
            max = np.max(max, eval.evaluate(evalCard, evalBoard))
    message = messagebox.showinfo("showinfo", "The max hand evaluation is " + str(max))

def getAmountOfPlayers():
    global amountOfPlayers 
    amountOfPlayers = int(entry.get())
    entry.destroy()
    print(amountOfPlayers)
        

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

entry = Entry(root)
entry.pack()

deleteEntryButton= tkinter.Button(root, text = "Entry how many players you want", command = lambda : [getAmountOfPlayers(), deleteEntryButton.destroy()])
deleteEntryButton.pack()



canvas = tkinter.Canvas(root, width= 1000, height= 1400)

canvas.pack()



root.mainloop()