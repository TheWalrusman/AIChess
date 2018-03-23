import Kboard
import Kpieces
import copy




#ourboard = [[0 for y in range(8)] for x in range(8)]
ourboard = Kboard.Board()
Fenstring = "rnbqkbnr/2pppppp/p7/1p7/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
Fenstring = "r6r/1nbqkbn1/1pppppp1/1p6/P7/1PPPPPPP/RNB1KBp1/3Q3R b - e3 0 1"
Fenstring = Fenstring.split()
rankcount = 0
filecount = 0
ilist = [0,1,2,3,4,5,6,7,8]
whitecastle = []
blackcastle = []
enpassant = ""
halfmove = 0
fullmove = 0
for letter in Fenstring[0]:
    None 
    if letter in 'p':
        ourboard.board[rankcount][filecount] = Kpieces.Pawn(rankcount,filecount,"Black","Pawn",ourboard)
        filecount += 1
    elif  letter in 'b':
        ourboard.board[rankcount][filecount] = Kpieces.Bishop(rankcount,filecount,"Black","Bishop",ourboard)
        filecount += 1
    elif  letter in 'r':
        ourboard.board[rankcount][filecount] = Kpieces.Rook(rankcount,filecount,"Black","Rook",ourboard)
        filecount += 1
    elif  letter in 'n':
        ourboard.board[rankcount][filecount] = Kpieces.Knight(rankcount,filecount,"Black","Knight",ourboard)
        filecount += 1
    elif  letter in 'q':
        ourboard.board[rankcount][filecount] = Kpieces.Queen(rankcount,filecount,"Black","Queen",ourboard)
        filecount += 1
    elif  letter in 'k':
        ourboard.board[rankcount][filecount] = Kpieces.King(rankcount,filecount,"Black","King",ourboard)
        filecount += 1
    elif letter in 'P':
        ourboard.board[rankcount][filecount] = Kpieces.Pawn(rankcount,filecount,"White","Pawn",ourboard)
        filecount += 1
    elif  letter in 'B':
        ourboard.board[rankcount][filecount] = Kpieces.Bishop(rankcount,filecount,"White","Bishop",ourboard)
        filecount += 1
    elif  letter in 'R':
        ourboard.board[rankcount][filecount] = Kpieces.Rook(rankcount,filecount,"White","Rook",ourboard)
        filecount += 1
    elif  letter in 'N':
        ourboard.board[rankcount][filecount] = Kpieces.Knight(rankcount,filecount,"White","Knight",ourboard)
        filecount += 1
    elif  letter in 'Q':
        ourboard.board[rankcount][filecount] = Kpieces.Queen(rankcount,filecount,"White","Queen",ourboard)
        filecount += 1
    elif  letter in 'K':
        ourboard.board[rankcount][filecount] = Kpieces.King(rankcount,filecount,"White","King",ourboard)
        filecount += 1
    elif  letter in '/':
        filecount = 0
        rankcount += 1
    elif int(letter) in ilist:
        filecount += int(letter)
for letter in Fenstring[1]:
    current_player = letter
    if(letter == 'w'):
        ourboard.currentplayer = "White"
    elif(letter == "b"):
        ourboard.currentplayer = "Black"
for letter in Fenstring[2]:
    if letter in 'Q':
        whitecastle.append(letter.upper())
        ourboard.whitecastleQ = [True]
        ourboard.board[7][0].moved = ourboard.whitecastleQ
    elif letter in 'K':
        whitecastle.append(letter.upper())
        ourboard.whitecastleK = [True]
        ourboard.board[7][7].moved = ourboard.whitecastleK
    elif letter in 'q':
        blackcastle.append(letter.upper())
        ourboard.blackcastleQ = [True]
        ourboard.board[0][0].moved = ourboard.blackcastleQ
    elif letter in 'k':
        blackcastle.append(letter.upper())
        ourboard.blackcastleK = [True]
        ourboard.board[0][7].moved = ourboard.blackcastleK
for letter in Fenstring[3]:
    enpassant += letter
    ourboard.enpassant += letter
for letter in Fenstring[4]:
    halfmove = int(letter)
for letter in Fenstring[5]:
    fullmove = int(letter)

newboard = copy.deepcopy(ourboard)
newboard.board[0][0].player = "HIIIIIII"
ourboard.pretty()
#ourboard.whitecastleQ[0] = "HIIIIIIII"
for rows in ourboard.board:
    for piece in rows:
        if(isinstance(piece,Kpieces.King) and (piece.player == ourboard.currentplayer)):
            piece.actions()


None