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
currentSquare = []
def onPress(square, squareid):
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
            before = int(str(currentSquare[-1].cget("image"))[-1])
            after = int(str(squareid.cget("image"))[-1])
            if before%2 != after%2:
                difference = -1
                if before%2 == 1:
                    difference = 1
                newAfter =  str(squareid.cget("image"))[:-1] + str((after - difference))
                newBefore = str(currentSquare[-1].cget("image"))[:-1] + str((before - (-difference)))
                squareid.configure(image = newBefore)
                currentSquare[-1].configure(image = newAfter)
            else:
                temp = squareid.cget("image")
                squareid.configure(image = currentSquare[-1].cget("image"))
                currentSquare[-1].configure(image = temp)
            temp1 = board[row1][col1]
            board[row1][col1] = board[row2][col2]
            board[row2][col2] = temp1
    else:
        moveText += moves[-1]
        currentSquare.append(squareid)
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

whiteImage = PhotoImage(file = "images/whitesquare.png") #1
blackImage = PhotoImage(file = "images/blacksquare.png") #2
wWhitePawn = PhotoImage(file = "images/wWhitePawn.png") #3
bWhitePawn = PhotoImage(file = "images/bWhitePawn.png") #4
wWhiteRook = PhotoImage(file = "images/wWhiteRook.png") #5
bWhiteRook = PhotoImage(file = "images/bWhiteRook.png") #6
wWhiteKnight = PhotoImage(file = "images/wWhiteKnight.png") #7
bWhiteKnight= PhotoImage(file = "images/bWhiteKnight.png") #8

FILLER = PhotoImage(file = "images/whitesquare.png") #9
FILLER1 = PhotoImage(file = "images/whitesquare.png") #10

wWhiteBishop = PhotoImage(file = "images/wWhiteBishop.png") #11
bWhiteBishop = PhotoImage(file = "images/bWhiteBishop.png") #12
wWhiteQueen = PhotoImage(file = "images/wWhiteQueen.png") #13
bWhiteQueen = PhotoImage(file = "images/bWhiteQueen.png") #14
wWhiteKing = PhotoImage(file = "images/wWhiteKing.png") #15
bWhiteKing = PhotoImage(file = "images/bWhiteKing.png") #16

wBlackPawn = PhotoImage(file = "images/wBlackPawn.png") #17
bBlackPawn = PhotoImage(file = "images/bBlackPawn.png") #18

FILLER2 = PhotoImage(file = "images/whitesquare.png") #19
FILLER3 = PhotoImage(file = "images/whitesquare.png") #20

wBlackRook = PhotoImage(file = "images/wBlackRook.png") #21
bBlackRook = PhotoImage(file = "images/bBlackRook.png") #22
wBlackKnight = PhotoImage(file = "images/wBlackKnight.png") #23
bBlackKnight= PhotoImage(file = "images/bBlackKnight.png") #24
wBlackBishop = PhotoImage(file = "images/wBlackBishop.png") #25
bBlackBishop = PhotoImage(file = "images/bBlackBishop.png") #26
wBlackQueen = PhotoImage(file = "images/wBlackQueen.png") #27
bBlackQueen = PhotoImage(file = "images/bBlackQueen.png")#28

FILLER4 = PhotoImage(file = "images/whitesquare.png") #29
FILLER5 = PhotoImage(file = "images/whitesquare.png") #30

wBlackKing = PhotoImage(file = "images/wBlackKing.png")#31
bBlackKing = PhotoImage(file = "images/bBlackKing.png")#32

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
root.configure(bg=_from_rgb((61,61,61)))
topPadding = Label(root, text="Current Move:", font="none 24 bold", bg=_from_rgb((61,61,61)))
topPadding.grid(row = 0, columnspan = 8, pady = 60, padx=(275,0))
invalidMove = Label(root, text="Inavlid Move:", font="none 24 bold", bg=_from_rgb((61,61,61)))
leftPadding = Label(root, bg=_from_rgb((61,61,61)))
leftPadding.grid(row = 0, rowspan = 8, padx = 90)

