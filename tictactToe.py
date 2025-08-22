import random,sys
theBoard={"top":[[" ",0],[" ",0],[" ",0]],
            "middle":[[" ",0],[" ",0],[" ",0]],
            "bottom":[[" ",0],[" ",0],[" ",0]]
        
            }
# X=4 and O=3 s
WIN_STATEX=12
WIN_STATEO=9
#Draw occurs when there are 5 Xs and 4 Os or 4 Xs and 5 Os 
DRAW_STATES=[31,32]
#Get name of players
player1=input("Name of player 1? ")
player2=input("Name of player 2? ")
def printBoard(board):
    #First Row
    print(f"{board["top"][0][0]}|{board["top"][1][0]}|{board["top"][2][0]}")
    print("-+-+-")
    #Second row
    print(f"{board["middle"][0][0]}|{board["middle"][1][0]}|{board["middle"][2][0]}")
    print("-+-+-")
    #Third Row
    print(f"{board["bottom"][0][0]}|{board["bottom"][1][0]}|{board["bottom"][2][0]}")
    print("\n")
    
    
def startGame():
    print("TIC-TAC-TOE")
    print("MOVES ARE THE POSITIONS ON THE BOARD")
    print(""" 
VALID POSITIONS ON BOARD:
top-1,top-2,top-3,middle-1,bottom-1 and so on..... Numbered from left to Right
""")
    #Randomly give X and O to each player
    print(f"{player1} is X and {player2} is O")
    
    print(f"{player2} is O and {player1} is X")

#Get player moves
def playMove1():
    while True:
        move1=input(f"What is your move {player1}? ")
        #Geting top,left or bottom row
        row_name=move1.split(sep="-")[0]
        #Geting Column in that row
        #Subtract 1 to convert to index
        row_column=int(move1.split(sep="-")[1])-1
        #Check valid moves
        if row_name in theBoard.keys():
            theBoard[row_name][row_column][0]="X"
            theBoard[row_name][row_column][1]=4
            printBoard(theBoard)
            break
        else:
            print("INVALID MOVE")
            print("MOVES ARE POS ON BOARD")

def playMove2():
    while True:
        move2=input(f"What is your move {player2}? ")
        #Geting top,left or bottom row
        row_name=move2.split(sep="-")[0]
        #Geting Column in that row
        #Subtract 1 to convert to index
        row_column=int(move2.split(sep="-")[1])-1
        #Check valid moves
        if row_name in theBoard.keys():
            theBoard[row_name][row_column][0]="O"
            theBoard[row_name][row_column][1]=3
            printBoard(theBoard)
            break
        else:
            print("INVALID MOVE")
            print("MOVES ARE POS ON BOARD")
#Function to determine who won            
def hasWon(board):
    sumTop=theBoard["top"][0][1]+theBoard["top"][1][1]+theBoard["top"][2][1]
    sumMiddle=theBoard["middle"][0][1]+theBoard["middle"][1][1]+theBoard["middle"][2][1]
    sumBottom=theBoard["bottom"][0][1]+theBoard["bottom"][1][1]+theBoard["bottom"][2][1]
    sumlDiagonal=theBoard["top"][0][1]+theBoard["middle"][1][1]+theBoard["bottom"][2][1]
    sumrDiagonal=theBoard["top"][2][1]+theBoard["middle"][1][1]+theBoard["bottom"][0][1]
    sumBoard=sumTop+sumMiddle+sumBottom
    if sumTop==WIN_STATEX or sumMiddle==WIN_STATEX or sumBottom==WIN_STATEX or sumlDiagonal==WIN_STATEX or sumrDiagonal==WIN_STATEX:
        print(f"{player1} won")
        sys.exit()
    elif sumTop==WIN_STATEO or sumMiddle==WIN_STATEO or sumBottom==WIN_STATEO or sumlDiagonal==WIN_STATEO or sumrDiagonal==WIN_STATEO:
        print(f"{player2} won")
        sys.exit()
    elif sumBoard in DRAW_STATES:
        print("Tie!")
        sys.exit()

def main():
    startGame()
    while True:
        hasWon(theBoard)
        playMove1()
        playMove2()



main()