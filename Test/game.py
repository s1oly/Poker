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

deck = list(poker.Card)
random.shuffle(deck)
cards = []
board = []
image_list = []
handCount = 0
boardCount = 0

#Getting the necessary card

def changeCardHand():
    global cards
    card = deck.pop()
    if len(cards) <2:
        cards.append(card)
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


#Need to add in the angle part and that will come in for all of the hands and that finds the highest value hand at the end with the button
def dealCard():
    global handCount, cards, cardSuit, cardRank 
    while handCount < 2:
        card = changeCardHand()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(200 + handCount*160, 400, image = cardImage)
        handCount = handCount + 1


def setBoard():
    global boardCount, board, cardSuit, cardRank
    while boardCount < 5:
        card = changeCardBoard()
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(100 + boardCount*100, 200, image = cardImage)
        boardCount = boardCount + 1


def evaluateHand():
    global evalCard, evalBoard
    eval = Evaluator()
    evalCard = []
    evalBoard = []
    if len(board) == 5 and len(cards) ==2:
        for card in cards:
            a = str(card.rank) + convert_to_Letter(str(card.suit))
            card2 = Card.new(a)
            evalCard.append(card2)
        for card in board:
            a = str(card.rank) + convert_to_Letter(str(card.suit))
            card2 = Card.new(a)
            evalBoard.append(card2)
    message = messagebox.showinfo("showinfo", "Your hand evaluation is " + str(eval.evaluate(evalCard, evalBoard)))

def getAmountOfPlayers():
    global amount 
    amount = entry.get()
    entry.destroy()
    print(amount)
        

root = tkinter.Tk()
root.geometry("800x1000")
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



canvas = tkinter.Canvas(root, width= 600, height= 700)

canvas.pack()



root.mainloop()