#BLACK PIECES ROW 1
whiteSquare56 = Button(root, image=wBlackRook, command = lambda: onPress(("a",8), whiteSquare56), borderwidth = 0, highlightthickness= 0)
whiteSquare56.grid(row=1,column=1)
blackSquare16 = Button(root, image=bBlackKnight, command = lambda: onPress(("b",8), blackSquare16), borderwidth = 0, highlightthickness = 0)
blackSquare16.grid(row=1,column=2)
whiteSquare9 = Button(root, image=wBlackBishop, command = lambda: onPress(("c",8), whiteSquare9), borderwidth = 0, highlightthickness= 0)
whiteSquare9.grid(row=1,column=3)
blackSquare32 = Button(root, image=bBlackQueen, command = lambda: onPress(("d",8), blackSquare32), borderwidth = 0, highlightthickness = 0)
blackSquare32.grid(row=1,column=4)
whiteSquare24 = Button(root, image=wBlackKing, command = lambda: onPress(("e",8), whiteSquare24), borderwidth = 0, highlightthickness= 0)
whiteSquare24.grid(row=1,column=5)
blackSquare48 = Button(root, image=bBlackBishop, command = lambda: onPress(("f",8), blackSquare48), borderwidth = 0, highlightthickness = 0)
blackSquare48.grid(row=1,column=6)
whiteSquare41 = Button(root, image=wBlackKnight, command = lambda: onPress(("g",8), whiteSquare41), borderwidth = 0, highlightthickness= 0)
whiteSquare41.grid(row=1,column=7)
blackSquare = Button(root, image=bBlackRook, command = lambda: onPress(("h",8), blackSquare), borderwidth = 0, highlightthickness = 0)
blackSquare.grid(row=1,column=8)
#####################

#BLACK PAWN ROW 2
blackSquare57 = Button(root, image=bBlackPawn, command = lambda: onPress(("a",7), blackSquare57), borderwidth = 0, highlightthickness = 0)
blackSquare57.grid(row=2,column=1)
whiteSquare17 = Button(root, image=wBlackPawn, command = lambda: onPress(("b",7), whiteSquare17), borderwidth = 0, highlightthickness= 0)
whiteSquare17.grid(row=2,column=2)
blackSquare10 = Button(root, image=bBlackPawn, command = lambda: onPress(("c",7), blackSquare10), borderwidth = 0, highlightthickness = 0)
blackSquare10.grid(row=2,column=3)
whiteSquare33 = Button(root, image=wBlackPawn, command = lambda: onPress(("d",7), whiteSquare33), borderwidth = 0, highlightthickness= 0)
whiteSquare33.grid(row=2,column=4)
blackSquare25 = Button(root, image=bBlackPawn, command = lambda: onPress(("e",7), blackSquare25), borderwidth = 0, highlightthickness = 0)
blackSquare25.grid(row=2,column=5)
whiteSquare49 = Button(root, image=wBlackPawn, command = lambda: onPress(("f",7), whiteSquare49), borderwidth = 0, highlightthickness= 0)
whiteSquare49.grid(row=2,column=6)
blackSquare42 = Button(root, image=bBlackPawn, command = lambda: onPress(("g",7), blackSquare42), borderwidth = 0, highlightthickness = 0)
blackSquare42.grid(row=2,column=7)
whiteSquare = Button(root, image=wBlackPawn, command = lambda: onPress(("h",7), whiteSquare), borderwidth = 0, highlightthickness= 0)
whiteSquare.grid(row=2,column=8)

######################

#ROW #3
whiteSquare58 = Button(root, image=whiteImage, command = lambda: onPress(("a",6), whiteSquare58), borderwidth = 0, highlightthickness= 0)
whiteSquare58.grid(row=3,column=1)
blackSquare18 = Button(root, image=blackImage, command = lambda: onPress(("b",6), blackSquare18), borderwidth = 0, highlightthickness = 0)
blackSquare18.grid(row=3,column=2)
whiteSquare11 = Button(root, image=whiteImage, command = lambda: onPress(("d",6), whiteSquare11), borderwidth = 0, highlightthickness= 0)
whiteSquare11.grid(row=3,column=3)
blackSquare34 = Button(root, image=blackImage, command = lambda: onPress(("d",6), blackSquare34), borderwidth = 0, highlightthickness = 0)
blackSquare34.grid(row=3,column=4)
whiteSquare26 = Button(root, image=whiteImage, command = lambda: onPress(("e",6), whiteSquare26), borderwidth = 0, highlightthickness= 0)
whiteSquare26.grid(row=3,column=5)
blackSquare50 = Button(root, image=blackImage, command = lambda: onPress(("f",6), blackSquare50), borderwidth = 0, highlightthickness = 0)
blackSquare50.grid(row=3,column=6)
whiteSquare43 = Button(root, image=whiteImage, command = lambda: onPress(("g",6), whiteSquare43), borderwidth = 0, highlightthickness= 0)
whiteSquare43.grid(row=3,column=7)
blackSquare2 = Button(root, image=blackImage, command = lambda: onPress(("h",6), blackSquare2), borderwidth = 0, highlightthickness = 0)
blackSquare2.grid(row=3,column=8)
#######################

