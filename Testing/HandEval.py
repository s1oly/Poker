import poker
import tkinter
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import Image
from PIL import ImageTk
import random

deck = list(poker.Card)
cards = []
image_list = []
count = 0

#Getting the necessary card

def changeCard():
    global cards
    random.shuffle(deck)
    card = deck.pop()
    if len(cards) <2:
        cards.append(card)
    return card


# def updateCardImage():
#     global canvas, cardImage
#     cardImage = showCard(cardSuit, cardRank, width= 150, height=200)
#     canvas.itemconfig(card_image_id, image = cardImage)

# def updateCardLabel():
#     global cardLabel
#     text = cardRank + " of " + cardSuit
#     cardLabel.config(text = text)

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


#need to tune the spacing a bit
def dealCard():
    global count, cards, cardSuit, cardRank 
    if count < 2:
        card = cards[count]
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(100 + count*100, 200, image = cardImage)
        count = count + 1
    else:
        message = messagebox.showerror("showerror", "You already have two cards")

        



root = tkinter.Tk(screenName= "Poker Game")
root.geometry("800x1000")


deckOfCardImage = Image.open(f"PNG-cards-1.3/card_back_red.png")
deckOfCardImage = deckOfCardImage.resize((100,150))
deckOfCardImage = ImageTk.PhotoImage(deckOfCardImage)
deckOfCardButton = tkinter.Button(root, image=deckOfCardImage, command= lambda: [changeCard(), dealCard()])
deckOfCardButton.pack()

canvas = tkinter.Canvas(root, width= 600, height= 700)

canvas.pack()


root.mainloop()

