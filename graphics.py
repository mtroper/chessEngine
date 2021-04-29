from tkinter import *

board = [["s" for i in range(8)] for j in range(8)]

board[0][0] = "br"
board[0][1] = "bn"
board[0][2] = "bb"
board[0][3] = "bq"
board[0][4] = "bk"
board[0][5] = "bb"
board[0][6] = "bn"
board[0][7] = "br"
for a in range(2):
    for b in range(8):
        if a == 0:
            board[1][b] = "bp"
        elif a == 1:
            board[6][b] = "wp"
board[7][0] = "wr"
board[7][1] = "wn"
board[7][2] = "wb"
board[7][3] = "wq"
board[7][4] = "wk"
board[7][5] = "wb"
board[7][6] = "wn"
board[7][7] = "wr"


moves = []
def onPress(square):
    moveText = "Current Move: "
    coords = square[0] + str(square[1])
    moves.append(coords)
    if len(moves) % 2 == 0:
        move = moves[-2] + " " + moves[-1]
        moveText += move
        col1 = ord(move[0]) - 97
        row1 = 8 - int(move[1])
        col2 = ord(move[3]) - 97
        row2 = 8 - int(move[4])
        if not isValid(col1,row1,col2,row2):
            moveText = "INVALID"
        else:

    else:
        moveText += moves[-1]
    topPadding.configure(text = moveText)

def isValid(col1,row1,col2,row2):
    #Case where move on anothe piece of same color
    if board[row1][col1][0] == board[row2][col2][0]:
        return False
    return True

################## GRAPHICS ####################
root = Tk()
root.title("Chess Engine")
root.geometry("1000x1000")

whiteImage = PhotoImage(file = "images/whitesquare.png")
blackImage = PhotoImage(file = "images/blacksquare.png")

wWhitePawn = PhotoImage(file = "images/wWhitePawn.png")
bWhitePawn = PhotoImage(file = "images/bWhitePawn.png")
wWhiteRook = PhotoImage(file = "images/wWhiteRook.png")
bWhiteRook = PhotoImage(file = "images/bWhiteRook.png")
wWhiteKnight = PhotoImage(file = "images/wWhiteKnight.png")
bWhiteKnight= PhotoImage(file = "images/bWhiteKnight.png")
wWhiteBishop = PhotoImage(file = "images/wWhiteBishop.png")
bWhiteBishop = PhotoImage(file = "images/bWhiteBishop.png")
wWhiteQueen = PhotoImage(file = "images/wWhiteQueen.png")
bWhiteQueen = PhotoImage(file = "images/bWhiteQueen.png")
wWhiteKing = PhotoImage(file = "images/wWhiteKing.png")
bWhiteKing = PhotoImage(file = "images/bWhiteKing.png")

wBlackPawn = PhotoImage(file = "images/wBlackPawn.png")
bBlackPawn = PhotoImage(file = "images/bBlackPawn.png")
wBlackRook = PhotoImage(file = "images/wBlackRook.png")
bBlackRook = PhotoImage(file = "images/bBlackRook.png")
wBlackKnight = PhotoImage(file = "images/wBlackKnight.png")
bBlackKnight= PhotoImage(file = "images/bBlackKnight.png")
wBlackBishop = PhotoImage(file = "images/wBlackBishop.png")
bBlackBishop = PhotoImage(file = "images/bBlackBishop.png")
wBlackQueen = PhotoImage(file = "images/wBlackQueen.png")
bBlackQueen = PhotoImage(file = "images/bBlackQueen.png")
wBlackKing = PhotoImage(file = "images/wBlackKing.png")
bBlackKing = PhotoImage(file = "images/bBlackKing.png")

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
root.configure(bg=_from_rgb((61,61,61)))
topPadding = Label(root, text="Current Move:", font="none 24 bold", bg=_from_rgb((61,61,61)))
topPadding.grid(row = 0, columnspan = 8, pady = 60, padx=(275,0))
invalidMove = Label(root, text="Inavlid Move:", font="none 24 bold", bg=_from_rgb((61,61,61)))
leftPadding = Label(root, bg=_from_rgb((61,61,61)))
leftPadding.grid(row = 0, rowspan = 8, padx = 90)

