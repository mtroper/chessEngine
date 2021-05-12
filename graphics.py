from tkinter import *
from Bishop import Bishop
from King import King
from Queen import Queen
from Rook import Rook
from Pawn import Pawn
from Knight import Knight


# white pieces

blackPawn1 = Pawn("black", (1,0))
blackPawn2 = Pawn("black", (1,1))
blackPawn3 = Pawn("black", (1,2))
blackPawn4 = Pawn("black", (1,3))
blackPawn5 = Pawn("black", (1,4))
blackPawn6 = Pawn("black", (1,5))
blackPawn7 = Pawn("black", (1,6))
blackPawn8 = Pawn("black", (1,7))

blackRook1 = Rook("black", (0,0))
blackRook2 = Rook("black", (0,7))

blackKnight1 = Knight("black", (0,1))
blackKnight2 = Knight("black", (0,6))

blackBishop1 = Bishop("black", (0,2))
blackBishop2 = Bishop("black", (0,5))

blackQueen = Queen("black", (0,3))
blackKing = King("black", (0,4))

# black pieces

whitePawn1 = Pawn("white", (6,0))
whitePawn2 = Pawn("white", (6,1))
whitePawn3 = Pawn("white", (6,2))
whitePawn4 = Pawn("white", (6,3))
whitePawn5 = Pawn("white", (6,4))
whitePawn6 = Pawn("white", (6,5))
whitePawn7 = Pawn("white", (6,6))
whitePawn8 = Pawn("white", (6,7))

whiteRook1 = Rook("white", (7,0))
whiteRook2 = Rook("white", (7,7))

whiteKnight1 = Knight("white", (7,1))
whiteKnight2 = Knight("white", (7,6))

whiteBishop1 = Bishop("white", (7,2))
whiteBishop2 = Bishop("white", (7,5))

whiteQueen = Queen("white", (7,3))
whiteKing = King("white", (7,4))

board =[
    [blackRook1,blackKnight1,blackBishop1,blackQueen,blackKing,blackBishop2,blackKnight2,blackRook2],
    [blackPawn1,blackPawn2,blackPawn3,blackPawn4,blackPawn5,blackPawn6,blackPawn7,blackPawn8],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [whitePawn1,whitePawn2,whitePawn3,whitePawn4,whitePawn5,whitePawn6,whitePawn7,whitePawn8],
    [whiteRook1,whiteKnight1,whiteBishop1,whiteQueen,whiteKing,whiteBishop2,whiteKnight2,whiteRook2],
]

# piece is a piece class (Rook, Pawn, etc.)
# target is a tuple (row,col)

#returns tuple:  (isValid, board)

