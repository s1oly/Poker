import poker
import tkinter
from tkinter import ttk
from tkinter import messagebox
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


#need to tune the spacing a bit + as well as allow for multiple lists to find hand evaluations
#need to differentiate the amount 
def dealCard():
    global handCount, cards, cardSuit, cardRank 
    if handCount < 2:
        card = cards[handCount]
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(200 + handCount*160, 400, image = cardImage)
        handCount = handCount + 1
    else:
        message = messagebox.showerror("showerror", "You already have two cards")

def setBoard():
    global boardCount, board, cardSuit, cardRank
    if boardCount < 5:
        card = board[boardCount]
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(100 + boardCount*100, 200, image = cardImage)
        boardCount = boardCount + 1
    else:
        message = messagebox.showerror("showerror", "The board is already full")

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
        print(eval.evaluate(evalCard, evalBoard))




root = tkinter.Tk(screenName= "Poker Game")
root.geometry("800x1000")


deckOfCardImage = Image.open(f"PNG-cards-1.3/card_back_red.png")
deckOfCardImage = deckOfCardImage.resize((100,150))
deckOfCardImage = ImageTk.PhotoImage(deckOfCardImage)
deckOfCardButton = tkinter.Button(root, image=deckOfCardImage, command= lambda: [changeCardHand(), dealCard()])
deckOfCardButton.pack()

dealBoardButton = tkinter.Button(root, text= "Place the board", command = lambda: [changeCardBoard(), setBoard()])
dealBoardButton.pack()

handEvaluationButton = tkinter.Button(root, text = "Evaluate your Hand", command =  lambda : [evaluateHand()])
handEvaluationButton.pack()

canvas = tkinter.Canvas(root, width= 600, height= 700)

canvas.pack()



root.mainloop()

