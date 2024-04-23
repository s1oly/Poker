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


#Need to tune this to further deal cards

def dealCard():
    global count, cards, cardSuit, cardRank 
    if count < 2:
        card = cards[count]
        cardSuit = str(card.suit)
        cardRank = str(card.rank)
        cardImage = showCard(cardSuit, cardRank, width= 75, height = 100)
        image_list.append(cardImage)
        canvas.create_image(20 + (1 + count%5) * 70, 20 + (1 + count //5) * 70, image = cardImage)
        count = count + 1
    else:
        message = messagebox.showerror("showerror", "You already have two cards")

        


#have a button with the image of the back of the card and pack it and when pressed change a card and add it 
#to the list such that the canvas can create the images


root = tkinter.Tk(screenName= "Poker Game")
root.geometry("800x1000")


deckOfCardImage = Image.open(f"PNG-cards-1.3/card_back_red.png")
deckOfCardImage = deckOfCardImage.resize((100,150))
deckOfCardImage = ImageTk.PhotoImage(deckOfCardImage)
deckOfCardButton = tkinter.Button(root, image=deckOfCardImage, command= lambda: [changeCard(), dealCard()])
deckOfCardButton.pack()

canvas = tkinter.Canvas(root, width= 400, height= 500)

canvas.pack()


root.mainloop()