#isValid is a boolean, true if valid, false if not
def isValid(piece, target, board):
    if piece == 0:
        print("Invalid, no piece selected")

        return (False, board)
    (row1,col1) = piece.position
    (row2,col2) = target


    #Case -1: pawn double jump
    if piece.getClass() == "Pawn":
        if piece.color == "white":
            if row1 == 6 and col2 == col1:
                if row2 == 4:
                    print("double jump")
                    return (True,board)
        if piece.color == "black":
            if row1 == 1 and col2 == col1:
                if row2 == 3:
                    print("double jump")
                    return (True,board)



    #Case 0: if target not in the available moves
    if target not in piece.moves():
        print("Case 0")
        print("Invalid, not in available moves")
        print("Available Moves: " + str(piece.moves()) )
        return (False, board)

    #Case 1: if there is a piece of the same color occupuying target_square
    if board[row2][col2] != 0:
        print("Case 1")
        if board[row2][col2].color == piece.color:
            print("Invalid, landing on occupied square")
            print("Occupied Square: " + str(board[row2][col2]))
            return (False, board)

    #Case 2: if there are pieces in the way (ignore for knight class, king class, and pawn class)
    if piece.getClass() == "Rook":
        print("Case 2, Rook")
        #if move is to the left
        if col2 < col1:
            i = 1
            while(col1 - i != col2):
                if board[row1][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is to the right
        elif col2 > col1:
            i = 1
            while(col1 + i != col2):
                if board[row1][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is down
        elif row2 > row1:
            i = 1
            while(row1 + i != row2):
                if board[row1 + i][col1] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is up
        elif row2 < row1:
            i = 1
            while(row1 - i != row2):
                if board[row1 - i][col1] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
    if piece.getClass() == "Bishop":
        print("Case 2, Bishop")
        #if move is down left
        if row2 > row1 and col2 < col1:
            i = 1
            while(row1 + i != row2 and col1 - i != col2):
                if board[row1 + i][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is down right
        if row2 > row1 and col2 > col1:
            i = 1
            while(row1 + i != row2 and col1 + i != col2):
                if board[row1 + i][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is upper left
        if row2 < row1 and col2 < col1:
            i = 1
            while(row1 - i != row2 and col1 - i != col2):
                if board[row1 - i][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is upper right
        if row2 < row1 and col2 > col1:
            i = 1
            while(row1 - i != row2 and col1 + i != col2):
                if board[row1 - i][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
    if piece.getClass() == "Queen":
        #if move is to the left
        if col2 < col1 and row2 == row1:
            i = 1
            while(col1 - i != col2):
                if board[row1][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is to the right
        elif col2 > col1 and row2 == row1:
            i = 1
            while(col1 + i != col2):
                if board[row1][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is up
        elif row2 > row1 and col2 == col1:
            i = 1
            while(row1 + i != row2):
                if board[row1 + i][col1] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is down
        elif row2 < row1 and col2 == col1:
            i = 1
            while(row1 - i != row2):
                if board[row1 - i][col1] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is down left
        if row2 > row1 and col2 < col1:
            i = 1
            while(row1 + i != row2 and col1 - i != col2):
                if board[row1 + i][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is down right
        if row2 > row1 and col2 > col1:
            i = 1
            while(row1 + i != row2 and col1 + i != col2):
                if board[row1 + i][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is upper left
        if row2 < row1 and col2 < col1:
            i = 1
            while(row1 - i != row2 and col1 - i != col2):
                if board[row1 - i][col1 - i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1
        #if move is upper right
        if row2 < row1 and col2 > col1:
            i = 1
            while(row1 - i != row2 and col1 + i != col2):
                if board[row1 - i][col1 + i] != 0:
                    print("Invalid, there is a piece in the way")
                    return (False, board)
                i += 1


    #Case 3: Pawn Special - moving, eating, double jump
    if piece.getClass() == "Pawn":
        #Pawn is white
        if piece.color == "white":
            #moving up
            if row2 < row1 and col2 == col1:
                print("moving up")
                
                if target not in piece.moves():
                    print("Invalid, not in piece.moves")
                    print(piece.moves())
                    return (False, board)
            #upper right eating
            if row2 == row1 - 1 and col2 == col1 + 1:
                if board[row2][col2] == 0:
                    print("Invalid")
                    return (False, board)
                elif board[row2][col2].color != piece.color:
                    pass
            #upper left eating
            if row2 == row1 - 1 and col2 == col1 - 1:
                if board[row2][col2] == 0:
                    print("Invalid")
                    return (False, board)
                elif board[row2][col2].color != piece.color:
                    pass
        else:
        #Pawn is black
            #moving up
            if row2 == row1 +1 and col2 == col1:
                print("moving up")
                if target not in piece.moves():
                    print("Invalid, not in piece.moves")
                    print(piece.moves())
                    return (False, board)
            #upper right eating
            if row2 == row1 + 1 and col2 == col1 + 1:
                if board[row2][col2] == 0:
                    print("Invalid")
                    return (False, board)
                elif board[row2][col2].color != piece.color:
                    pass
            #upper left eating
            if row2 == row1 + 1 and col2 == col1 - 1:
                if board[row2][col2] == 0:
                    print("Invalid")
                    return (False, board)
                elif board[row2][col2].color != piece.color:
                    pass
    #Case 4: Castling
    if piece.getClass() == "King":
        pass
    
    #Case 5: En Passant
    if piece.getClass() == "Pawn":
        pass
    
    #Promotion, Check/Checkmate



   
    #sets piece current position to target position
    piece.position = target

    # no need to change the actual board here
    # print("piece.position: " + str(piece.position))
    # board[row2][col2] = piece
    # print("board[row2][col2]: " + str(board[row2][col2]))
    # #sets where piece used to be to 0
    # board[row1][col1] = 0
    # print("board[row1][col1]: " + str(board[row1][col1]))
    # print("_________")
    return (True, board)



moves = []
currentSquare = []
def onPress(board, square, squareid):
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

        
        print("row1: " + str(row1) + ", col1: " + str(col1))
        print("row2: " + str(row2) + ", col2: " + str(col2))

        (valid, tempBoard) = isValid(board[row1][col1], (row2,col2), board)
        board = tempBoard

        if not valid:
            print("___________")
            moveText = "INVALID"
        else:
            capture = False
            if board[row1][col1] != 0 and board[row2][col2] != 0:
                board[row2][col2] = board[row1][col1]
                board[row1][col1] = 0
                capture = True
            else:
                temp1 = board[row1][col1]
                board[row1][col1] = board[row2][col2]
                board[row2][col2] = temp1

            before = int(str(currentSquare[-1].cget("image"))[-1])
            after = int(str(squareid.cget("image"))[-1])
            if before%2 != after%2:
                difference = -1
                if before%2 == 1:
                    difference = 1
                newAfter = str(squareid.cget("image"))[:-1] + str((after - difference))
                newBefore = str(currentSquare[-1].cget("image"))[:-1] + str((before + difference))
                squareid.configure(image = newBefore)
                if capture and before%2 == 1:
                    currentSquare[-1].configure(image = whiteImage)
                elif capture and before%2 == 0:
                    currentSquare[-1].configure(image = blackImage)
                else:
                    currentSquare[-1].configure(image = newAfter)
            else:
                if capture:
                    temp = currentSquare[-1].cget("image")
                    if after%2 == 1:
                        currentSquare[-1].configure(image = whiteImage)
                    else:
                        currentSquare[-1].configure(image = blackImage)
                    squareid.configure(image = temp)
                else:
                    temp = squareid.cget("image")
                    squareid.configure(image = currentSquare[-1].cget("image"))
                    currentSquare[-1].configure(image = temp)

                # if row2 == 0 and board[row2][col2] == "wp":
                #     print("promotion white")
                # elif row2 == 7 and board[row2][col2] == "bp":
                #     print("promotion black")

    else:
        moveText += moves[-1]
        currentSquare.append(squareid)
    topPadding.configure(text = moveText)

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
whiteSquare56 = Button(root, image=wBlackRook, command = lambda: onPress(board, ("a",8), whiteSquare56), borderwidth = 0, highlightthickness= 0)
whiteSquare56.grid(row=1,column=1)
blackSquare16 = Button(root, image=bBlackKnight, command = lambda: onPress(board, ("b",8), blackSquare16), borderwidth = 0, highlightthickness = 0)
blackSquare16.grid(row=1,column=2)
whiteSquare9 = Button(root, image=wBlackBishop, command = lambda: onPress(board, ("c",8), whiteSquare9), borderwidth = 0, highlightthickness= 0)
whiteSquare9.grid(row=1,column=3)
blackSquare32 = Button(root, image=bBlackQueen, command = lambda: onPress(board, ("d",8), blackSquare32), borderwidth = 0, highlightthickness = 0)
blackSquare32.grid(row=1,column=4)
whiteSquare24 = Button(root, image=wBlackKing, command = lambda: onPress(board, ("e",8), whiteSquare24), borderwidth = 0, highlightthickness= 0)
whiteSquare24.grid(row=1,column=5)
blackSquare48 = Button(root, image=bBlackBishop, command = lambda: onPress(board, ("f",8), blackSquare48), borderwidth = 0, highlightthickness = 0)
blackSquare48.grid(row=1,column=6)
whiteSquare41 = Button(root, image=wBlackKnight, command = lambda: onPress(board, ("g",8), whiteSquare41), borderwidth = 0, highlightthickness= 0)
whiteSquare41.grid(row=1,column=7)
blackSquare = Button(root, image=bBlackRook, command = lambda: onPress(board, ("h",8), blackSquare), borderwidth = 0, highlightthickness = 0)
blackSquare.grid(row=1,column=8)
#####################

#BLACK PAWN ROW 2
blackSquare57 = Button(root, image=bBlackPawn, command = lambda: onPress(board, ("a",7), blackSquare57), borderwidth = 0, highlightthickness = 0)
blackSquare57.grid(row=2,column=1)
whiteSquare17 = Button(root, image=wBlackPawn, command = lambda: onPress(board, ("b",7), whiteSquare17), borderwidth = 0, highlightthickness= 0)
whiteSquare17.grid(row=2,column=2)
blackSquare10 = Button(root, image=bBlackPawn, command = lambda: onPress(board, ("c",7), blackSquare10), borderwidth = 0, highlightthickness = 0)
blackSquare10.grid(row=2,column=3)
whiteSquare33 = Button(root, image=wBlackPawn, command = lambda: onPress(board, ("d",7), whiteSquare33), borderwidth = 0, highlightthickness= 0)
whiteSquare33.grid(row=2,column=4)
blackSquare25 = Button(root, image=bBlackPawn, command = lambda: onPress(board, ("e",7), blackSquare25), borderwidth = 0, highlightthickness = 0)
blackSquare25.grid(row=2,column=5)
whiteSquare49 = Button(root, image=wBlackPawn, command = lambda: onPress(board, ("f",7), whiteSquare49), borderwidth = 0, highlightthickness= 0)
whiteSquare49.grid(row=2,column=6)
blackSquare42 = Button(root, image=bBlackPawn, command = lambda: onPress(board, ("g",7), blackSquare42), borderwidth = 0, highlightthickness = 0)
blackSquare42.grid(row=2,column=7)
whiteSquare = Button(root, image=wBlackPawn, command = lambda: onPress(board, ("h",7), whiteSquare), borderwidth = 0, highlightthickness= 0)
whiteSquare.grid(row=2,column=8)

######################

#ROW #3
whiteSquare58 = Button(root, image=whiteImage, command = lambda: onPress(board, ("a",6), whiteSquare58), borderwidth = 0, highlightthickness= 0)
whiteSquare58.grid(row=3,column=1)
blackSquare18 = Button(root, image=blackImage, command = lambda: onPress(board, ("b",6), blackSquare18), borderwidth = 0, highlightthickness = 0)
blackSquare18.grid(row=3,column=2)
whiteSquare11 = Button(root, image=whiteImage, command = lambda: onPress(board, ("c",6), whiteSquare11), borderwidth = 0, highlightthickness= 0)
whiteSquare11.grid(row=3,column=3)
blackSquare34 = Button(root, image=blackImage, command = lambda: onPress(board, ("d",6), blackSquare34), borderwidth = 0, highlightthickness = 0)
blackSquare34.grid(row=3,column=4)
whiteSquare26 = Button(root, image=whiteImage, command = lambda: onPress(board, ("e",6), whiteSquare26), borderwidth = 0, highlightthickness= 0)
whiteSquare26.grid(row=3,column=5)
blackSquare50 = Button(root, image=blackImage, command = lambda: onPress(board, ("f",6), blackSquare50), borderwidth = 0, highlightthickness = 0)
blackSquare50.grid(row=3,column=6)
whiteSquare43 = Button(root, image=whiteImage, command = lambda: onPress(board, ("g",6), whiteSquare43), borderwidth = 0, highlightthickness= 0)
whiteSquare43.grid(row=3,column=7)
blackSquare2 = Button(root, image=blackImage, command = lambda: onPress(board, ("h",6), blackSquare2), borderwidth = 0, highlightthickness = 0)
blackSquare2.grid(row=3,column=8)
#######################

#ROW 4
blackSquare59 = Button(root, image=blackImage, command = lambda: onPress(board, ("a",5), blackSquare59), borderwidth = 0, highlightthickness = 0)
blackSquare59.grid(row=4,column=1)
whiteSquare19 = Button(root, image=whiteImage, command = lambda: onPress(board, ("b",5), whiteSquare19), borderwidth = 0, highlightthickness= 0)
whiteSquare19.grid(row=4,column=2)
blackSquare12 = Button(root, image=blackImage, command = lambda: onPress(board, ("c",5), blackSquare12), borderwidth = 0, highlightthickness = 0)
blackSquare12.grid(row=4,column=3)
whiteSquare35 = Button(root, image=whiteImage, command = lambda: onPress(board, ("d",5), whiteSquare35), borderwidth = 0, highlightthickness= 0)
whiteSquare35.grid(row=4,column=4)
blackSquare27 = Button(root, image=blackImage, command = lambda: onPress(board, ("e",5), blackSquare27), borderwidth = 0, highlightthickness = 0)
blackSquare27.grid(row=4,column=5)
whiteSquare51 = Button(root, image=whiteImage, command = lambda: onPress(board, ("f",5), whiteSquare51), borderwidth = 0, highlightthickness= 0)
whiteSquare51.grid(row=4,column=6)
blackSquare44 = Button(root, image=blackImage, command = lambda: onPress(board, ("g",5), blackSquare44), borderwidth = 0, highlightthickness = 0)
blackSquare44.grid(row=4,column=7)
whiteSquare2 = Button(root, image=whiteImage, command = lambda: onPress(board, ("h",5), whiteSquare2), borderwidth = 0, highlightthickness= 0)
whiteSquare2.grid(row=4,column=8)
###########################

#ROW 5
whiteSquare60 = Button(root, image=whiteImage, command = lambda: onPress(board, ("a",4), whiteSquare60), borderwidth = 0, highlightthickness= 0)
whiteSquare60.grid(row=5,column=1)
blackSquare20 = Button(root, image=blackImage, command = lambda: onPress(board, ("b",4), blackSquare20), borderwidth = 0, highlightthickness = 0)
blackSquare20.grid(row=5,column=2)
whiteSquare13 = Button(root, image=whiteImage, command = lambda: onPress(board, ("c",4), whiteSquare13), borderwidth = 0, highlightthickness= 0)
whiteSquare13.grid(row=5,column=3)
blackSquare36 = Button(root, image=blackImage, command = lambda: onPress(board, ("d",4), blackSquare36), borderwidth = 0, highlightthickness = 0)
blackSquare36.grid(row=5,column=4)
whiteSquare28 = Button(root, image=whiteImage, command = lambda: onPress(board, ("e",4), whiteSquare28), borderwidth = 0, highlightthickness= 0)
whiteSquare28.grid(row=5,column=5)
blackSquare52 = Button(root, image=blackImage, command = lambda: onPress(board, ("f",4), blackSquare52), borderwidth = 0, highlightthickness = 0)
blackSquare52.grid(row=5,column=6)
whiteSquare45 = Button(root, image=whiteImage, command = lambda: onPress(board, ("g",4), whiteSquare45), borderwidth = 0, highlightthickness= 0)
whiteSquare45.grid(row=5,column=7)
blackSquare4 = Button(root, image=blackImage, command = lambda: onPress(board, ("h",4), blackSquare4), borderwidth = 0, highlightthickness = 0)
blackSquare4.grid(row=5,column=8)
######################

#ROW 6
blackSquare61 = Button(root, image=blackImage, command = lambda: onPress(board, ("a",3), blackSquare61), borderwidth = 0, highlightthickness = 0)
blackSquare61.grid(row=6,column=1)
whiteSquare21 = Button(root, image=whiteImage, command = lambda: onPress(board, ("b",3), whiteSquare21), borderwidth = 0, highlightthickness= 0)
whiteSquare21.grid(row=6,column=2)
blackSquare14 = Button(root, image=blackImage, command = lambda: onPress(board, ("c",3), blackSquare14), borderwidth = 0, highlightthickness = 0)
blackSquare14.grid(row=6,column=3)
whiteSquare37 = Button(root, image=whiteImage, command = lambda: onPress(board, ("d",3), whiteSquare37), borderwidth = 0, highlightthickness= 0)
whiteSquare37.grid(row=6,column=4)
blackSquare29 = Button(root, image=blackImage, command = lambda: onPress(board, ("e",3), blackSquare29), borderwidth = 0, highlightthickness = 0)
blackSquare29.grid(row=6,column=5)
whiteSquare53 = Button(root, image=whiteImage, command = lambda: onPress(board, ("f",3), whiteSquare53), borderwidth = 0, highlightthickness= 0)
whiteSquare53.grid(row=6,column=6)
blackSquare46 = Button(root, image=blackImage, command = lambda: onPress(board, ("g",3), blackSquare46), borderwidth = 0, highlightthickness = 0)
blackSquare46.grid(row=6,column=7)
whiteSquare5 = Button(root, image=whiteImage, command = lambda: onPress(board, ("h",3), whiteSquare5), borderwidth = 0, highlightthickness= 0)
whiteSquare5.grid(row=6,column=8)
#####################

#WHITE PAWNS ROW 7
whiteSquare62 = Button(root, image=wWhitePawn, command = lambda: onPress(board, ("a",2), whiteSquare62), borderwidth = 0, highlightthickness= 0)
whiteSquare62.grid(row=7,column=1)
blackSquare22 = Button(root, image=bWhitePawn, command = lambda: onPress(board, ("b",2), blackSquare22), borderwidth = 0, highlightthickness = 0)
blackSquare22.grid(row=7,column=2)
whiteSquare15 = Button(root, image=wWhitePawn, command = lambda: onPress(board, ("c",2), whiteSquare15), borderwidth = 0, highlightthickness= 0)
whiteSquare15.grid(row=7,column=3)
blackSquare38 = Button(root, image=bWhitePawn, command = lambda: onPress(board, ("d",2), blackSquare38), borderwidth = 0, highlightthickness = 0)
blackSquare38.grid(row=7,column=4)
whiteSquare30 = Button(root, image=wWhitePawn, command = lambda: onPress(board, ("e",2), whiteSquare30), borderwidth = 0, highlightthickness= 0)
whiteSquare30.grid(row=7,column=5)
blackSquare54 = Button(root, image=bWhitePawn, command = lambda: onPress(board, ("f",2),blackSquare54), borderwidth = 0, highlightthickness = 0)
blackSquare54.grid(row=7,column=6)
whiteSquare47 = Button(root, image=wWhitePawn, command = lambda: onPress(board, ("g",2), whiteSquare47), borderwidth = 0, highlightthickness= 0)
whiteSquare47.grid(row=7,column=7)
blackSquare6 = Button(root, image=bWhitePawn, command = lambda: onPress(board, ("h",2), blackSquare6), borderwidth = 0, highlightthickness = 0)
blackSquare6.grid(row=7,column=8)
##################


#WHITE PIECES ROW 8
blackSquare63 = Button(root, image=bWhiteRook, command = lambda: onPress(board, ("a",1), blackSquare63), borderwidth = 0, highlightthickness = 0)
blackSquare63.grid(row=8,column=1)
whiteSquare23 = Button(root, image=wWhiteKnight, command = lambda: onPress(board, ("b",1), whiteSquare23), borderwidth = 0, highlightthickness= 0)
whiteSquare23.grid(row=8,column=2)
blackSquare8 = Button(root, image=bWhiteBishop, command = lambda: onPress(board, ("c",1), blackSquare8), borderwidth = 0, highlightthickness = 0)
blackSquare8.grid(row=8,column=3)
whiteSquare39 = Button(root, image=wWhiteQueen, command = lambda: onPress(board, ("d",1), whiteSquare39), borderwidth = 0, highlightthickness= 0)
whiteSquare39.grid(row=8,column=4)
blackSquare31 = Button(root, image=bWhiteKing, command = lambda: onPress(board, ("e",1), blackSquare31), borderwidth = 0, highlightthickness = 0)
blackSquare31.grid(row=8,column=5)
whiteSquare55 = Button(root, image=wWhiteBishop, command = lambda: onPress(board, ("f",1), whiteSquare55), borderwidth = 0, highlightthickness= 0)
whiteSquare55.grid(row=8,column=6)
blackSquare40 = Button(root, image=bWhiteKnight, command = lambda: onPress(board, ("g",1), blackSquare40), borderwidth = 0, highlightthickness = 0)
blackSquare40.grid(row=8,column=7)
whiteSquare7 = Button(root, image=wWhiteRook, command = lambda: onPress(board, ("h",1), whiteSquare7), borderwidth = 0, highlightthickness= 0)
whiteSquare7.grid(row=8,column=8)
###################

def main(): 
    root.mainloop()
    
    

if __name__ == '__main__':
    main()