#BLACK PIECES ROW 1
whiteSquare56 = Button(root, image=wBlackRook, command = lambda: onPress(("a",8)), borderwidth = 0, highlightthickness= 0)
whiteSquare56.grid(row=1,column=1)
blackSquare16 = Button(root, image=bBlackKnight, command = lambda: onPress(("b",8)), borderwidth = 0, highlightthickness = 0)
blackSquare16.grid(row=1,column=2)
whiteSquare9 = Button(root, image=wBlackBishop, command = lambda: onPress(("c",8)), borderwidth = 0, highlightthickness= 0)
whiteSquare9.grid(row=1,column=3)
blackSquare32 = Button(root, image=bBlackQueen, command = lambda: onPress(("d",8)), borderwidth = 0, highlightthickness = 0)
blackSquare32.grid(row=1,column=4)
whiteSquare24 = Button(root, image=wBlackKing, command = lambda: onPress(("e",8)), borderwidth = 0, highlightthickness= 0)
whiteSquare24.grid(row=1,column=5)
blackSquare48 = Button(root, image=bBlackBishop, command = lambda: onPress(("f",8)), borderwidth = 0, highlightthickness = 0)
blackSquare48.grid(row=1,column=6)
whiteSquare41 = Button(root, image=wBlackKnight, command = lambda: onPress(("g",8)), borderwidth = 0, highlightthickness= 0)
whiteSquare41.grid(row=1,column=7)
blackSquare = Button(root, image=bBlackRook, command = lambda: onPress(("h",8)), borderwidth = 0, highlightthickness = 0)
blackSquare.grid(row=1,column=8)
#####################

#BLACK PAWN ROW 2
blackSquare57 = Button(root, image=bBlackPawn, command = lambda: onPress(("a",7)), borderwidth = 0, highlightthickness = 0)
blackSquare57.grid(row=2,column=1)
whiteSquare17 = Button(root, image=wBlackPawn, command = lambda: onPress(("b",7)), borderwidth = 0, highlightthickness= 0)
whiteSquare17.grid(row=2,column=2)
blackSquare10 = Button(root, image=bBlackPawn, command = lambda: onPress(("c",7)), borderwidth = 0, highlightthickness = 0)
blackSquare10.grid(row=2,column=3)
whiteSquare33 = Button(root, image=wBlackPawn, command = lambda: onPress(("d",7)), borderwidth = 0, highlightthickness= 0)
whiteSquare33.grid(row=2,column=4)
blackSquare25 = Button(root, image=bBlackPawn, command = lambda: onPress(("e",7)), borderwidth = 0, highlightthickness = 0)
blackSquare25.grid(row=2,column=5)
whiteSquare49 = Button(root, image=wBlackPawn, command = lambda: onPress(("f",7)), borderwidth = 0, highlightthickness= 0)
whiteSquare49.grid(row=2,column=6)
blackSquare42 = Button(root, image=bBlackPawn, command = lambda: onPress(("g",7)), borderwidth = 0, highlightthickness = 0)
blackSquare42.grid(row=2,column=7)
whiteSquare = Button(root, image=wBlackPawn, command = lambda: onPress(("h",7)), borderwidth = 0, highlightthickness= 0)
whiteSquare.grid(row=2,column=8)

######################

#ROW #3
whiteSquare58 = Button(root, image=whiteImage, command = lambda: onPress(("a",6)), borderwidth = 0, highlightthickness= 0)
whiteSquare58.grid(row=3,column=1)
blackSquare18 = Button(root, image=blackImage, command = lambda: onPress(("b",6)), borderwidth = 0, highlightthickness = 0)
blackSquare18.grid(row=3,column=2)
whiteSquare11 = Button(root, image=whiteImage, command = lambda: onPress(("d",6)), borderwidth = 0, highlightthickness= 0)
whiteSquare11.grid(row=3,column=3)
blackSquare34 = Button(root, image=blackImage, command = lambda: onPress(("d",6)), borderwidth = 0, highlightthickness = 0)
blackSquare34.grid(row=3,column=4)
whiteSquare26 = Button(root, image=whiteImage, command = lambda: onPress(("e",6)), borderwidth = 0, highlightthickness= 0)
whiteSquare26.grid(row=3,column=5)
blackSquare50 = Button(root, image=blackImage, command = lambda: onPress(("f",6)), borderwidth = 0, highlightthickness = 0)
blackSquare50.grid(row=3,column=6)
whiteSquare43 = Button(root, image=whiteImage, command = lambda: onPress(("g",6)), borderwidth = 0, highlightthickness= 0)
whiteSquare43.grid(row=3,column=7)
blackSquare2 = Button(root, image=blackImage, command = lambda: onPress(("h",6)), borderwidth = 0, highlightthickness = 0)
blackSquare2.grid(row=3,column=8)
#######################