#ROW 4
blackSquare59 = Button(root, image=blackImage, command = lambda: onPress(("a",5), blackSquare59), borderwidth = 0, highlightthickness = 0)
blackSquare59.grid(row=4,column=1)
whiteSquare19 = Button(root, image=whiteImage, command = lambda: onPress(("b",5), whiteSquare19), borderwidth = 0, highlightthickness= 0)
whiteSquare19.grid(row=4,column=2)
blackSquare12 = Button(root, image=blackImage, command = lambda: onPress(("c",5), blackSquare12), borderwidth = 0, highlightthickness = 0)
blackSquare12.grid(row=4,column=3)
whiteSquare35 = Button(root, image=whiteImage, command = lambda: onPress(("d",5), whiteSquare35), borderwidth = 0, highlightthickness= 0)
whiteSquare35.grid(row=4,column=4)
blackSquare27 = Button(root, image=blackImage, command = lambda: onPress(("e",5), blackSquare27), borderwidth = 0, highlightthickness = 0)
blackSquare27.grid(row=4,column=5)
whiteSquare51 = Button(root, image=whiteImage, command = lambda: onPress(("f",5), whiteSquare51), borderwidth = 0, highlightthickness= 0)
whiteSquare51.grid(row=4,column=6)
blackSquare44 = Button(root, image=blackImage, command = lambda: onPress(("g",5), blackSquare44), borderwidth = 0, highlightthickness = 0)
blackSquare44.grid(row=4,column=7)
whiteSquare2 = Button(root, image=whiteImage, command = lambda: onPress(("h",5), whiteSquare2), borderwidth = 0, highlightthickness= 0)
whiteSquare2.grid(row=4,column=8)
###########################

#ROW 5
whiteSquare60 = Button(root, image=whiteImage, command = lambda: onPress(("a",4), whiteSquare60), borderwidth = 0, highlightthickness= 0)
whiteSquare60.grid(row=5,column=1)
blackSquare20 = Button(root, image=blackImage, command = lambda: onPress(("b",4), blackSquare20), borderwidth = 0, highlightthickness = 0)
blackSquare20.grid(row=5,column=2)
whiteSquare13 = Button(root, image=whiteImage, command = lambda: onPress(("c",4), whiteSquare13), borderwidth = 0, highlightthickness= 0)
whiteSquare13.grid(row=5,column=3)
blackSquare36 = Button(root, image=blackImage, command = lambda: onPress(("d",4), blackSquare36), borderwidth = 0, highlightthickness = 0)
blackSquare36.grid(row=5,column=4)
whiteSquare28 = Button(root, image=whiteImage, command = lambda: onPress(("e",4), whiteSquare28), borderwidth = 0, highlightthickness= 0)
whiteSquare28.grid(row=5,column=5)
blackSquare52 = Button(root, image=blackImage, command = lambda: onPress(("f",4), blackSquare52), borderwidth = 0, highlightthickness = 0)
blackSquare52.grid(row=5,column=6)
whiteSquare45 = Button(root, image=whiteImage, command = lambda: onPress(("g",4), whiteSquare45), borderwidth = 0, highlightthickness= 0)
whiteSquare45.grid(row=5,column=7)
blackSquare4 = Button(root, image=blackImage, command = lambda: onPress(("h",4), blackSquare4), borderwidth = 0, highlightthickness = 0)
blackSquare4.grid(row=5,column=8)
######################

