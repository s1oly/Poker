import poker
import tkinter
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
import random

deck = list(poker.Card)
cards = []

card = None
cardSuit = None
cardRank = None

#Getting the necessary card

def changeCard():
    global card, cardSuit, cardRank
    random.shuffle(deck)
    card = deck.pop()
    cardSuit = str(card.suit)
    cardRank = str(card.rank)


def updateCardImage():
    global canvas, cardImage
    cardImage = showCard(cardSuit, cardRank, width= 150, height=200)
    canvas.itemconfig(card_image_id, image = cardImage)

def updateCardLabel():
    global cardLabel
    text = cardRank + " of " + cardSuit
    cardLabel.config(text = text)

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

def showCard(suit, rank, width, height):
    suit = convert_To_Words(suit)
    image = Image.open(f"PNG-cards-1.3/{rank}_of_{suit}.png")
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image

changeCard()

#have a button with the image of the back of the card and pack it and when pressed change a card and add it 
#to the list such that the canvas can create the images


root = tkinter.Tk()
root.geometry("400x500")

canvas = tkinter.Canvas(root, width= 300, height= 400)

canvas.pack()

cardImage = showCard(cardSuit, cardRank, width = 150, height = 200)
card_image_id = canvas.create_image(150, 200,image = cardImage)

changeCardButton = ttk.Button(root, text="Change Card", command = lambda: [changeCard(), updateCardImage(), updateCardLabel()])
changeCardButton.pack()

cardLabel = ttk.Label(text = cardRank + " of " + cardSuit)
cardLabel.pack()

root.mainloop()