#ROW 4
blackSquare59 = Button(root, image=blackImage, command = lambda: onPress(("a",5)), borderwidth = 0, highlightthickness = 0)
blackSquare59.grid(row=4,column=1)
whiteSquare19 = Button(root, image=whiteImage, command = lambda: onPress(("b",5)), borderwidth = 0, highlightthickness= 0)
whiteSquare19.grid(row=4,column=2)
blackSquare12 = Button(root, image=blackImage, command = lambda: onPress(("c",5)), borderwidth = 0, highlightthickness = 0)
blackSquare12.grid(row=4,column=3)
whiteSquare35 = Button(root, image=whiteImage, command = lambda: onPress(("d",5)), borderwidth = 0, highlightthickness= 0)
whiteSquare35.grid(row=4,column=4)
blackSquare27 = Button(root, image=blackImage, command = lambda: onPress(("e",5)), borderwidth = 0, highlightthickness = 0)
blackSquare27.grid(row=4,column=5)
whiteSquare51 = Button(root, image=whiteImage, command = lambda: onPress(("f",5)), borderwidth = 0, highlightthickness= 0)
whiteSquare51.grid(row=4,column=6)
blackSquare44 = Button(root, image=blackImage, command = lambda: onPress(("g",5)), borderwidth = 0, highlightthickness = 0)
blackSquare44.grid(row=4,column=7)
whiteSquare2 = Button(root, image=whiteImage, command = lambda: onPress(("h",5)), borderwidth = 0, highlightthickness= 0)
whiteSquare2.grid(row=4,column=8)
###########################

#ROW 5
whiteSquare60 = Button(root, image=whiteImage, command = lambda: onPress(("a",4)), borderwidth = 0, highlightthickness= 0)
whiteSquare60.grid(row=5,column=1)
blackSquare20 = Button(root, image=blackImage, command = lambda: onPress(("b",4)), borderwidth = 0, highlightthickness = 0)
blackSquare20.grid(row=5,column=2)
whiteSquare13 = Button(root, image=whiteImage, command = lambda: onPress(("c",4)), borderwidth = 0, highlightthickness= 0)
whiteSquare13.grid(row=5,column=3)
blackSquare36 = Button(root, image=blackImage, command = lambda: onPress(("d",4)), borderwidth = 0, highlightthickness = 0)
blackSquare36.grid(row=5,column=4)
whiteSquare28 = Button(root, image=whiteImage, command = lambda: onPress(("e",4)), borderwidth = 0, highlightthickness= 0)
whiteSquare28.grid(row=5,column=5)
blackSquare52 = Button(root, image=blackImage, command = lambda: onPress(("f",4)), borderwidth = 0, highlightthickness = 0)
blackSquare52.grid(row=5,column=6)
whiteSquare45 = Button(root, image=whiteImage, command = lambda: onPress(("g",4)), borderwidth = 0, highlightthickness= 0)
whiteSquare45.grid(row=5,column=7)
blackSquare4 = Button(root, image=blackImage, command = lambda: onPress(("h",4)), borderwidth = 0, highlightthickness = 0)
blackSquare4.grid(row=5,column=8)
######################