#ROW 6
blackSquare61 = Button(root, image=blackImage, command = lambda: onPress(("a",3), blackSquare61), borderwidth = 0, highlightthickness = 0)
blackSquare61.grid(row=6,column=1)
whiteSquare21 = Button(root, image=whiteImage, command = lambda: onPress(("b",3), whiteSquare21), borderwidth = 0, highlightthickness= 0)
whiteSquare21.grid(row=6,column=2)
blackSquare14 = Button(root, image=blackImage, command = lambda: onPress(("c",3), blackSquare14), borderwidth = 0, highlightthickness = 0)
blackSquare14.grid(row=6,column=3)
whiteSquare37 = Button(root, image=whiteImage, command = lambda: onPress(("d",3), whiteSquare37), borderwidth = 0, highlightthickness= 0)
whiteSquare37.grid(row=6,column=4)
blackSquare29 = Button(root, image=blackImage, command = lambda: onPress(("e",3), blackSquare29), borderwidth = 0, highlightthickness = 0)
blackSquare29.grid(row=6,column=5)
whiteSquare53 = Button(root, image=whiteImage, command = lambda: onPress(("f",3), whiteSquare53), borderwidth = 0, highlightthickness= 0)
whiteSquare53.grid(row=6,column=6)
blackSquare46 = Button(root, image=blackImage, command = lambda: onPress(("g",3), blackSquare46), borderwidth = 0, highlightthickness = 0)
blackSquare46.grid(row=6,column=7)
whiteSquare5 = Button(root, image=whiteImage, command = lambda: onPress(("h",3), whiteSquare5), borderwidth = 0, highlightthickness= 0)
whiteSquare5.grid(row=6,column=8)
#####################

#WHITE PAWNS ROW 7
whiteSquare62 = Button(root, image=wWhitePawn, command = lambda: onPress(("a",2), whiteSquare62), borderwidth = 0, highlightthickness= 0)
whiteSquare62.grid(row=7,column=1)
blackSquare22 = Button(root, image=bWhitePawn, command = lambda: onPress(("b",2), blackSquare22), borderwidth = 0, highlightthickness = 0)
blackSquare22.grid(row=7,column=2)
whiteSquare15 = Button(root, image=wWhitePawn, command = lambda: onPress(("c",2), whiteSquare15), borderwidth = 0, highlightthickness= 0)
whiteSquare15.grid(row=7,column=3)
blackSquare38 = Button(root, image=bWhitePawn, command = lambda: onPress(("d",2), blackSquare38), borderwidth = 0, highlightthickness = 0)
blackSquare38.grid(row=7,column=4)
whiteSquare30 = Button(root, image=wWhitePawn, command = lambda: onPress(("e",2), whiteSquare30), borderwidth = 0, highlightthickness= 0)
whiteSquare30.grid(row=7,column=5)
blackSquare54 = Button(root, image=bWhitePawn, command = lambda: onPress(("f",2),blackSquare54), borderwidth = 0, highlightthickness = 0)
blackSquare54.grid(row=7,column=6)
whiteSquare47 = Button(root, image=wWhitePawn, command = lambda: onPress(("g",2), whiteSquare47), borderwidth = 0, highlightthickness= 0)
whiteSquare47.grid(row=7,column=7)
blackSquare6 = Button(root, image=bWhitePawn, command = lambda: onPress(("h",2), blackSquare6), borderwidth = 0, highlightthickness = 0)
blackSquare6.grid(row=7,column=8)
##################


#WHITE PIECES ROW 8
blackSquare63 = Button(root, image=bWhiteRook, command = lambda: onPress(("a",1), blackSquare63), borderwidth = 0, highlightthickness = 0)
blackSquare63.grid(row=8,column=1)
whiteSquare23 = Button(root, image=wWhiteKnight, command = lambda: onPress(("b",1), whiteSquare23), borderwidth = 0, highlightthickness= 0)
whiteSquare23.grid(row=8,column=2)
blackSquare8 = Button(root, image=bWhiteBishop, command = lambda: onPress(("c",1), blackSquare8), borderwidth = 0, highlightthickness = 0)
blackSquare8.grid(row=8,column=3)
whiteSquare39 = Button(root, image=wWhiteQueen, command = lambda: onPress(("d",1), whiteSquare39), borderwidth = 0, highlightthickness= 0)
whiteSquare39.grid(row=8,column=4)
blackSquare31 = Button(root, image=bWhiteKing, command = lambda: onPress(("e",1), blackSquare31), borderwidth = 0, highlightthickness = 0)
blackSquare31.grid(row=8,column=5)
whiteSquare55 = Button(root, image=wWhiteBishop, command = lambda: onPress(("f",1), whiteSquare55), borderwidth = 0, highlightthickness= 0)
whiteSquare55.grid(row=8,column=6)
blackSquare40 = Button(root, image=bWhiteKnight, command = lambda: onPress(("g",1), blackSquare40), borderwidth = 0, highlightthickness = 0)
blackSquare40.grid(row=8,column=7)
whiteSquare7 = Button(root, image=wWhiteRook, command = lambda: onPress(("h",1), whiteSquare7), borderwidth = 0, highlightthickness= 0)
whiteSquare7.grid(row=8,column=8)
###################

def main(): 
    root.mainloop()
    
    

if __name__ == '__main__':
    main()