#ROW 6
blackSquare61 = Button(root, image=blackImage, command = lambda: onPress(("a",3)), borderwidth = 0, highlightthickness = 0)
blackSquare61.grid(row=6,column=1)
whiteSquare21 = Button(root, image=whiteImage, command = lambda: onPress(("b",3)), borderwidth = 0, highlightthickness= 0)
whiteSquare21.grid(row=6,column=2)
blackSquare14 = Button(root, image=blackImage, command = lambda: onPress(("c",3)), borderwidth = 0, highlightthickness = 0)
blackSquare14.grid(row=6,column=3)
whiteSquare37 = Button(root, image=whiteImage, command = lambda: onPress(("d",3)), borderwidth = 0, highlightthickness= 0)
whiteSquare37.grid(row=6,column=4)
blackSquare29 = Button(root, image=blackImage, command = lambda: onPress(("e",3)), borderwidth = 0, highlightthickness = 0)
blackSquare29.grid(row=6,column=5)
whiteSquare53 = Button(root, image=whiteImage, command = lambda: onPress(("f",3)), borderwidth = 0, highlightthickness= 0)
whiteSquare53.grid(row=6,column=6)
blackSquare46 = Button(root, image=blackImage, command = lambda: onPress(("g",3)), borderwidth = 0, highlightthickness = 0)
blackSquare46.grid(row=6,column=7)
whiteSquare5 = Button(root, image=whiteImage, command = lambda: onPress(("h",3)), borderwidth = 0, highlightthickness= 0)
whiteSquare5.grid(row=6,column=8)
#####################

#WHITE PAWNS ROW 7
whiteSquare62 = Button(root, image=wWhitePawn, command = lambda: onPress(("a",2)), borderwidth = 0, highlightthickness= 0)
whiteSquare62.grid(row=7,column=1)
blackSquare22 = Button(root, image=bWhitePawn, command = lambda: onPress(("b",2)), borderwidth = 0, highlightthickness = 0)
blackSquare22.grid(row=7,column=2)
whiteSquare15 = Button(root, image=wWhitePawn, command = lambda: onPress(("c",2)), borderwidth = 0, highlightthickness= 0)
whiteSquare15.grid(row=7,column=3)
blackSquare38 = Button(root, image=bWhitePawn, command = lambda: onPress(("d",2)), borderwidth = 0, highlightthickness = 0)
blackSquare38.grid(row=7,column=4)
whiteSquare30 = Button(root, image=wWhitePawn, command = lambda: onPress(("e",2)), borderwidth = 0, highlightthickness= 0)
whiteSquare30.grid(row=7,column=5)
blackSquare54 = Button(root, image=bWhitePawn, command = lambda: onPress(("f",2)), borderwidth = 0, highlightthickness = 0)
blackSquare54.grid(row=7,column=6)
whiteSquare47 = Button(root, image=wWhitePawn, command = lambda: onPress(("g",2)), borderwidth = 0, highlightthickness= 0)
whiteSquare47.grid(row=7,column=7)
blackSquare6 = Button(root, image=bWhitePawn, command = lambda: onPress(("h",2)), borderwidth = 0, highlightthickness = 0)
blackSquare6.grid(row=7,column=8)
##################


#WHITE PIECES ROW 8
blackSquare63 = Button(root, image=bWhiteRook, command = lambda: onPress(("a",1)), borderwidth = 0, highlightthickness = 0)
blackSquare63.grid(row=8,column=1)
whiteSquare23 = Button(root, image=wWhiteKnight, command = lambda: onPress(("b",1)), borderwidth = 0, highlightthickness= 0)
whiteSquare23.grid(row=8,column=2)
blackSquare8 = Button(root, image=bWhiteBishop, command = lambda: onPress(("c",1)), borderwidth = 0, highlightthickness = 0)
blackSquare8.grid(row=8,column=3)
whiteSquare39 = Button(root, image=wWhiteQueen, command = lambda: onPress(("d",1)), borderwidth = 0, highlightthickness= 0)
whiteSquare39.grid(row=8,column=4)
blackSquare31 = Button(root, image=bWhiteKing, command = lambda: onPress(("e",1)), borderwidth = 0, highlightthickness = 0)
blackSquare31.grid(row=8,column=5)
whiteSquare55 = Button(root, image=wWhiteBishop, command = lambda: onPress(("f",1)), borderwidth = 0, highlightthickness= 0)
whiteSquare55.grid(row=8,column=6)
blackSquare40 = Button(root, image=bWhiteKnight, command = lambda: onPress(("g",1)), borderwidth = 0, highlightthickness = 0)
blackSquare40.grid(row=8,column=7)
whiteSquare7 = Button(root, image=wWhiteRook, command = lambda: onPress(("h",1)), borderwidth = 0, highlightthickness= 0)
whiteSquare7.grid(row=8,column=8)
###################

def main(): 
    root.mainloop()
    
    

if __name__ == '__main__':
    main()


